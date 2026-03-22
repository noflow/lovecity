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
            thumb ""
        text "[value]" style "lc_value" xminimum 38 text_align 1.0

## ── HUD OVERLAY ─────────────────────────────────────────────────
## Always-visible top strip showing key stats
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

            # Menu button
            textbutton "≡" action Function(renpy.show_screen, "lc_menu") style "lc_button_small"

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
        textbutton "📖 Continue"   action Return() style "lc_button" xalign 0.5
        textbutton "💾 Save Game"  action Function(renpy.show_screen, "save")  style "lc_button" xalign 0.5
        textbutton "📂 Load Game"  action Function(renpy.show_screen, "load")  style "lc_button" xalign 0.5
        textbutton "📊 Stats"      action Function(renpy.show_screen, "lc_stats_screen") style "lc_button" xalign 0.5
        textbutton "📓 Diary"      action Function(renpy.show_screen, "lc_diary_screen") style "lc_button" xalign 0.5
        textbutton "⚙️ Preferences" action Function(renpy.show_screen, "preferences") style "lc_button" xalign 0.5
        null height 8
        textbutton "🚪 Main Menu"  action Function(renpy.full_restart) style "lc_button_small" xalign 0.5

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
                textbutton "✕" action Function(renpy.hide_screen, "lc_stats_screen") style "lc_button_small"
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
                textbutton "✕" action Function(renpy.hide_screen, "lc_rel_screen") style "lc_button_small"
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
                                thumb ""
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
                textbutton "✕" action Function(renpy.hide_screen, "lc_diary_screen") style "lc_button_small"
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


