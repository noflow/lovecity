## story/dr_rivera.rpy — Dr. Elena Rivera arc
## ═══════════════════════════════════════════════════════════════
## OVERRIDABLE: Export gen_talk_dr_rivera / gen_meet_dr_rivera to
## story/generated/ to replace these fallback labels.
## Therapist at Luminos Clinic. The transformation arc hub.
## ═══════════════════════════════════════════════════════════════

label meet_dr_rivera:
    ## scene bg_clinic with dissolve
    show dr_rivera at center with dissolve

    narrator "The receptionist sends you down a quiet corridor."
    narrator "The door at the end has a small brass plate. {b}Dr. E. Rivera{/b}."
    narrator "You knock. A pause. Then:"

    dr_rivera "Come in."

    narrator "The office is calm. Bookshelves. Plants. A large window."
    narrator "She looks up from her notes. Evaluates you without appearing to."

    dr_rivera "You must be [player_name]. Sit anywhere you're comfortable."
    narrator "There are three chairs. You pick one."

    dr_rivera "I'm Dr. Rivera. I won't ask why you're here — that's what the session is for."
    narrator "She sets her pen down."
    dr_rivera "I'll ask something easier first. What did you have for breakfast?"

    menu:
        "Eggs. My mom made them.":
            dr_rivera "Good. And how do you feel right now?"
            mc "Honest answer?"
            dr_rivera "Always."
            mc "Nervous. A little."
            dr_rivera "That's useful information. Hold onto that."
            $ add_stat("trust", 8)

        "I skipped it.":
            dr_rivera "Hmm."
            narrator "She writes something. You can't see what."
            dr_rivera "And what did you skip breakfast {i}for{/i}?"
            mc "Nothing. I just wasn't hungry."
            dr_rivera "Interesting."
            $ add_stat("curiosity", 5)

        "I don't see how that's relevant.":
            dr_rivera "It isn't, particularly. But you answered, which is what I was testing."
            narrator "She almost smiles."
            dr_rivera "You're more cooperative than you think you are."
            $ add_stat("confidence", 3)
            $ add_stat("trust", 4)

    dr_rivera "Tell me what brought you here. In your own words, in your own time."

    menu:
        "I've been feeling... off. Hard to describe.":
            dr_rivera "Then we'll find the words together."
            $ add_rel("dr_rivera", 12)
            $ add_stat("trust", 6)
            $ add_stat("acceptance", 5)

        "Honestly, I'm not sure why I came.":
            dr_rivera "That's often where the most interesting answers live."
            $ add_rel("dr_rivera", 10)
            $ add_stat("curiosity", 5)

        "I have questions about myself I can't answer.":
            dr_rivera "Then you're in the right place."
            narrator "She says it simply. Not like a slogan. Like a fact."
            $ add_rel("dr_rivera", 15)
            $ add_stat("trust", 8)
            $ add_stat("acceptance", 8)

    $ flag_met_dr_rivera = True
    $ unlock_phone_contact("dr_rivera")
    $ flag_therapy_started = True

    dr_rivera "We'll stop there for today. Same time next week?"
    mc "Yes."
    dr_rivera "Good. And [player_name]..."
    narrator "She picks up her pen again."
    dr_rivera "Eat breakfast."

    hide dr_rivera with dissolve
    return


## ── REGULAR THERAPY SESSIONS ────────────────────────────────────
label therapy_session_regular:
    ## scene bg_clinic with dissolve
    show dr_rivera at center with dissolve
    python:
        rel = get_rel("dr_rivera")
        session_trust = store.stat_trust

    if session_trust < 20:
        call therapy_session_early
    elif session_trust < 50:
        call therapy_session_mid
    else:
        call therapy_session_deep

    $ advance_time(1)
    $ stat_money -= 80
    hide dr_rivera with dissolve
    return


label therapy_session_early:
    dr_rivera "How has the week been?"
    menu:
        "Okay. Mostly.":
            dr_rivera "What does 'mostly' cover?"
            mc "Things I haven't quite figured out how to say yet."
            dr_rivera "That's progress. You know they exist."
            $ add_stat("trust", 5)
            $ add_stat("acceptance", 3)

        "Difficult.":
            dr_rivera "In what way?"
            mc "In the way where you know something is changing but can't see what yet."
            dr_rivera "That's quite precise, for something you can't see."
            $ add_stat("trust", 8)

        "Fine. Normal.":
            dr_rivera "You said that the same way last time."
            mc "Maybe because it's true."
            dr_rivera "Mm. We'll come back to that."
            $ add_stat("curiosity", 3)

    $ add_rel("dr_rivera", 6)
    return


label therapy_session_mid:
    dr_rivera "I've been thinking about something you said last week."
    mc "What was that?"
    dr_rivera "That you feel more like yourself in some moments than others."
    narrator "She waits."
    dr_rivera "Can you tell me more about the moments when you feel most like yourself?"

    menu:
        "When I'm alone, usually.":
            dr_rivera "And when you're with others?"
            mc "Performing, a little. Like I'm wearing something that doesn't quite fit."
            dr_rivera "That's important. What would 'fitting' look like to you?"
            $ add_stat("acceptance", 8)
            $ add_stat("trust", 6)

        "Honestly? When I don't think about it.":
            dr_rivera "What happens when you do think about it?"
            mc "It gets complicated."
            dr_rivera "Complicated how?"
            mc "Like there are two answers to every question about myself."
            narrator "She writes something. A longer note."
            $ add_stat("trust", 10)
            $ add_stat("acceptance", 6)

        "I'm not sure I've felt that.":
            dr_rivera "That's worth sitting with."
            narrator "She doesn't push."
            $ add_stat("trust", 4)

    $ add_rel("dr_rivera", 10)
    $ add_stat("curiosity", 4)
    return


label therapy_session_deep:
    dr_rivera "We've talked around something for a while now."
    mc "Have we?"
    dr_rivera "I think you know what it is."

    menu:
        "Maybe I do.":
            dr_rivera "Then let's say it out loud."
            mc "I've been thinking about... who I am. What I am."
            narrator "A long pause. She doesn't rush it."
            dr_rivera "And what are you?"
            mc "I don't know yet. But I think I want to find out."
            dr_rivera "That's everything."
            $ add_stat("acceptance", 15)
            $ add_stat("trust", 10)
            $ add_stat("confidence", 8)
            $ body_femininity += 5

        "I'm not ready to say it yet.":
            dr_rivera "Then we don't. But it'll be here when you are."
            $ add_stat("trust", 5)

        "There's nothing to say.":
            dr_rivera "All right."
            narrator "She doesn't believe you. You know she doesn't."
            narrator "You're not sure you believe yourself."
            $ add_stat("curiosity", 5)

    $ add_rel("dr_rivera", 15)
    return
