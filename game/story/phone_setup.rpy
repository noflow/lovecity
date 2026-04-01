## phone_setup.rpy — LoveCity phone integration
## ═══════════════════════════════════════════════════════════════
## Uses kleineluka's Ren'Py Phone System (phone.rpy)
## https://kleineluka.itch.io/phone
##
## File locations (confirmed from phone.rpy source):
##   Images:  game/gui/phone/           (screen, header, base, bubbles etc.)
##   Audio:   game/audio/phone/         (send.mp3, receive.mp3)
##   Icons:   game/gui/phone/           (icon.png for default)
##
## Correct API (from phone.rpy source):
##   create_phone_channel(id, display_name, participants_list, icon_path)
##   send_phone_message(sender, text, channel_id, do_pause=False)
##   phone_start() / phone_end()
##   reset_phone_data()   ← contacts already set up inside phone.rpy itself
##
## All LoveCity contacts are configured in phone.rpy's reset_phone_data().
## ═══════════════════════════════════════════════════════════════

init python:
    def _phone_ok():
        """True if phone.rpy is installed and ready."""
        return hasattr(store, "reset_phone_data")

    def lc_text(channel_id, sender_name, message):
        """
        Send a text message in a channel.
        channel_id:   e.g. "ch_mom"
        sender_name:  display name matching channel participant, e.g. "Mom"
                      use phone_config["phone_player_name"] for the player ("Me")
        message:      string
        """
        if _phone_ok():
            send_phone_message(sender_name, message, channel_id, do_pause=False)

    def lc_text_player(channel_id, message):
        """Send a message as the player (MC)."""
        if _phone_ok():
            send_phone_message(phone_config["phone_player_name"], message, channel_id, do_pause=False)

    def lc_notify(channel_id):
        """Show notification badge. (send_phone_message sets this automatically)"""
        if _phone_ok() and channel_id in channel_notifs:
            channel_notifs[channel_id] = True
            renpy.restart_interaction()

    def lc_clear_notify(channel_id):
        """Clear notification badge."""
        if _phone_ok() and channel_id in channel_notifs:
            channel_notifs[channel_id] = False
            renpy.restart_interaction()

    def lc_show_phone():
        """Show the phone UI overlay from the HUD button."""
        if _phone_ok():
            phone_start()
            renpy.show_screen("phone_ui")
            renpy.restart_interaction()


## ── PHONE INIT ───────────────────────────────────────────────────
## Calls reset_phone_data() — contacts are set up inside phone.rpy.

label lc_phone_init:
    if _phone_ok():
        $ reset_phone_data()
        $ store._lc_phone_inited = True
    return


## ── SHOW / HIDE ──────────────────────────────────────────────────
label lc_phone_show:
    if _phone_ok():
        $ phone_start()
        show screen phone_ui
    return

label lc_phone_hide:
    if _phone_ok():
        hide screen phone_ui
        $ phone_end()
    return


## ── DAY 1 PHONE EVENTS ──────────────────────────────────────────
## Call these after the relevant story moments.

label phone_mom_day1:
    if _phone_ok():
        $ lc_text("ch_mom", "Mom", "Don't forget to eat something at school.")
        $ lc_text("ch_mom", "Mom", "Text me when you get there. ❤")
    return

label phone_sister_day1:
    if _phone_ok():
        $ lc_text("ch_sister", "Cass", "hey")
        $ lc_text("ch_sister", "Cass", "you survive orientation?")
    return


## ── USAGE EXAMPLES ───────────────────────────────────────────────
## Send a message from an NPC:
##   $ lc_text("ch_mom", "Mom", "Are you home yet?")
##
## Send as player:
##   $ lc_text_player("ch_mom", "Almost!")
##
## Send with in-game pause (waits for click):
##   $ send_phone_message("Mom", "Dinner's ready.", "ch_mom", do_pause=True)
##
## Photo message:
##   $ send_phone_message("Luna", "path/to/photo.png", "ch_luna", message_kind=2)
##
## Choice reply:
##   $ present_phone_choices([
##       ("Sure!", "Sure!", None),
##       ("Maybe later", "Maybe later...", None),
##   ], "ch_alex")
