## mainmenu.rpy — LoveCity Main Menu
## ═══════════════════════════════════════════════════════════════

## ── TITLE SCREEN ─────────────────────────────────────────────────
screen lc_title_screen():
    tag menu
    zorder 0

    ## Background
    if renpy.loadable("backgrounds/bedroom.webp"):
        add "backgrounds/bedroom.webp" fit "cover"
    else:
        add Solid("#07071a")

    ## Gradient overlay — dark on left where menu sits, lighter on right
    add "#000000CC"

    ## Left panel — menu area
    frame:
        background "#07071aCC"
        xpos 0
        ypos 0
        xsize 420
        ysize 720
        padding (0, 0)

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 0

            ## ── TITLE ──────────────────────────────────────────
            null height 20
            text "💖":
                xalign 0.5
                size   52

            null height 8

            text "LoveCity":
                xalign 0.5
                color  "#f472b6"
                size   52
                bold   True

            null height 6

            text "a story about the city":
                xalign    0.5
                text_align 0.5
                color  "#64748b"
                size   15
                italic True

            text "and the people in it":
                xalign    0.5
                text_align 0.5
                color  "#64748b"
                size   15
                italic True

            ## ── DIVIDER ────────────────────────────────────────
            null height 40

            frame:
                background "#f472b622"
                xsize 180
                ysize 1
                xalign 0.5

            null height 40

            ## ── BUTTONS ────────────────────────────────────────
            ## New Game
            button:
                action Return("new")
                xalign 0.5
                xsize  300
                ysize  56
                background "#f472b620"
                hover_background "#f472b640"
                hbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 14
                    text "✨":
                        yalign 0.5
                        size   20
                    text "New Game":
                        yalign 0.5
                        color  "#f472b6"
                        hover_color "#ffffff"
                        size   20
                        bold   True

            null height 10

            ## Continue (only if save exists)
            if renpy.newest_slot() is not None:
                button:
                    action Return("continue")
                    xalign 0.5
                    xsize  300
                    ysize  52
                    background "#60a5fa15"
                    hover_background "#60a5fa30"
                    hbox:
                        xalign 0.5
                        yalign 0.5
                        spacing 14
                        text "▶":
                            yalign 0.5
                            size   18
                            color "#60a5fa"
                        text "Continue":
                            yalign 0.5
                            color  "#60a5fa"
                            hover_color "#ffffff"
                            size   18
                null height 10

            ## Load Game
            button:
                action Return("load")
                xalign 0.5
                xsize  300
                ysize  48
                background "#1e293b"
                hover_background "#334155"
                hbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 14
                    text "📂":
                        yalign 0.5
                        size   16
                    text "Load Game":
                        yalign 0.5
                        color  "#94a3b8"
                        hover_color "#e2e8f0"
                        size   16

            null height 6

            ## Settings
            button:
                action Return("settings")
                xalign 0.5
                xsize  300
                ysize  48
                background "#1e293b"
                hover_background "#334155"
                hbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 14
                    text "⚙️":
                        yalign 0.5
                        size   16
                    text "Settings":
                        yalign 0.5
                        color  "#94a3b8"
                        hover_color "#e2e8f0"
                        size   16

            null height 6

            ## Quit
            button:
                action Return("quit")
                xalign 0.5
                xsize  300
                ysize  48
                background "#0f172a"
                hover_background "#1e293b"
                hbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 14
                    text "🚪":
                        yalign 0.5
                        size   16
                    text "Quit":
                        yalign 0.5
                        color  "#475569"
                        hover_color "#ef4444"
                        size   16

            null height 48

    ## Thin pink accent line on left edge
    frame:
        background "#f472b6"
        xpos 0
        ypos 0
        xsize 3
        ysize 720

    ## Version bottom-left
    text "v0.1.0  ·  Ren'Py 8":
        xpos 14
        ypos -10
        yalign 1.0
        color  "#1e293b"
        size   12

    ## Credit to kleineluka bottom-right
    text "Phone system by KleineLuka":
        xalign 1.0
        yalign 1.0
        xpos   -14
        ypos   -10
        color  "#1e293b"
        size   12
