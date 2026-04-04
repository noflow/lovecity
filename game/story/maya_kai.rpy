## story/maya_kai.rpy — Maya Chen + Kai Nakamura meet scenes
## ═══════════════════════════════════════════════════════════════
## OVERRIDABLE: Export gen_talk_maya / gen_talk_kai etc. to
## story/generated/ to replace these fallback labels.

## ── MAYA ─────────────────────────────────────────────────────
label meet_maya_first:
    ## scene bg_school with dissolve
    show maya at right with dissolve

    narrator "She's in the hallway after class. Textbook under one arm, phone in the other."
    narrator "She's doing four things at once, perfectly."
    narrator "She glances up. Evaluates. Returns to her phone."

    maya "You're new."
    mc "Yeah. [player_name]."
    maya "Maya. Are you in AP English?"
    mc "I — I don't know yet."
    maya "Room 204, Mr. Lennox. If you're not, you should be."
    narrator "She says it as advice, not a question."

    menu:
        "Why do you say that?":
            maya "Because you look like someone who reads. Am I wrong?"
            mc "No."
            maya "Good. See you in 204."
            $ add_rel("maya", 10)

        "Maybe I will.":
            maya "Don't maybe. Either you're doing it or you're not."
            mc "...I'll do it."
            maya "Better."
            $ add_rel("maya", 8)
            $ add_stat("confidence", 2)

        "I'll figure it out.":
            maya "That's usually the wrong approach."
            narrator "She's already walking away."
            $ add_rel("maya", 4)

    $ flag_met_maya = True
    $ unlock_phone_contact("maya")
    hide maya with dissolve
    return


label meet_maya_regular:
    ## scene bg_school with dissolve
    show maya at right with dissolve
    python:
        rel = get_rel("maya")

    if rel < 30:
        maya "You made it to 204."
        mc "I did."
        maya "Good. What did you think of the Woolf piece?"
        menu:
            "Honestly? Couldn't put it down.":
                maya "I knew it."
                $ add_rel("maya", 8)
                $ add_stat("intelligence", 2)
            "It was good. Dense.":
                maya "Dense is good. Dense means there's more."
                $ add_rel("maya", 5)
            "I didn't get to it yet.":
                maya "Get to it."
                $ add_rel("maya", 1)

    elif rel < 70:
        maya "Hey. Are you studying for Harlow's midterm?"
        menu:
            "Not yet. Should I be?":
                maya "He drops three trick questions every time. I have the pattern."
                mc "You... have the pattern."
                maya "I study everything."
                $ add_rel("maya", 8)
                $ add_stat("intelligence", 3)
            "Already started.":
                maya "Then you're ahead of everyone except me."
                narrator "She almost smiles."
                $ add_rel("maya", 6)

    else:
        maya "I wanted to say something."
        narrator "She says it straight. No preamble."
        mc "Okay."
        maya "You're different from when you started here."
        menu:
            "Is that good or bad?":
                maya "Good, I think. You seem more... settled."
                $ add_rel("maya", 12)
                $ add_stat("confidence", 5)
            "I didn't notice.":
                maya "That's usually how it works."
                $ add_rel("maya", 8)

    hide maya with dissolve
    return


## ── KAI ──────────────────────────────────────────────────────
label meet_kai_first:
    ## scene bg_gym with dissolve
    show kai at center with dissolve

    narrator "The gym is busier than you expected."
    narrator "Someone in a grey tank top is correcting a guy's squat form with two words and complete confidence."
    narrator "She notices you standing at the edge."

    kai "First time?"
    mc "That obvious?"
    kai "You're holding the weights like a question."
    narrator "She takes them from you. Adjusts your grip in three seconds."
    kai "Try now."

    menu:
        "That's... actually better.":
            kai "Of course it is."
            narrator "Not arrogant. Just precise."
            mc "I'm [player_name]."
            kai "Kai. If you're serious about being here, book a session. If you're not, the treadmills are over there."
            $ add_rel("kai", 10)
            $ add_stat("fitness", 2)

        "Thanks. I can figure it out from here.":
            kai "You can. But you'll do it wrong for longer."
            narrator "She hands the weights back."
            $ add_rel("kai", 6)

        "Are you a trainer here?":
            kai "Yes."
            narrator "Short, final. Like all her answers."
            $ add_rel("kai", 5)

    $ flag_met_kai = True
    $ unlock_phone_contact("kai")
    hide kai with dissolve
    return
