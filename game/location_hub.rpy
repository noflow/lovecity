## location_hub.rpy — In-location screen
## ═══════════════════════════════════════════════════════════════
##
## When the player enters a location they see:
##   - Full-screen background image for that location
##   - Characters present as clickable portrait buttons
##   - Available actions in a bottom panel
##   - Quick travel back to map
##
## This is the main interaction screen — Summertime Saga style.
## ═══════════════════════════════════════════════════════════════

## ── LOCATION HUB SCREEN ─────────────────────────────────────────
screen lc_location_hub(loc_id, npcs_here, loc_actions):
    tag hub
    zorder 50

    python:
        loc_info = LOCATIONS.get(loc_id, {"name": loc_id, "icon": "📍"})
        loc_name = loc_info["name"]
        loc_icon = loc_info["icon"]

    # ── Background is set via scene command in sandbox.rpy ──
    # ── (already showing from set_background call) ──

    # Location name top-left
    frame:
        xpos        14
        ypos        50
        background  "#07071088"
        padding     (12, 8)
        hbox:
            spacing 8
            text loc_icon size 20 yalign 0.5
            text loc_name color "#f472b6" bold True size 18 yalign 0.5
            text "[time_str()]" color "#60a5fa" size 14 yalign 0.5

    # ── Map button (top right) ──
    frame:
        xalign  1.0
        ypos    50
        xpos    -14
        background "#07071088"
        padding    (10, 7)
        hbox:
            spacing 8
            textbutton "🗺️ Map":
                action Return(("goto_map", None))
                idle_color  "#94a3b8"
                hover_color "#60a5fa"
                background  "#1e293b"
                hover_background "#334155"
                padding     (12, 7)

    # ── NPC characters present ───────────────────────────────────
    # Placed at centre-left of screen, large clickable portraits
    if npcs_here:
        hbox:
            xalign  0.5
            ypos    200
            spacing 24
            for npc_id in npcs_here:
                python:
                    npc         = NPC_DATA.get(npc_id, {"name": npc_id})
                    npc_name    = npc["name"]
                    npc_job     = npc.get("job", "")
                    rel_val     = getattr(store, "rel_" + npc_id, 0)
                    rel_lbl     = rel_label(rel_val)
                    has_sprite  = renpy.loadable("characters/" + npc_id + "/neutral.png")
                    met_flag    = getattr(store, "flag_met_" + npc_id, False)
                    is_dating   = store.dating.get(npc_id, False)
                    npc_col     = "#f472b6"

                imagebutton:
                    xsize   140
                    ysize   220
                    idle    Frame(Solid("#0f172a88"), 16, 16)
                    hover   Frame(Solid("#f472b622"), 16, 16)
                    action  Return(("talk", npc_id))

                    has vbox:
                        xalign 0.5
                        spacing 6

                        # Portrait or emoji placeholder
                        frame:
                            xalign      0.5
                            xsize       110
                            ysize       150
                            background  "#0a0a1e"
                            if has_sprite:
                                add ("characters/" + npc_id + "/neutral.png") fit "contain" xalign 0.5 yalign 1.0
                            else:
                                vbox:
                                    xalign 0.5
                                    yalign 0.5
                                    # Big emoji stand-in
                                    text ("❤️" if is_dating else "👤") size 56 xalign 0.5
                                    text (npc_name.split()[0]) size 11 color npc_col xalign 0.5 text_align 0.5

                        # Name
                        text npc_name.split()[0] size 14 bold True color npc_col xalign 0.5

                        # Relationship level
                        text rel_lbl size 11 color "#475569" xalign 0.5

                        # Dating heart
                        if is_dating:
                            text "💕" size 14 xalign 0.5

    else:
        # Nobody here
        frame:
            xalign  0.5
            ypos    280
            background "#07071066"
            padding    (30, 20)
            vbox:
                xalign 0.5
                spacing 6
                text "Nobody around right now." color "#334155" italic True size 16 xalign 0.5
                text "Come back at a different time of day." color "#1e293b" size 13 xalign 0.5

    # ── Bottom action panel ──────────────────────────────────────
    frame:
        xfill   True
        yalign  1.0
        background "#07071099"
        padding    (16, 14)

        vbox:
            spacing 10

            # Actions row
            hbox:
                spacing 10
                xfill True

                if loc_actions:
                    for action_id, action_label in loc_actions:
                        textbutton "[action_label]":
                            action  Return(("action", action_id))
                            idle_color   "#94a3b8"
                            hover_color  "#e2e8f0"
                            background   "#1e293b"
                            hover_background "#334155"
                            padding      (12, 9)

                null xfill True

                # Wait button
                textbutton "⏭️ Wait":
                    action  Return(("wait", None))
                    idle_color   "#94a3b8"
                    hover_color  "#fbbf24"
                    background   "#1e293b55"
                    hover_background "#334155"
                    padding      (12, 9)

            # Stat strip
            hbox:
                spacing 20
                xfill True
                text "💰 $[stat_money]"       color "#34d399" size 13
                text "⚡ [stat_energy]%"      color "#fbbf24" size 13
                text "😊 [stat_happiness]%"   color "#f472b6" size 13
                null xfill True
                text "Day [time_day]  [time_str()]" color "#475569" size 13

## ── HOME HUB — room picker inside the house ─────────────────────
screen lc_home_hub():
    tag hub
    zorder 50

    # Background
    add Solid(bg_colors.get("bg_home", "#1a1230"))

    # Header
    frame:
        xpos        14
        ypos        50
        background  "#07071088"
        padding     (12, 8)
        hbox:
            spacing 8
            text "🏠" size 20 yalign 0.5
            text "Home" color "#f472b6" bold True size 18 yalign 0.5
            text "[time_str()]" color "#60a5fa" size 14 yalign 0.5

    # Map button
    frame:
        xalign  1.0
        ypos    50
        xpos    -14
        background "#07071088"
        padding    (10, 7)
        textbutton "🗺️ Map":
            action Return(("goto_map", None))
            idle_color  "#94a3b8"
            hover_color "#60a5fa"
            background  "#1e293b"
            hover_background "#334155"
            padding     (12, 7)

    # Room buttons — grid
    vbox:
        xalign  0.5
        ypos    140
        spacing 16

        text "Which room?" color "#f472b6" bold True size 20 xalign 0.5

        hbox:
            xalign  0.5
            spacing 16
            for room_id, room_info in HOME_ROOMS.items():
                python:
                    # Who's in this room?
                    npcs_in_room = []
                    for npc_id in ["mom", "sister"]:
                        npc_loc, npc_room, _ = get_npc_location(npc_id)
                        if npc_loc == "home" and (npc_room == room_id or npc_room is None):
                            npcs_in_room.append(npc_id)

                imagebutton:
                    xsize   160
                    ysize   130
                    idle    Frame(Solid("#0f172a99"), 14, 14)
                    hover   Frame(Solid("#f472b622"), 14, 14)
                    action  Return(("enter_room", room_id))

                    has vbox:
                        xalign 0.5
                        spacing 6
                        text room_info["icon"] size 38 xalign 0.5
                        text room_info["name"] size 14 bold True color "#e2e8f0" xalign 0.5 text_align 0.5
                        if npcs_in_room:
                            hbox:
                                xalign 0.5
                                spacing 4
                                for npc_id in npcs_in_room:
                                    python:
                                        npc = NPC_DATA.get(npc_id, {})
                                    text npc.get("name","?").split()[0] size 11 color "#f472b6"
