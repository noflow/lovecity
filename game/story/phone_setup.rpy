## phone_setup.rpy — LoveCity phone integration
## ═══════════════════════════════════════════════════════════════
## Requires kleineluka's Ren'Py Phone System
## https://kleineluka.itch.io/phone (free)
##
## Install:
##   1. Drop phone.rpy into game/
##   2. Images in game/gui/phone/    ✓
##   3. Audio in game/audio/phone/   ✓
##   4. screens.rpy has screen say   ✓
##
## IMPORTANT: All functions below are NO-OPS until phone.rpy
## is installed. The game runs fine without it.
## ═══════════════════════════════════════════════════════════════

## ── PHONE AVAILABLE FLAG ─────────────────────────────────────────
## Detect whether phone.rpy is installed by checking for phone_mode
init python:
    try:
        _phone_mode_test = phone_mode  # defined in phone.rpy
        _lc_phone_available = True
    except NameError:
        _lc_phone_available = False

    ## ── Safe wrapper functions ───────────────────────────────────
    ## These silently no-op if phone.rpy isn't installed yet.

    def lc_text(channel_id, sender_id, message):
        """Send a text. No-op if phone not installed."""
        if not _lc_phone_available:
            return
        add_phone_message(channel_id, sender_id, message)

    def lc_notify(channel_id):
        """Show notification badge. No-op if phone not installed."""
        if not _lc_phone_available:
            return
        set_phone_notification(channel_id, True)

    def lc_clear_notify(channel_id):
        """Clear notification. No-op if phone not installed."""
        if not _lc_phone_available:
            return
        set_phone_notification(channel_id, False)


## ── PHONE INIT ───────────────────────────────────────────────────
## Called from intro.rpy. No-ops if phone.rpy not installed.

label lc_phone_init:
    python:
        if not _lc_phone_available:
            pass  # phone.rpy not installed yet — skip safely
        else:
            reset_phone_data()

            ## Contacts — add_phone_contact(id, name, colour, pfp_or_None)
            add_phone_contact("mom",       "Mom",        "#f472b6", None)
            add_phone_contact("sister",    "Cass",       "#a78bfa", None)
            add_phone_contact("alex",      "Alex",       "#60a5fa", None)
            add_phone_contact("maya",      "Maya",       "#34d399", None)
            add_phone_contact("kai",       "Kai",        "#f97316", None)
            add_phone_contact("theo",      "Theo",       "#94a3b8", None)
            add_phone_contact("cora",      "Cora Finch", "#fbbf24", None)
            add_phone_contact("luna",      "Luna",       "#c084fc", None)
            add_phone_contact("zane",      "Zane",       "#ef4444", None)
            add_phone_contact("nadia",     "Nadia",      "#22d3ee", None)
            add_phone_contact("ronnie",    "Ronnie",     "#fb923c", None)
            add_phone_contact("dr_rivera", "Dr. Rivera", "#64748b", None)

            ## Channels — add_phone_channel(channel_id, name, contact_id)
            add_phone_channel("ch_mom",    "Mom",        "mom")
            add_phone_channel("ch_sister", "Cass",       "sister")
            add_phone_channel("ch_alex",   "Alex",       "alex")
            add_phone_channel("ch_maya",   "Maya",       "maya")
            add_phone_channel("ch_kai",    "Kai",        "kai")
            add_phone_channel("ch_theo",   "Theo",       "theo")
            add_phone_channel("ch_cora",   "Cora",       "cora")
            add_phone_channel("ch_luna",   "Luna",       "luna")
            add_phone_channel("ch_zane",   "Zane",       "zane")
            add_phone_channel("ch_nadia",  "Nadia",      "nadia")
            add_phone_channel("ch_ronnie", "Ronnie",     "ronnie")
            add_phone_channel("ch_rivera", "Dr. Rivera", "dr_rivera")
    return


## ── SHOW / HIDE PHONE ───────────────────────────────────────────

label lc_phone_show:
    if _lc_phone_available:
        $ phone_start()
        show screen phone_ui
    return

label lc_phone_hide:
    if _lc_phone_available:
        hide screen phone_ui
        $ phone_end()
    return


## ── DAY 1 PHONE EVENTS ──────────────────────────────────────────

label phone_mom_day1:
    if _lc_phone_available:
        $ lc_text("ch_mom", "mom", "Don't forget to eat something at school.")
        $ lc_text("ch_mom", "mom", "Text me when you get there. ❤")
        $ lc_notify("ch_mom")
    return

label phone_sister_day1:
    if _lc_phone_available:
        $ lc_text("ch_sister", "sister", "hey")
        $ lc_text("ch_sister", "sister", "you survive orientation?")
        $ lc_notify("ch_sister")
    return
