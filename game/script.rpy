## script.rpy — Entry point for LoveCity

label start:
    ## Loaded save — go straight to sandbox
    if flag_intro_done:
        show screen hud
        jump sandbox_room_driver
    ## Fresh start — show main menu
    jump lc_main_menu_loop

## ── MAIN MENU LOOP ───────────────────────────────────────────────
label lc_main_menu_loop:
    call screen lc_title_screen
    if _return == "new":
        jump lc_start
    elif _return == "continue":
        $ renpy.load(renpy.newest_slot())
    elif _return == "load":
        call screen load_screen
        jump lc_main_menu_loop
    elif _return == "settings":
        call screen preferences
        jump lc_main_menu_loop
    elif _return == "quit":
        $ renpy.quit()
    jump lc_main_menu_loop
