## phone_setup.rpy — LoveCity phone integration
## ═══════════════════════════════════════════════════════════════
## Requires kleineluka's phone system (phone.rpy + gui assets)
## Download free from: https://kleineluka.itch.io/phone
## Drop phone.rpy into game/ and the gui assets into game/gui/
## ═══════════════════════════════════════════════════════════════

## ── PHONE INIT ───────────────────────────────────────────────────
## Call this once at game start to set up all LoveCity contacts

label lc_phone_init:
    ## Reset phone to blank state
    $ reset_phone_data()

    ## ── ADD CONTACTS ────────────────────────────────────────────
    ## Format: add_phone_contact(id, display_name, colour, pfp_image)
    ## pfp_image = path to portrait or None

    ## Family
    $ add_phone_contact("mom",    "Mom",           "#f472b6", None)
    $ add_phone_contact("sister", "Cass",          "#a78bfa", None)

    ## Friends / classmates
    $ add_phone_contact("alex",   "Alex",          "#60a5fa", None)
    $ add_phone_contact("maya",   "Maya",          "#34d399", None)
    $ add_phone_contact("kai",    "Kai",           "#f97316", None)
    $ add_phone_contact("theo",   "Theo",          "#94a3b8", None)
    $ add_phone_contact("cora",   "Cora Finch",    "#fbbf24", None)

    ## Romance
    $ add_phone_contact("luna",   "Luna",          "#c084fc", None)
    $ add_phone_contact("zane",   "Zane",          "#ef4444", None)
    $ add_phone_contact("nadia",  "Nadia",         "#22d3ee", None)

    ## Professional
    $ add_phone_contact("dr_rivera", "Dr. Rivera", "#64748b", None)

    ## ── CREATE INITIAL CHAT CHANNELS ────────────────────────────
    ## Format: add_phone_channel(channel_id, display_name, contact_id_or_list)

    $ add_phone_channel("mom_chat",    "Mom",        "mom")
    $ add_phone_channel("sister_chat", "Cass",       "sister")
    $ add_phone_channel("alex_chat",   "Alex",       "alex")
    $ add_phone_channel("maya_chat",   "Maya",       "maya")
    $ add_phone_channel("kai_chat",    "Kai",        "kai")
    $ add_phone_channel("theo_chat",   "Theo",       "theo")
    $ add_phone_channel("cora_chat",   "Cora",       "cora")
    $ add_phone_channel("luna_chat",   "Luna",       "luna")
    $ add_phone_channel("zane_chat",   "Zane",       "zane")
    $ add_phone_channel("rivera_chat", "Dr. Rivera", "dr_rivera")
    return


## ── SHOW / HIDE PHONE ───────────────────────────────────────────
## Called from the HUD phone button

label lc_phone_show:
    $ phone_start()
    show screen phone_ui
    return

label lc_phone_hide:
    hide screen phone_ui
    $ phone_end()
    return


## ── SEND MESSAGES ───────────────────────────────────────────────
## Helpers to send texts from story events.
## Usage:  $ lc_text("mom_chat", "mom", "Don't be late for dinner.")
##         $ lc_text("mom_chat", "player", "I won't.")

init python:
    def lc_text(channel_id, sender_id, message):
        """Send a single text message to a channel."""
        add_phone_message(channel_id, sender_id, message)

    def lc_text_player(channel_id, message):
        """Send a message as the player."""
        add_phone_message(channel_id, "player", message)

    def lc_notify(channel_id, sender_id, preview=None):
        """Show a notification badge for an incoming message."""
        set_phone_notification(channel_id, True)


## ── MOM INTRO TEXT ──────────────────────────────────────────────
## Triggered after meeting mom on day 1

label phone_event_mom_day1:
    ## Mom texts after the morning conversation
    $ lc_text("mom_chat", "mom", "Don't forget to eat something at school.")
    $ lc_text("mom_chat", "mom", "And text me when you get there.")
    $ lc_notify("mom_chat", "mom", "Don't forget to eat")
    return


## ── SISTER INTRO TEXT ───────────────────────────────────────────
label phone_event_sister_day1:
    $ lc_text("sister_chat", "sister", "hey")
    $ lc_text("sister_chat", "sister", "you survived orientation?")
    $ lc_notify("sister_chat", "sister", "hey")
    return
