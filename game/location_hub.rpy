## location_hub.rpy — In-location screen
## ═══════════════════════════════════════════════════════════════

## ── LOCATION HUB SCREEN (non-home locations) ────────────────────
screen lc_location_hub(loc_id, npcs_here, loc_actions):
    tag hub
    zorder 50

    # Background — rendered inside screen, never uses scene
    python:
        bg_key   = _current_bg_key
        bg_color = _current_bg_color
    if renpy.loadable("backgrounds/" + bg_key + ".webp"):
        add ("backgrounds/" + bg_key + ".webp") fit "cover"
    elif renpy.loadable("backgrounds/" + bg_key + ".jpg"):
        add ("backgrounds/" + bg_key + ".jpg") fit "cover"
    else:
        add Solid(bg_color)

    python:
        loc_info = LOCATIONS.get(loc_id, {"name": loc_id, "icon": "📍"})
        loc_name = loc_info["name"]
        loc_icon = loc_info["icon"]

    # Location name — top left
    frame:
        xpos       14
        ypos       50
        background "#07071088"
        padding    (12, 8)
        hbox:
            spacing 8
            text loc_icon size 20 yalign 0.5
            text loc_name color "#f472b6" bold True size 18 yalign 0.5
            text "[time_str()]" color "#60a5fa" size 14 yalign 0.5

    # Top-right: Outside button
    frame:
        xalign  1.0
        ypos    50
        xpos    -14
        background "#07071088"
        padding    (10, 7)
        textbutton "🌍 Outside":
            action Return(("goto_map", None))
            text_color       "#94a3b8"
            text_hover_color "#60a5fa"
            background       "#1e293b"
            hover_background "#334155"
            padding          (12, 7)

    # NPCs present — middle of screen
    if npcs_here:
        hbox:
            xalign  0.5
            ypos    180
            spacing 24
            for npc_id in npcs_here:
                python:
                    npc       = NPC_DATA.get(npc_id, {"name": npc_id})
                    npc_name  = npc["name"]
                    rel_val   = getattr(store, "rel_" + npc_id, 0)
                    rel_lbl   = rel_label(rel_val)
                    is_dating = store.dating.get(npc_id, False)

                frame:
                    xsize   130
                    ysize   200
                    background "#0f172a88"
                    hover_background "#f472b622"
                    padding (0, 0)
                    button:
                        action Return(("talk", npc_id))
                        xfill True
                        yfill True
                        vbox:
                            xalign 0.5
                            yalign 0.5
                            spacing 6
                            frame:
                                xalign    0.5
                                xsize     100
                                ysize     140
                                background "#0a0a1e"
                                vbox:
                                    xalign 0.5
                                    yalign 0.5
                                    text ("❤️" if is_dating else "👤") size 52 xalign 0.5
                                    text npc_name.split()[0] size 11 color "#f472b6" xalign 0.5
                            text npc_name.split()[0] size 13 bold True color "#f472b6" xalign 0.5
                            text rel_lbl size 11 color "#475569" xalign 0.5
    else:
        frame:
            xalign  0.5
            ypos    260
            background "#07071066"
            padding    (30, 16)
            text "Nobody here right now." color "#334155" italic True size 15 xalign 0.5

    # Bottom panel — actions + wait + outside + stats strip
    frame:
        xfill      True
        yalign     1.0
        background "#07071099"
        padding    (16, 12)
        vbox:
            spacing 8
            # Action buttons row
            hbox:
                spacing 8
                xfill True
                if loc_actions:
                    for action_id, action_label in loc_actions:
                        textbutton "[action_label]":
                            action Return(("action", action_id))
                            text_color       "#94a3b8"
                            text_hover_color "#e2e8f0"
                            background       "#1e293b"
                            hover_background "#334155"
                            padding          (10, 8)
                null xfill True
                textbutton "⏭️ Wait":
                    action Return(("wait", None))
                    text_color       "#94a3b8"
                    text_hover_color "#fbbf24"
                    background       "#1e293b55"
                    hover_background "#334155"
                    padding          (10, 8)
                textbutton "🌍 Outside":
                    action Return(("goto_map", None))
                    text_color       "#60a5fa"
                    text_hover_color "#e2e8f0"
                    background       "#1e293b"
                    hover_background "#334155"
                    padding          (10, 8)


