## screens.rpy — All UI screens for LoveCity sandbox
## ═══════════════════════════════════════════════════════════════

## ── STYLES ──────────────────────────────────────────────────────
style lc_button:
    background  "#1e293b"
    hover_background "#334155"
    padding     (14, 10)
    xminimum    160
    idle_color  "#e2e8f0"
    hover_color "#f472b6"

style lc_button_small:
    background  "#0f172a"
    hover_background "#1e293b"
    padding     (10, 7)
    idle_color  "#94a3b8"
    hover_color "#60a5fa"

style lc_label:
    color  "#94a3b8"
    size   16

style lc_value:
    color  "#e2e8f0"
    bold   True
    size   16

style lc_panel:
    background  "#0a0a1466"
    padding     (16, 14)
    xfill       True

style lc_header:
    color  "#f472b6"
    bold   True
    size   22

style stat_bar_bg:
    background "#1e293b"
    xfill True
    ysize 8

style stat_bar_fill:
    ysize 8

## ── STAT BAR HELPER ─────────────────────────────────────────────
screen stat_bar(label, value, max_val=100, color="#f472b6", icon=""):
    hbox:
        spacing 8
        xfill True
        text "[icon] [label]" style "lc_label" xminimum 140
        bar:
            value value
            range max_val
            xfill True
            ysize 8
            left_bar  Frame("#1e293b", 0, 0)
            right_bar Frame("#0f172a", 0, 0)
            thumb None
        text "[value]" style "lc_value" xminimum 38 text_align 1.0

## ── HUD OVERLAY ─────────────────────────────────────────────────
## Always-visible top strip showing key stats + phone + menu
screen hud():
    zorder 100
    frame:
        style_prefix "lc"
        background  "#07071099"
        padding     (12, 6)
        xfill       True
        ypos        0
        hbox:
            spacing 20
            xfill True

            # Time & day
            hbox:
                spacing 6
                text "[time_str()]" color "#60a5fa" size 15
                text "Day [time_day]" color "#475569" size 14
                if is_weekend():
                    text "Weekend 🎉" color "#fbbf24" size 14

            null xfill True

            # Quick stats
            hbox:
                spacing 16
                text "💰 $[stat_money]"   color "#34d399" size 14
                text "⚡ [stat_energy]%"  color "#fbbf24" size 14
                text "😊 [stat_happiness]%" color "#f472b6" size 14

            null width 12

            # Phone button — opens phone if installed
            if _phone_ok():
                textbutton "📱":
                    action [Function(lc_show_phone), NullAction()]
                    style "lc_button_small"
                    text_color       "#94a3b8"
                    text_hover_color "#34d399"

            # Menu button
            textbutton "≡":
                action [Function(lc_show_screen, "lc_menu"), NullAction()]
                style "lc_button_small"

## ── MAIN MENU / PAUSE ───────────────────────────────────────────
screen lc_menu():
    modal True
    zorder 200
    add "#00000099"
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 12
        text "LoveCity" style "lc_header" xalign 0.5
        null height 8
        textbutton "📖 Continue":
            action [Function(lc_hide_screen, "lc_menu"), NullAction()]
            style "lc_button" xalign 0.5
        textbutton "💾 Save Game":
            action [Function(lc_hide_screen, "lc_menu"), Function(lc_show_screen, "lc_save_screen"), NullAction()]
            style "lc_button" xalign 0.5
        textbutton "📂 Load Game":
            action [Function(lc_hide_screen, "lc_menu"), Function(lc_show_screen, "lc_load_screen"), NullAction()]
            style "lc_button" xalign 0.5
        textbutton "📊 Stats":
            action [Function(lc_hide_screen, "lc_menu"), Function(lc_show_screen, "lc_stats_screen"), NullAction()]
            style "lc_button" xalign 0.5
        textbutton "📓 Diary":
            action [Function(lc_hide_screen, "lc_menu"), Function(lc_show_screen, "lc_diary_screen"), NullAction()]
            style "lc_button" xalign 0.5
        textbutton "⚙️ Preferences":
            action [Function(lc_hide_screen, "lc_menu"), Function(lc_show_screen, "lc_preferences_screen"), NullAction()]
            style "lc_button" xalign 0.5
        null height 8
        textbutton "🚪 Main Menu":
            action Function(renpy.full_restart)
            style "lc_button_small" xalign 0.5

