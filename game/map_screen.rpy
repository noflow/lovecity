## map_screen.rpy — Clickable city map (Summertime Saga style)
## ═══════════════════════════════════════════════════════════════

init python:
    MAP_LOCATIONS = [
        # id           label               icon   x     y
        ("home",       "Home",             "🏠",  130,  480),
        ("school",     "Highbrook\nAcademy","🎓", 300,  180),
        ("cafe",       "Moondrop\nCafé",   "☕",  440,  340),
        ("mall",       "Sakura\nMall",     "🛍️",  680,  200),
        ("park",       "Riverside\nPark",  "🌳",  560,  480),
        ("clinic",     "Luminos\nClinic",  "🏥",  850,  160),
        ("gym",        "Iron Peak\nGym",   "💪",  200,  310),
        ("office",     "City\nOffice",     "🏢",  780,  400),
        ("bar",        "Neon\nLounge",     "🍸",  950,  520),
        ("library",    "Grand\nLibrary",   "📚",  390,  500),
        ("salon",      "Glam\nStudio",     "✂️",  660,  560),
        ("street",     "City\nStreets",    "🏙️",  1050, 320),
    ]
    MAP_LOC_DICT = {loc[0]: loc for loc in MAP_LOCATIONS}

## ── MAP SCREEN ──────────────────────────────────────────────────
screen lc_map():
    tag map
    zorder 50

    # Background
    if renpy.loadable("maps/city_map.jpg"):
        add "maps/city_map.jpg"
    elif renpy.loadable("maps/city_map.png"):
        add "maps/city_map.png"
    else:
        add Solid("#0a0f1a")
        for gx in range(0, 1281, 120):
            add Solid("#1a2030") xpos gx ypos 0 xsize 2 ysize 720
        for gy in range(0, 721, 90):
            add Solid("#1a2030") xpos 0 ypos gy xsize 1280 ysize 2

    add Solid("#00000055")

    ## ── HUD bar (inlined — avoids use/subscreen scoping issues) ─────
    frame:
        background "#07071099"
        padding    (14, 8)
        xfill      True
        ypos       0
        hbox:
            spacing 18
            xfill True
            text "💖 LoveCity" color "#f472b6" bold True size 18 yalign 0.5
            null width 8
            text "[time_str()]"         color "#60a5fa" size 14 yalign 0.5
            text "Day [time_day]"       color "#475569" size 13 yalign 0.5
            null xfill True
            text "💰 $[stat_money]"     color "#34d399" size 14 yalign 0.5
            text "⚡ [stat_energy]%"    color "#fbbf24" size 14 yalign 0.5
            text "😊 [stat_happiness]%" color "#f472b6" size 14 yalign 0.5
            null width 8
            textbutton "≡":
                action Function(_show_screen, "lc_pause_menu")
                text_color       "#94a3b8"
                text_hover_color "#f472b6"
                background       "#1e293b"
                padding          (10, 6)

    # Location buttons
    for loc_id, label, icon, lx, ly in MAP_LOCATIONS:
        python:
            npcs_here  = npcs_at_location(loc_id)
            is_current = (current_location == loc_id)
            loc_info   = LOCATIONS.get(loc_id, {})
            is_open    = loc_info.get("always_open", False) or "hours" not in loc_info

        frame:
            xpos lx - 50
            ypos ly - 50
            xsize 100
            ysize 100
            background (Frame(Solid("#f472b622"), 12, 12) if is_current else Frame(Solid("#0f172a99"), 12, 12))
            padding (4, 4)

            button:
                action [SetVariable("current_location", loc_id), Return(("travel", None))]
                sensitive is_open
                xfill True
                yfill True

                vbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 2

                    hbox:
                        xalign 0.5
                        spacing 3
                        text icon size (32 if is_current else 28) xalign 0.5
                        if len(npcs_here) >= 1:
                            text "·" color "#f472b6" size 14 yalign 1.0
                        if len(npcs_here) >= 2:
                            text "·" color "#f472b6" size 14 yalign 1.0
                        if len(npcs_here) >= 3:
                            text "+" color "#f472b6" size 12 yalign 1.0

                    text label:
                        xalign     0.5
                        text_align 0.5
                        size       (13 if not is_current else 14)
                        color      ("#f472b6" if is_current else ("#e2e8f0" if is_open else "#475569"))
                        bold       is_current

                    if not is_open:
                        text "closed" size 10 color "#475569" xalign 0.5

        # NPC initials below button
        if len(npcs_here) > 0:
            hbox:
                xpos lx - 40
                ypos ly + 52
                spacing 3
                for npc_id in npcs_here[:4]:
                    python:
                        npc     = NPC_DATA.get(npc_id, {})
                        npc_col = "#f472b6"
                    frame:
                        background Solid(npc_col + "33")
                        padding (3, 2)
                        xsize 18
                        text npc.get("name", npc_id)[0] size 11 color npc_col xalign 0.5

    # Time period strip — bottom right
    frame:
        xalign  1.0
        yalign  1.0
        xpos    -12
        ypos    -12
        background "#07071099"
        padding    (14, 10)
        hbox:
            spacing 6
            for i, (p_name, p_icon) in enumerate(zip(
                ["Morning", "Afternoon", "Evening", "Night"],
                ["☀️",       "🌤️",        "🌇",       "🌙"])):
                frame:
                    background ("#f472b622" if time_period == i else "#1e293b44")
                    padding    (8, 6)
                    xsize      80
                    vbox:
                        xalign 0.5
                        text p_icon size 18 xalign 0.5
                        text p_name size 11 color ("#f472b6" if time_period == i else "#475569") xalign 0.5

    # Bottom-left toolbar
    frame:
        xalign  0.0
        yalign  1.0
        xpos    12
        ypos    -12
        background "#07071099"
        padding    (10, 8)
        hbox:
            spacing 8
            textbutton "⏭️ Wait":
                action Return(("wait", None))
                text_color       "#94a3b8"
                text_hover_color "#fbbf24"
                background       "#1e293b"
                hover_background "#334155"
                padding          (12, 8)
            textbutton "📊 Stats":
                action Function(_show_screen, "lc_stats_screen")
                text_color       "#94a3b8"
                text_hover_color "#60a5fa"
                background       "#1e293b"
                hover_background "#334155"
                padding          (12, 8)
            textbutton "📓 Diary":
                action Function(_show_screen, "lc_diary_screen")
                text_color       "#94a3b8"
                text_hover_color "#fbbf24"
                background       "#1e293b"
                hover_background "#334155"
                padding          (12, 8)
            textbutton "💕 Relations":
                action Function(_show_screen, "lc_rel_screen")
                text_color       "#94a3b8"
                text_hover_color "#f472b6"
                background       "#1e293b"
                hover_background "#334155"
                padding          (12, 8)


