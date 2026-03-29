## phone_setup.rpy — LoveCity phone integration
## Requires kleineluka's Ren'Py Phone System
## https://kleineluka.itch.io/phone  (free — drop phone.rpy into game/)

init python:
    def lc_text(channel_id, sender_id, message):
        if "add_phone_message" in dir(store):
            add_phone_message(channel_id, sender_id, message)

    def lc_notify(channel_id):
        if "set_phone_notification" in dir(store):
            set_phone_notification(channel_id, True)

    def lc_clear_notify(channel_id):
        if "set_phone_notification" in dir(store):
            set_phone_notification(channel_id, False)

    def _phone_ok():
        """True if phone.rpy is installed and ready."""
        return "reset_phone_data" in dir(store)


## ── PHONE INIT ───────────────────────────────────────────────────
label lc_phone_init:
    if not _phone_ok():
        return  ## phone.rpy not installed yet — skip safely

    python:
        reset_phone_data()

        ## Contacts — (id, display_name, colour, portrait_or_None)
        for _c in [
            ("mom",       "Mom",        "#f472b6"),
            ("sister",    "Cass",       "#a78bfa"),
            ("alex",      "Alex",       "#60a5fa"),
            ("maya",      "Maya",       "#34d399"),
            ("kai",       "Kai",        "#f97316"),
            ("theo",      "Theo",       "#94a3b8"),
            ("cora",      "Cora Finch", "#fbbf24"),
            ("luna",      "Luna",       "#c084fc"),
            ("zane",      "Zane",       "#ef4444"),
            ("nadia",     "Nadia",      "#22d3ee"),
            ("ronnie",    "Ronnie",     "#fb923c"),
            ("dr_rivera", "Dr. Rivera", "#64748b"),
        ]:
            add_phone_contact(_c[0], _c[1], _c[2], None)

        ## Channels — (channel_id, display_name, contact_id)
        for _ch in [
            ("ch_mom",    "Mom",        "mom"),
            ("ch_sister", "Cass",       "sister"),
            ("ch_alex",   "Alex",       "alex"),
            ("ch_maya",   "Maya",       "maya"),
            ("ch_kai",    "Kai",        "kai"),
            ("ch_theo",   "Theo",       "theo"),
            ("ch_cora",   "Cora",       "cora"),
            ("ch_luna",   "Luna",       "luna"),
            ("ch_zane",   "Zane",       "zane"),
            ("ch_nadia",  "Nadia",      "nadia"),
            ("ch_ronnie", "Ronnie",     "ronnie"),
            ("ch_rivera", "Dr. Rivera", "dr_rivera"),
        ]:
            add_phone_channel(_ch[0], _ch[1], _ch[2])
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
