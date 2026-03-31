## phone_setup.rpy — LoveCity phone integration
## ═══════════════════════════════════════════════════════════════
## Requires kleineluka's Ren'Py Phone System
## https://kleineluka.itch.io/phone  (free)
##
## FILE LOCATIONS (confirmed from phone.rpy config):
##   game/phone.rpy                    ← phone engine
##   game/gui/phone/                   ← phone UI images (screen, header, etc.)
##   game/gui/phone/skins/dark_mode/   ← dark mode images
##   game/gui/phone/skins/flip_phone/  ← flip phone images
##   game/gui/phone/skins/status_bar/  ← status bar images
##   game/audio/phone/                 ← send/receive sounds
##   game/phone/icon.png               ← default contact icon
##                                        NOTE: no gui/ prefix — game/phone/
##
## ADDING CONTACTS: Edit reset_phone_data() inside phone.rpy
## See game/lovecity_phone_contacts.txt for the contacts to add
## ═══════════════════════════════════════════════════════════════

init python:
    def _phone_ok():
        """True if phone.rpy is installed and ready."""
        return hasattr(store, "reset_phone_data")

    def lc_text(channel_id, sender_id, message):
        """Send a text message. No-op if phone not installed."""
        if _phone_ok() and hasattr(store, "add_phone_message"):
            add_phone_message(channel_id, sender_id, message)

    def lc_notify(channel_id):
        """Show notification badge. No-op if phone not installed."""
        if _phone_ok() and hasattr(store, "set_phone_notification"):
            set_phone_notification(channel_id, True)

    def lc_clear_notify(channel_id):
        """Clear notification badge. No-op if phone not installed."""
        if _phone_ok() and hasattr(store, "set_phone_notification"):
            set_phone_notification(channel_id, False)


## ── PHONE INIT ───────────────────────────────────────────────────
## Calls reset_phone_data() inside phone.rpy which sets up contacts.
## Contacts/channels must be configured in phone.rpy itself.

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


## ── DAY 1 EVENTS ─────────────────────────────────────────────────
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