## ── PAUSE MENU ──────────────────────────────────────────────────
screen lc_pause_menu():
    modal True
    zorder 200
    add "#00000099"
    frame:
        background "#07071088"
        padding    (30, 24)
        xalign     0.5
        yalign     0.5
        xsize      280
        vbox:
            spacing 10
            text "LoveCity" color "#f472b6" bold True size 22 xalign 0.5
            null height 6
            textbutton "▶  Continue":
                action Function(_hide_screen, "lc_pause_menu")
                xalign 0.5
                text_color "#e2e8f0" text_hover_color "#f472b6"
                background "#1e293b" hover_background "#334155"
                padding (14, 9) xminimum 200
            textbutton "💾  Save":
                action [Function(_hide_screen, "lc_pause_menu"), Function(_show_menu, "save")]
                xalign 0.5
                text_color "#e2e8f0" text_hover_color "#34d399"
                background "#1e293b" hover_background "#334155"
                padding (14, 9) xminimum 200
            textbutton "📂  Load":
                action [Function(_hide_screen, "lc_pause_menu"), Function(_show_menu, "load")]
                xalign 0.5
                text_color "#e2e8f0" text_hover_color "#60a5fa"
                background "#1e293b" hover_background "#334155"
                padding (14, 9) xminimum 200
            textbutton "⚙️  Preferences":
                action [Function(_hide_screen, "lc_pause_menu"), Function(_show_menu, "preferences")]
                xalign 0.5
                text_color "#94a3b8" text_hover_color "#94a3b8"
                background "#1e293b" hover_background "#334155"
                padding (14, 9) xminimum 200
            null height 4
            textbutton "🚪  Main Menu":
                action Function(renpy.full_restart)
                xalign 0.5
                text_color "#475569" text_hover_color "#ef4444"
                background "#0f172a" hover_background "#1e293b"
                padding (14, 9) xminimum 200
