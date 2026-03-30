## phone_setup.rpy — LoveCity phone integration
## ═══════════════════════════════════════════════════════════════
## Requires kleineluka's Ren'Py Phone System
## https://kleineluka.itch.io/phone
##
## SETUP: Contacts are configured inside phone.rpy in reset_phone_data()
## per the README. This file just handles show/hide and helper functions.
## ═══════════════════════════════════════════════════════════════

init python:
    def _phone_ok():
        """True if phone.rpy is installed."""
        return hasattr(store, "reset_phone_data")

    def lc_text(channel_id, sender_id, message):
        if _phone_ok():
            add_phone_message(channel_id, sender_id, message)

    def lc_notify(channel_id):
        if _phone_ok():
            set_phone_notification(channel_id, True)

    def lc_clear_notify(channel_id):
        if _phone_ok():
            set_phone_notification(channel_id, False)


## ── PHONE INIT ───────────────────────────────────────────────────
## Calls reset_phone_data() which is defined inside phone.rpy.
## Contacts/channels are configured there per the README.

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
label phone_mom_day1:
    if _phone_ok():
        $ lc_text("ch_mom", "mom", "Don't forget to eat something at school.")
        $ lc_text("ch_mom", "mom", "Text me when you get there. ❤")
        $ lc_notify("ch_mom")
    return

label phone_sister_day1:
    if _phone_ok():
        $ lc_text("ch_sister", "sister", "hey")
        $ lc_text("ch_sister", "sister", "you survive orientation?")
        $ lc_notify("ch_sister")
    return