## ── STATS SCREEN ────────────────────────────────────────────────
screen lc_stats_screen():
    modal True
    zorder 150
    add "#00000099"
    frame:
        background "#07071088"
        padding    (24, 20)
        xalign  0.5
        yalign  0.5
        xsize   700
        vbox:
            spacing 12
            hbox:
                text "📊 Stats — [player_name]" style "lc_header"
                null xfill True
                textbutton "✕":
                    action Function(_hide_screen, "lc_stats_screen")
                    style "lc_button_small"
            null height 8

            # Core stats
            text "Core Attributes" color "#60a5fa" bold True size 15
            use stat_bar("Intelligence", stat_intelligence, 100, "#3b82f6", "🧠")
            use stat_bar("Charm",        stat_charm,        100, "#ec4899", "✨")
            use stat_bar("Fitness",      stat_fitness,      100, "#10b981", "💪")
            use stat_bar("Energy",       stat_energy,       100, "#fbbf24", "⚡")
            use stat_bar("Happiness",    stat_happiness,    100, "#f59e0b", "😊")
            null height 6

            # Progression
            text "Progression" color "#a78bfa" bold True size 15
            use stat_bar("Trust",       stat_trust,       100, "#c084fc", "🤝")
            use stat_bar("Confidence",  stat_confidence,  100, "#667eea", "🦋")
            use stat_bar("Acceptance",  stat_acceptance,  100, "#43e97b", "🌿")
            use stat_bar("Curiosity",   stat_curiosity,   100, "#f59e0b", "🔍")
            null height 6

            # Body
            text "Body" color "#f472b6" bold True size 15
            use stat_bar("Femininity",  body_femininity,  100, "#f472b6", "⚧")
            use stat_bar("Bust",        body_bust,        100, "#ec4899", "🌸")
            use stat_bar("Hips",        body_hips,        100, "#a78bfa", "〰")
            use stat_bar("Muscle",      body_muscle,      100, "#3b82f6", "💪")

## ── RELATIONSHIP SCREEN ─────────────────────────────────────────
screen lc_rel_screen():
    modal True
    zorder 150
    add "#00000099"
    frame:
        background "#07071088"
        padding    (24, 20)
        xalign  0.5
        yalign  0.5
        xsize   700
        ysize   560
        vbox:
            spacing 8
            hbox:
                text "💕 Relationships" style "lc_header"
                null xfill True
                textbutton "✕":
                    action Function(_hide_screen, "lc_rel_screen")
                    style "lc_button_small"
            null height 6
            viewport:
                scrollbars "vertical"
                mousewheel True
                ysize 480
                vbox:
                    spacing 6
                    python:
                        chars = list(NPC_DATA.items())
                    for npc_id, npc in chars:
                        python:
                            rel_val = getattr(store, "rel_" + npc_id, 0)
                            rel_lbl = rel_label(rel_val)
                            is_dating = store.dating.get(npc_id, False)
                        hbox:
                            spacing 10
                            xfill True
                            text "[npc['name']]" color "#e2e8f0" size 15 xminimum 180
                            text "[npc['job']]"  color "#475569" size 13 xminimum 160
                            bar:
                                value rel_val
                                range 200
                                xfill True
                                ysize 8
                                left_bar  Frame("#f472b688", 0, 0)
                                right_bar Frame("#1e293b", 0, 0)
                                thumb None
                            text "[rel_val]"  color "#f472b6" size 14 xminimum 36 text_align 1.0
                            if is_dating:
                                text "💕" size 16

## ── DIARY SCREEN ────────────────────────────────────────────────
screen lc_diary_screen():
    modal True
    zorder 150
    add "#00000099"
    frame:
        background "#07071088"
        padding    (24, 20)
        xalign  0.5
        yalign  0.5
        xsize   680
        ysize   520
        vbox:
            spacing 10
            hbox:
                text "📓 Diary" style "lc_header"
                null xfill True
                textbutton "✕":
                    action Function(_hide_screen, "lc_diary_screen")
                    style "lc_button_small"
            viewport:
                scrollbars "vertical"
                mousewheel True
                ysize 440
                vbox:
                    spacing 8
                    if len(diary) == 0:
                        text "Nothing written yet. Get out there." color "#475569" italic True
                    for entry in diary:
                        python:
                            period_names = ["Morning", "Afternoon", "Evening", "Night"]
                            p_name = period_names[entry.get("period", 0)]
                        frame:
                            background "#0f172a"
                            padding (12, 8)
                            xfill True
                            vbox:
                                spacing 3
                                text "Day [entry['day']] · [p_name]" color "#475569" size 13
                                text "[entry['text']]" color "#94a3b8" size 14


