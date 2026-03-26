## phone_setup.rpy — LoveCity phone integration
## ═══════════════════════════════════════════════════════════════
## Requires kleineluka's Ren'Py Phone System
## https://kleineluka.itch.io/phone (free)
##
## Install:
##   1. Drop phone.rpy into game/
##   2. Images already in game/gui/phone/    ✓
##   3. Audio already in game/audio/phone/   ✓
##   4. screens.rpy already has screen say   ✓
## ═══════════════════════════════════════════════════════════════

## ── PHONE INIT ───────────────────────────────────────────────────
## Call once at game start. Sets up all LoveCity contacts + channels.

label lc_phone_init:
    $ reset_phone_data()

    ## ── Contacts ────────────────────────────────────────────────
    ## add_phone_contact(id, name, colour, pfp_path_or_None)

    ## Family
    $ add_phone_contact("mom",       "Mom",        "#f472b6", None)
    $ add_phone_contact("sister",    "Cass",        "#a78bfa", None)

    ## Friends / school
    $ add_phone_contact("alex",      "Alex",        "#60a5fa", None)
    $ add_phone_contact("maya",      "Maya",        "#34d399", None)
    $ add_phone_contact("kai",       "Kai",         "#f97316", None)
    $ add_phone_contact("theo",      "Theo",        "#94a3b8", None)
    $ add_phone_contact("cora",      "Cora Finch",  "#fbbf24", None)

    ## Romance interests
    $ add_phone_contact("luna",      "Luna",        "#c084fc", None)
    $ add_phone_contact("zane",      "Zane",        "#ef4444", None)
    $ add_phone_contact("nadia",     "Nadia",       "#22d3ee", None)
    $ add_phone_contact("ronnie",    "Ronnie",      "#fb923c", None)

    ## Professional
    $ add_phone_contact("dr_rivera", "Dr. Rivera",  "#64748b", None)

    ## ── Channels (one per contact for now) ──────────────────────
    ## add_phone_channel(channel_id, display_name, contact_id)
    ## Channel IDs used later with add_phone_message()

    $ add_phone_channel("ch_mom",     "Mom",        "mom")
    $ add_phone_channel("ch_sister",  "Cass",       "sister")
    $ add_phone_channel("ch_alex",    "Alex",       "alex")
    $ add_phone_channel("ch_maya",    "Maya",       "maya")
    $ add_phone_channel("ch_kai",     "Kai",        "kai")
    $ add_phone_channel("ch_theo",    "Theo",       "theo")
    $ add_phone_channel("ch_cora",    "Cora",       "cora")
    $ add_phone_channel("ch_luna",    "Luna",       "luna")
    $ add_phone_channel("ch_zane",    "Zane",       "zane")
    $ add_phone_channel("ch_nadia",   "Nadia",      "nadia")
    $ add_phone_channel("ch_ronnie",  "Ronnie",     "ronnie")
    $ add_phone_channel("ch_rivera",  "Dr. Rivera", "dr_rivera")

    return


## ── SHOW / HIDE PHONE ───────────────────────────────────────────
## These are called by the 📱 button in the HUD.

label lc_phone_show:
    $ phone_start()
    show screen phone_ui
    return

label lc_phone_hide:
    hide screen phone_ui
    $ phone_end()
    return


## ── TEXT HELPER FUNCTIONS ────────────────────────────────────────
## Use these in story scripts to send messages to the player.

init python:
    def lc_text(channel_id, sender_id, message):
        """
        Send a text message.
        channel_id: e.g. "ch_mom"
        sender_id:  contact id, e.g. "mom", or "player" for the MC
        message:    string
        """
        add_phone_message(channel_id, sender_id, message)

    def lc_notify(channel_id):
        """Show notification badge on a channel."""
        set_phone_notification(channel_id, True)

    def lc_clear_notify(channel_id):
        """Clear notification badge."""
        set_phone_notification(channel_id, False)


## ── DAY 1 PHONE EVENTS ──────────────────────────────────────────
## Call these from the story after the relevant character meetings.

label phone_mom_day1:
    ## Mom texts after breakfast
    $ lc_text("ch_mom", "mom", "Don't forget to eat something at school.")
    $ lc_text("ch_mom", "mom", "Text me when you get there. ❤")
    $ lc_notify("ch_mom")
    return

label phone_sister_day1:
    ## Sister texts after orientation
    $ lc_text("ch_sister", "sister", "hey")
    $ lc_text("ch_sister", "sister", "you survive orientation?")
    $ lc_notify("ch_sister")
    return


## ── EXAMPLE: how to reply as player ────────────────────────────
##
##   $ lc_text("ch_mom", "player", "I'm here, don't worry.")
##   $ lc_text("ch_sister", "player", "barely")
##
## Example choice in story:
##
##   menu:
##       "Yeah, survived.":
##           $ lc_text("ch_sister", "player", "yeah, survived.")
##           $ lc_text("ch_sister", "sister", "told you.")
##       "It was rough.":
##           $ lc_text("ch_sister", "player", "it was rough tbh")
##           $ lc_text("ch_sister", "sister", "aw :( talk later?")
