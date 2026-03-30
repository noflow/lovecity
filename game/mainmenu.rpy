## mainmenu.rpy — LoveCity Main Menu
## ═══════════════════════════════════════════════════════════════

## ── TITLE SCREEN ─────────────────────────────────────────────────
screen lc_title_screen():
    tag menu
    zorder 0

    ## Background — use bedroom or solid fallback
    if renpy.loadable("backgrounds/bedroom.webp"):
        add "backgrounds/bedroom.webp" fit "cover"
    else:
        add Solid("#07071a")

    ## Dark overlay
    add Solid("#00000088")

    ## Subtle animated shimmer at top
    frame:
        background "#f472b608"
        xfill True
        ysize 3
        ypos 0

    ## Title block — centred
    vbox:
        xalign 0.5
        yalign 0.38
        spacing 6

        ## Logo / Title
        text "💖 LoveCity":
            xalign 0.5
            color  "#f472b6"
            size   72
            bold   True

        text "a story about the city and the people in it":
            xalign    0.5
            text_align 0.5
            color  "#475569"
            size   18
            italic True

    ## Menu buttons
    vbox:
        xalign 0.5
        yalign 0.65
        spacing 14

        ## New Game
        textbutton "✨  New Game":
            action Return("new")
            xalign 0.5
            xminimum 280
            background "#f472b618"
            hover_background "#f472b633"
            padding (24, 14)
            text_color       "#f472b6"
            text_hover_color "#ffffff"
            text_size        20
            text_bold        True

        ## Continue (only if save exists)
        if renpy.can_load_fast():
            textbutton "▶  Continue":
                action Return("continue")
                xalign 0.5
                xminimum 280
                background "#60a5fa18"
                hover_background "#60a5fa33"
                padding (24, 14)
                text_color       "#60a5fa"
                text_hover_color "#ffffff"
                text_size        20

        ## Load Game
        textbutton "📂  Load Game":
            action Return("load")
            xalign 0.5
            xminimum 280
            background "#1e293b"
            hover_background "#334155"
            padding (24, 14)
            text_color       "#94a3b8"
            text_hover_color "#e2e8f0"
            text_size        18

        ## Settings
        textbutton "⚙️  Settings":
            action Return("settings")
            xalign 0.5
            xminimum 280
            background "#1e293b"
            hover_background "#334155"
            padding (24, 14)
            text_color       "#94a3b8"
            text_hover_color "#e2e8f0"
            text_size        18

        ## Quit
        textbutton "🚪  Quit":
            action Return("quit")
            xalign 0.5
            xminimum 280
            background "#0f172a"
            hover_background "#1e293b"
            padding (24, 14)
            text_color       "#475569"
            text_hover_color "#ef4444"
            text_size        18

    ## Version + credit
    text "v0.1.0":
        xalign 1.0
        yalign 1.0
        xpos   -14
        ypos   -10
        color  "#1e293b"
        size   13


## ── ABOUT SCREEN ─────────────────────────────────────────────────
screen lc_about_screen():
    tag menu
    add Solid("#07071a")
    add Solid("#00000088")

    frame:
        background "#07071088"
        padding    (40, 36)
        xalign 0.5
        yalign 0.5
        xsize 640
        vbox:
            spacing 16
            text "About LoveCity":
                color "#f472b6"
                bold True
                size 28
                xalign 0.5
            null height 8
            text "A sandbox visual novel set in a modern city.\nExplore, connect, grow.":
                color "#94a3b8"
                size  18
                text_align 0.5
                xalign 0.5
            null height 16
            textbutton "← Back":
                action Return()
                xalign 0.5
                background "#1e293b"
                hover_background "#334155"
                padding (16, 10)
                text_color "#94a3b8"
                text_hover_color "#e2e8f0"