## ── HOME ROOM SCREEN ─────────────────────────────────────────────
## Shown whenever the player is inside their home.
## Bottom bar shows all other rooms as navigation buttons.
## Current room is excluded from the bottom bar.
screen lc_home_room(current_room_id, npcs_here, room_actions):
    tag hub
    zorder 50

    # Background — rendered inside screen, never uses scene
    python:
        bg_key   = _current_bg_key
        bg_color = _current_bg_color
    if renpy.loadable("backgrounds/" + bg_key + ".webp"):
        add ("backgrounds/" + bg_key + ".webp") fit "cover"
    elif renpy.loadable("backgrounds/" + bg_key + ".jpg"):
        add ("backgrounds/" + bg_key + ".jpg") fit "cover"
    else:
        add Solid(bg_color)

    python:
        room_info = HOME_ROOMS.get(current_room_id, {"name": current_room_id, "icon": "🚪"})
        room_name = room_info["name"]
        room_icon = room_info["icon"]

    # Room name + time — top left
    frame:
        xpos       14
        ypos       50
        background "#07071088"
        padding    (12, 8)
        hbox:
            spacing 8
            text room_icon size 20 yalign 0.5
            text room_name color "#f472b6" bold True size 18 yalign 0.5
            text "[time_str()]" color "#60a5fa" size 14 yalign 0.5

    # Top-right: Outside button
    frame:
        xalign  1.0
        ypos    50
        xpos    -14
        background "#07071088"
        padding    (10, 7)
        textbutton "🌍 Outside":
            action Return(("goto_map", None))
            text_color       "#94a3b8"
            text_hover_color "#60a5fa"
            background       "#1e293b"
            hover_background "#334155"
            padding          (12, 7)

    # NPCs present in this room
    if npcs_here:
        hbox:
            xalign  0.5
            ypos    180
            spacing 24
            for npc_id in npcs_here:
                python:
                    npc       = NPC_DATA.get(npc_id, {"name": npc_id})
                    npc_name  = npc["name"]
                    rel_val   = getattr(store, "rel_" + npc_id, 0)
                    rel_lbl   = rel_label(rel_val)
                    is_dating = store.dating.get(npc_id, False)

                frame:
                    xsize   130
                    ysize   200
                    background "#0f172a88"
                    hover_background "#f472b622"
                    padding (0, 0)
                    button:
                        action Return(("talk", npc_id))
                        xfill True
                        yfill True
                        vbox:
                            xalign 0.5
                            yalign 0.5
                            spacing 6
                            frame:
                                xalign    0.5
                                xsize     100
                                ysize     140
                                background "#0a0a1e"
                                vbox:
                                    xalign 0.5
                                    yalign 0.5
                                    text ("❤️" if is_dating else "👤") size 52 xalign 0.5
                                    text npc_name.split()[0] size 11 color "#f472b6" xalign 0.5
                            text npc_name.split()[0] size 13 bold True color "#f472b6" xalign 0.5
                            text rel_lbl size 11 color "#475569" xalign 0.5

    # ── BOTTOM PANEL ─────────────────────────────────────────────
    frame:
        xfill      True
        yalign     1.0
        background "#07071099"
        padding    (14, 10)
        vbox:
            spacing 8

            # Action buttons for this room
            hbox:
                spacing 8
                xfill True
                if room_actions:
                    for action_id, action_label in room_actions:
                        textbutton "[action_label]":
                            action Return(("action", action_id))
                            text_color       "#94a3b8"
                            text_hover_color "#e2e8f0"
                            background       "#1e293b"
                            hover_background "#334155"
                            padding          (10, 8)
                null xfill True
                textbutton "⏭️ Wait":
                    action Return(("wait", None))
                    text_color       "#94a3b8"
                    text_hover_color "#fbbf24"
                    background       "#1e293b55"
                    hover_background "#334155"
                    padding          (10, 8)

            # Room navigation bar — other rooms + Outside button
            hbox:
                spacing 12
                xalign 0.5
                python:
                    other_rooms = [(rid, rinfo) for rid, rinfo in HOME_ROOMS.items() if rid != current_room_id]
                for room_id, rinfo in other_rooms:
                    python:
                        npc_there = []
                        for nid in NPC_SCHEDULE:
                            nloc, nroom, _unused = get_npc_location(nid)
                            if nloc == "home" and (nroom == room_id or nroom is None):
                                npc_there.append(nid)
                        has_npc   = len(npc_there) > 0
                        nav_idle  = "gui/locationhub/nav_" + room_id + ".webp"
                        nav_hover = "gui/locationhub/nav_" + room_id + "_hover.webp"
                        has_img   = renpy.loadable(nav_idle)
                        has_hover = renpy.loadable(nav_hover)

                    if has_img:
                        ## Custom image button
                        frame:
                            background None
                            padding (0, 0)
                            imagebutton:
                                idle  nav_idle
                                hover (nav_hover if has_hover else nav_idle)
                                action Return(("goto_room", room_id))
                                xsize 120
                                ysize 112
                    else:
                        ## Fallback circular styled button
                        button:
                            action Return(("goto_room", room_id))
                            xsize 120
                            ysize 112
                            background Solid("#1e293b")
                            hover_background Solid("#334155")
                            vbox:
                                xalign 0.5
                                yalign 0.5
                                text rinfo['icon']:
                                    size   26
                                    xalign 0.5
                                text rinfo['name']:
                                    size       11
                                    xalign     0.5
                                    text_align 0.5
                                    color      ("#f472b6" if has_npc else "#94a3b8")

                # Outside button — styled circular to match
                button:
                    action Return(("goto_map", None))
                    xsize 120
                    ysize 112
                    background Solid("#0f1e35")
                    hover_background Solid("#1e3a5f")
                    vbox:
                        xalign 0.5
                        yalign 0.5
                        text "🌍":
                            size   28
                            xalign 0.5
                        text "Outside":
                            size   11
                            xalign 0.5
                            color  "#60a5fa"

            # Stat strip removed — shown by global hud() screen