## ── SAVE SCREEN ─────────────────────────────────────────────────
screen lc_save_screen():
    modal True
    zorder 150
    add "#00000099"
    frame:
        background "#07071088"
        padding    (24, 20)
        xalign  0.5
        yalign  0.5
        xsize   740
        ysize   540
        vbox:
            spacing 10
            hbox:
                text "💾 Save Game" style "lc_header"
                null xfill True
                textbutton "✕":
                    action Function(_hide_screen, "lc_save_screen")
                    style "lc_button_small"

            # Page selector
            hbox:
                spacing 8
                xalign 0.5
                for pg in range(1, 7):
                    textbutton "[pg]":
                        action FilePage(pg)
                        style "lc_button_small"

            null height 6

            # Slot grid
            viewport:
                scrollbars "vertical"
                mousewheel True
                ysize 400
                vbox:
                    spacing 8
                    for slot_nr in range(1, 9):
                        python:
                            slot_name = str(slot_nr)
                            slot_time = FileTime(slot_name, empty="Empty slot")
                            slot_save_name = FileSaveName(slot_name, empty="")
                        button:
                            action FileSave(slot_name, confirm=True)
                            xfill True
                            background "#0f172a"
                            hover_background "#1e293b"
                            padding (14, 10)
                            hbox:
                                spacing 14
                                xfill True
                                text "Slot [slot_nr]" color "#60a5fa" size 16 bold True yalign 0.5 xminimum 80
                                vbox:
                                    spacing 2
                                    if slot_save_name:
                                        text "[slot_save_name]" color "#e2e8f0" size 15
                                    text "[slot_time]" color "#475569" size 13
                                null xfill True
                                if FileLoadable(slot_name):
                                    textbutton "🗑":
                                        action FileDelete(slot_name, confirm=True)
                                        style "lc_button_small"
                                        text_size 16
                                        yalign 0.5

## ── LOAD SCREEN ─────────────────────────────────────────────────
screen lc_load_screen():
    modal True
    zorder 150
    add "#00000099"
    frame:
        background "#07071088"
        padding    (24, 20)
        xalign  0.5
        yalign  0.5
        xsize   740
        ysize   540
        vbox:
            spacing 10
            hbox:
                text "📂 Load Game" style "lc_header"
                null xfill True
                textbutton "✕":
                    action Function(_hide_screen, "lc_load_screen")
                    style "lc_button_small"

            # Page selector
            hbox:
                spacing 8
                xalign 0.5
                for pg in range(1, 7):
                    textbutton "[pg]":
                        action FilePage(pg)
                        style "lc_button_small"

            null height 6

            # Slot grid
            viewport:
                scrollbars "vertical"
                mousewheel True
                ysize 400
                vbox:
                    spacing 8
                    for slot_nr in range(1, 9):
                        python:
                            slot_name = str(slot_nr)
                            slot_time = FileTime(slot_name, empty="Empty slot")
                            slot_save_name = FileSaveName(slot_name, empty="")
                        button:
                            action FileLoad(slot_name, confirm=True)
                            xfill True
                            background ("#0f172a" if FileLoadable(slot_name) else "#0a0a1a")
                            hover_background ("#1e293b" if FileLoadable(slot_name) else "#0a0a1a")
                            padding (14, 10)
                            sensitive FileLoadable(slot_name)
                            hbox:
                                spacing 14
                                xfill True
                                text "Slot [slot_nr]" color ("#60a5fa" if FileLoadable(slot_name) else "#334155") size 16 bold True yalign 0.5 xminimum 80
                                vbox:
                                    spacing 2
                                    if slot_save_name:
                                        text "[slot_save_name]" color "#e2e8f0" size 15
                                    text "[slot_time]" color "#475569" size 13
                                null xfill True
                                if FileLoadable(slot_name):
                                    textbutton "🗑":
                                        action FileDelete(slot_name, confirm=True)
                                        style "lc_button_small"
                                        text_size 16
                                        yalign 0.5

## ── LOAD SCREEN (main menu alias) ───────────────────────────────
## script.rpy calls "call screen load_screen" from the title
screen load_screen():
    use lc_load_screen

