## script.rpy — Entry point for LoveCity

label start:
    ## If intro already done (e.g. returned here by accident), go straight to sandbox
    if flag_intro_done:
        jump sandbox_room_loop
    jump lc_start
