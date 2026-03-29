## story/intro.rpy — Opening day of LoveCity
## ═══════════════════════════════════════════════════════════════

label lc_start:
    # Name entry
    $ player_name = renpy.input("What's your name?", default="Player", length=20).strip() or "Player"

    scene bg_bedroom with fade
    play music "audio/morning_theme.ogg" fadein 2.0
    stop music fadeout 3.0

    # Wake up
    narrator "8:47 AM. Monday."
    narrator "The ceiling. Same ceiling. Different year."
    thought "First day at Highbrook Academy."
    narrator "The light through the window is the particular shade of {i}not-quite-ready{/i}."
    thought "You lie there another thirty seconds. Then you get up."

    $ flag_intro_done = True

    ## ── Meet Mom (inlined — no call/return) ──
    show mom at left with dissolve

    menu:
        "Morning. What's for breakfast?":
            mom "Eggs and coffee. Sit down."
            mc "Thanks."
            mom "You have orientation today. Don't be late."
            mc "I know."
            $ add_rel("mom", 5)

        "I'm already running late.":
            mom "You're not. Sit down. Eat something."
            mc "I'm fine."
            mom "Sit. Down."
            mc "..."
            $ add_rel("mom", 2)
            $ add_stat("happiness", -3)

        "I don't think I'm ready for this.":
            mom "Nobody's ever ready."
            narrator "She says it plainly. Not unkind."
            mom "But you're going anyway. That's the part that matters."
            mc "Right."
            $ add_rel("mom", 8)
            $ add_stat("trust", 5)

    mom "The school is good. The people are..."
    narrator "She pauses."
    mom "...People. You'll figure it out."

    $ flag_met_mom = True
    hide mom with dissolve

    ## ── Meet Sister if home (inlined) ──
    python:
        _sis_loc, _sis_room, _sis_act = get_npc_location("sister", period=0, weekday=1)

    if _sis_loc == "home" and not flag_met_sister:
        show sister at right with dissolve

        sister "Finally. I thought you died."
        mc "Good morning to you too."
        sister "You look nervous."

        menu:
            "I'm not nervous.":
                sister "You are. Your left eye is doing that thing."
                mc "What thing?"
                sister "The thing."
                $ add_rel("sister", 3)

            "A little, maybe.":
                sister "Don't be. They're just people."
                narrator "She says it the same way your mom says things. Practical. Final."
                mc "Easy for you to say."
                sister "Yes. It is."
                $ add_rel("sister", 6)
                $ add_stat("confidence", 3)

            "I'm fine. Mind your business.":
                sister "Rude."
                mc "..."
                sister "Good luck anyway, jerk."
                $ add_rel("sister", 1)

        $ flag_met_sister = True
        hide sister with dissolve

    ## ── Head out ──
    narrator "You go back to your room. Get dressed. Pack your bag."
    narrator "The day is out there."
    narrator "This is where it starts."

    $ current_location = "home"
    $ current_room     = "bedroom"
    $ time_day         = 1
    $ time_period      = 0

    ## Initialise phone contacts (no-op if phone.rpy not installed yet)
    call lc_phone_init

    ## Jump cleanly into sandbox — zero pending call frames on the stack
    jump sandbox_room_driver


## ── MEET MOM ────────────────────────────────────────────────────
label meet_mom_intro:
    show mom at left with dissolve

    mom "You're actually up."
    narrator "She doesn't look surprised. She just sounds it."

    menu:
        "Morning. What's for breakfast?":
            mom "Eggs and coffee. Sit down."
            mc "Thanks."
            mom "You have orientation today. Don't be late."
            mc "I know."
            $ add_rel("mom", 5)

        "I'm already running late.":
            mom "You're not. Sit down. Eat something."
            mc "I'm fine."
            mom "Sit. Down."
            mc "..."
            $ add_rel("mom", 2)
            $ add_stat("happiness", -3)

        "I don't think I'm ready for this.":
            mom "Nobody's ever ready."
            narrator "She says it plainly. Not unkind."
            mom "But you're going anyway. That's the part that matters."
            mc "Right."
            $ add_rel("mom", 8)
            $ add_stat("trust", 5)

    mom "The school is good. The people are..." 
    narrator "She pauses."
    mom "...People. You'll figure it out."

    $ flag_met_mom = True
    hide mom with dissolve
    return


## ── CHECK INTRO EVENTS ─────────────────────────────────────────
label check_intro_events:
    # Meet sister if she's home
    python:
        sis_loc, sis_room, sis_act = get_npc_location("sister", period=0, weekday=1)
    if sis_loc == "home" and not flag_met_sister:
        call meet_sister_intro
    return


## ── MEET SISTER ─────────────────────────────────────────────────
label meet_sister_intro:
    ## scene removed — background handled by sandbox set_background
    show sister at right with dissolve

    sister "Finally. I thought you died."
    mc "Good morning to you too."
    sister "You look nervous."

    menu:
        "I'm not nervous.":
            sister "You are. Your left eye is doing that thing."
            mc "What thing?"
            sister "The thing."
            $ add_rel("sister", 3)

        "A little, maybe.":
            sister "Don't be. They're just people."
            narrator "She says it the same way your mom says things. Practical. Final."
            mc "Easy for you to say."
            sister "Yes. It is."
            $ add_rel("sister", 6)
            $ add_stat("confidence", 3)

        "I'm fine. Mind your business.":
            sister "Rude."
            mc "..."
            sister "Good luck anyway, jerk."
            $ add_rel("sister", 1)

    $ flag_met_sister = True
    hide sister with dissolve
    return