## ── PREFERENCES SCREEN ──────────────────────────────────────────
screen lc_preferences_screen():
    modal True
    zorder 150
    add "#00000099"
    frame:
        background "#07071088"
        padding    (24, 20)
        xalign  0.5
        yalign  0.5
        xsize   680
        ysize   540
        vbox:
            spacing 12
            hbox:
                text "⚙️ Preferences" style "lc_header"
                null xfill True
                textbutton "✕":
                    action Function(_hide_screen, "lc_preferences_screen")
                    style "lc_button_small"
            null height 6

            # Music volume
            hbox:
                spacing 10
                xfill True
                text "🎵 Music" color "#94a3b8" size 16 yalign 0.5 xminimum 160
                bar:
                    value Preference("music volume")
                    xfill True
                    ysize 12
                    left_bar  Frame("#f472b6", 0, 0)
                    right_bar Frame("#1e293b", 0, 0)
                    thumb None

            # Sound volume
            hbox:
                spacing 10
                xfill True
                text "🔊 Sound" color "#94a3b8" size 16 yalign 0.5 xminimum 160
                bar:
                    value Preference("sound volume")
                    xfill True
                    ysize 12
                    left_bar  Frame("#60a5fa", 0, 0)
                    right_bar Frame("#1e293b", 0, 0)
                    thumb None

            null height 8

            # Text speed
            hbox:
                spacing 10
                xfill True
                text "⌨️ Text Speed" color "#94a3b8" size 16 yalign 0.5 xminimum 160
                bar:
                    value Preference("text speed")
                    xfill True
                    ysize 12
                    left_bar  Frame("#34d399", 0, 0)
                    right_bar Frame("#1e293b", 0, 0)
                    thumb None

            # Auto-forward time
            hbox:
                spacing 10
                xfill True
                text "⏩ Auto Speed" color "#94a3b8" size 16 yalign 0.5 xminimum 160
                bar:
                    value Preference("auto-forward time")
                    xfill True
                    ysize 12
                    left_bar  Frame("#fbbf24", 0, 0)
                    right_bar Frame("#1e293b", 0, 0)
                    thumb None

            null height 10

            # Display mode
            hbox:
                spacing 14
                xalign 0.5
                text "Display:" color "#94a3b8" size 16 yalign 0.5
                textbutton "Window":
                    action Preference("display", "window")
                    style "lc_button_small"
                    text_color ("#f472b6" if not preferences.fullscreen else "#94a3b8")
                textbutton "Fullscreen":
                    action Preference("display", "fullscreen")
                    style "lc_button_small"
                    text_color ("#f472b6" if preferences.fullscreen else "#94a3b8")

            null height 6

            # Skip
            hbox:
                spacing 14
                xalign 0.5
                text "Skip:" color "#94a3b8" size 16 yalign 0.5
                textbutton "Unseen Text":
                    action Preference("skip", "toggle")
                    style "lc_button_small"
                textbutton "After Choices":
                    action Preference("after choices", "toggle")
                    style "lc_button_small"

## ── PREFERENCES SCREEN (main menu alias) ────────────────────────
## script.rpy calls "call screen preferences" from the title
screen preferences():
    use lc_preferences_screen


## ── CONFIRM SCREEN ──────────────────────────────────────────────
## Required by FileSave/FileDelete confirm=True
screen confirm(message, yes_action, no_action):
    modal True
    zorder 300
    add "#000000CC"
    frame:
        background "#0f172a"
        padding    (30, 24)
        xalign  0.5
        yalign  0.5
        xsize   460
        vbox:
            spacing 16
            text "[message]":
                color "#e2e8f0"
                size 18
                xalign 0.5
                text_align 0.5
            null height 6
            hbox:
                spacing 16
                xalign 0.5
                textbutton "Yes":
                    action yes_action
                    style "lc_button"
                    xminimum 120
                    text_color "#34d399"
                    text_hover_color "#ffffff"
                textbutton "No":
                    action no_action
                    style "lc_button"
                    xminimum 120
                    text_color "#f43f5e"
                    text_hover_color "#ffffff"


## ── SAY SCREEN STYLES ───────────────────────────────────────────
## Position the character name and dialogue text correctly

style say_window:
    xalign 0.5
    xsize 468
    yalign gui.textbox_yalign
    ysize gui.textbox_height

style say_who:
    xpos gui.name_xpos
    xanchor 0.0
    ypos gui.name_ypos
    yanchor 0.0
    color "#1e293b"
    bold True
    size gui.name_text_size

style say_dialogue:
    xpos gui.text_xpos
    xanchor 0.0
    ypos gui.text_ypos
    yanchor 0.0
    xsize gui.text_width
    color "#e2e8f0"
    size gui.text_size

## ── PHONE SYSTEM — screen say override ──────────────────────────
## Based on kleineluka README pattern. Hides textbox when phone open.

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        background (None if (_phone_ok() and phone_mode) else Transform("gui/locationhub/textbox_blue.png", size=(468, 111)))
        xalign 0.5
        xsize 468
        yalign gui.textbox_yalign
        ysize gui.textbox_height
        xpadding 0
        ypadding 0

        if who is not None:
            text who id "who"

        text what id "what"

    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0
