## script.rpy — Entry point

label start:
    if flag_intro_done:
        jump sandbox_room_driver
    jump lc_start