## ── MEET CORA (neighbour, triggered when leaving home) ──────────
label meet_cora:
    ## scene removed — background handled by sandbox set_background
    show cora at center with dissolve

    narrator "The woman from next door is at her letterbox. She looks up."
    cora "Oh! You must be Sarah's {i}[player_name]{/i}."
    narrator "She says it like a question she already knows the answer to."

    menu:
        "That's me. Hi.":
            cora "Cora. Finch. From next door."
            narrator "She gestures, unnecessarily, at the house."
            cora "I run the flower stall at the mall. Drop by sometime — I'll give you the neighbour rate."
            $ add_rel("cora", 10)

        "How do you know my name?":
            cora "Your mother talks about you. Constantly."
            mc "...Right."
            cora "Don't be embarrassed. It's sweet."
            $ add_rel("cora", 6)

    $ flag_met_cora = True
    hide cora with dissolve
    return




## ── TALK STUBS ──────────────────────────────────────────────────
## These are called when player chooses to talk to an NPC at a location.
## As scenes are written, replace the stub with actual dialogue.

label talk_mom:
    if not flag_met_mom:
        call meet_mom_intro
        return
    # Regular interaction
    show mom at center with dissolve
    menu:
        "How was your day?":
            mom "Long. Good. Normal."
            $ add_rel("mom", 2)
            $ add_stat("happiness", 3)
        "Need anything?":
            mom "No. You're sweet for asking."
            $ add_rel("mom", 3)
        "Just passing through.":
            mom "Then pass through quietly."
    hide mom with dissolve
    return

label talk_sister:
    if not flag_met_sister:
        call meet_sister_intro
        return
    show sister at center with dissolve
    menu:
        "How was school?":
            sister "Fine. You missed the drama in the hallway."
            mc "What drama?"
            sister "Exactly. You missed it."
            $ add_rel("sister", 2)
        "Can I borrow something?":
            sister "Depends what."
            mc "Advice."
            sister "Oh. That I have plenty of."
            $ add_rel("sister", 4)
            $ add_stat("charm", 2)
        "Nothing. Just saying hi.":
            sister "Hi."
            $ add_rel("sister", 1)
    hide sister with dissolve
    return

label talk_alex:
    if not flag_met_alex:
        call meet_alex_first
        return
    call meet_alex_regular
    return

label talk_maya:
    if not flag_met_maya:
        call meet_maya_first
        return
    call meet_maya_regular
    return

label talk_kai:
    if not flag_met_kai:
        call meet_kai_first
        return
    # Regular gym interaction
    show kai at center with dissolve
    kai "Working hard or hardly working?"
    mc "Working hard."
    kai "I can tell. Keep it up."
    $ add_rel("kai", 2)
    hide kai with dissolve
    return

label talk_luna:
    if not flag_met_luna:
        call meet_luna_first
        return
    show luna at center with dissolve
    luna "You're here late."
    mc "You too."
    luna "I'm always here late. That's rather the point."
    $ add_rel("luna", 2)
    hide luna with dissolve
    return

label talk_dr_rivera:
    if not flag_met_dr_rivera:
        call meet_dr_rivera
        return
    call therapy_session_regular
    return

label talk_cora:
    if not flag_met_cora:
        call meet_cora
        return
    show cora at center with dissolve
    cora "Back again! You need flowers or just company?"
    menu:
        "Just passing.":
            cora "There's no such thing. Sit for a minute."
            $ add_rel("cora", 2)
        "What do you recommend today?":
            cora "Depends what it's for."
            $ add_rel("cora", 4)
    hide cora with dissolve
    return

label talk_theo:
    if not flag_met_theo:
        show theo at center with dissolve
        narrator "He's in the library, surrounded by notes. He looks up."
        theo "Oh — sorry, am I in your way?"
        mc "No. I'm [player_name]."
        theo "Theo. Walsh."
        narrator "A pause. Not awkward. Just quiet."
        theo "Do you study here often?"
        mc "Starting to."
        theo "Good spot for it."
        $ flag_met_theo = True
        $ add_rel("theo", 8)
        hide theo with dissolve
    else:
        show theo at center with dissolve
        theo "Hey."
        mc "Hey."
        menu:
            "How's the studying going?":
                theo "Slowly. But going."
                $ add_rel("theo", 2)
            "Want company?":
                theo "Yeah. Actually, yeah."
                $ add_rel("theo", 4)
                $ add_stat("happiness", 5)
            "Just hi.":
                theo "Hi."
                $ add_rel("theo", 1)
        hide theo with dissolve
    return

## ── PLACEHOLDER STUBS FOR OTHER NPCS ───────────────────────────
## These will be filled in as scenes are written

label talk_nadia:
    show nadia at center with dissolve
    nadia "You look like you need legal advice."
    mc "I don't think I do."
    nadia "Everyone thinks that. Almost nobody's right."
    $ add_rel("nadia", 3)
    hide nadia with dissolve
    return

label talk_zane:
    show zane at center with dissolve
    zane "First time at the Lounge?"
    menu:
        "Is it that obvious?":
            zane "Little bit. Don't worry. That wears off."
            $ add_rel("zane", 5)
        "I've been around.":
            zane "Then you know how it works. Come back Friday — I'm on."
            $ add_rel("zane", 4)
    hide zane with dissolve
    return

label talk_ronnie:
    show ronnie at center with dissolve
    ronnie "What are you having?"
    menu:
        "Whatever you recommend.":
            ronnie "Smart answer."
            $ add_rel("ronnie", 4)
            $ add_stat("happiness", 5)
        "Just water.":
            ronnie "At the Lounge, we call that 'mineral.'"
            $ add_rel("ronnie", 2)
    hide ronnie with dissolve
    return

## Default stub for any unwritten character
