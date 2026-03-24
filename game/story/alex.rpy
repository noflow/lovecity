## story/alex.rpy — Alex Rivera arc
## ═══════════════════════════════════════════════════════════════
## Alex works at Moondrop Café (weekday afternoons + weekend mornings)
## Free-spirited barista. Paints on weekends.
## ═══════════════════════════════════════════════════════════════

label meet_alex_first:
    ## scene bg_cafe with dissolve
    show alex at center with dissolve

    narrator "She's behind the counter. Writing something on a napkin."
    narrator "She looks up when you walk in. Doesn't stop writing."

    alex "Be right with you."
    narrator "A minute passes. She finishes, folds the napkin, tucks it in her apron."
    alex "Sorry. What can I get you?"

    menu:
        "What do you recommend?":
            alex "Depends what kind of day you're having."
            mc "How can you tell what kind of day I'm having?"
            alex "Practice."
            narrator "She makes something without asking. Sets it in front of you."
            alex "Cortado. You look like you need something decisive."
            $ add_stat("energy", 20)
            $ stat_money -= 5
            $ add_rel("alex", 10)

        "Just a black coffee.":
            alex "Simple. Honest. Good."
            narrator "She has it ready in two minutes. Hands it over without ceremony."
            $ add_stat("energy", 15)
            $ stat_money -= 4
            $ add_rel("alex", 6)

        "I'll look at the menu for a second.":
            alex "Take your time."
            narrator "She goes back to the napkin. You notice she's drawing on it, not writing."
            $ add_rel("alex", 4)

    $ flag_met_alex = True
    narrator "She doesn't ask your name. She doesn't need to. You'll be back."
    hide alex with dissolve
    return


label meet_alex_regular:
    ## scene bg_cafe with dissolve
    show alex at center with dissolve
    python:
        rel = get_rel("alex")

    if rel < 20:
        alex "Back again."
        mc "Back again."
        alex "That's all I need to know."
        $ add_rel("alex", 3)
    elif rel < 50:
        alex "The usual?"
        mc "You remember?"
        alex "I remember everyone. Occupational thing."
        menu:
            "That's kind of intimidating.":
                alex "Good kind or bad kind?"
                mc "I haven't decided."
                alex "Let me know when you do."
                $ add_rel("alex", 5)
            "I don't mind.":
                alex "Good. Then sit down. You look like you have something on your mind."
                $ add_rel("alex", 7)
                $ add_stat("trust", 3)
    else:
        alex "Hey, you."
        narrator "She says it like you're already in the middle of a conversation."
        menu:
            "What are you drawing today?":
                alex "Something I saw this morning. A woman on the bus reading two books at once."
                mc "How does that work?"
                alex "I have no idea. That's why I drew it."
                $ add_rel("alex", 6)
                $ add_stat("curiosity", 3)
            "Are you free later?":
                alex "Depends what for."
                python:
                    if get_rel("alex") >= 60:
                        renpy.jump("alex_date_propose")
                    else:
                        renpy.jump("alex_not_yet")
            "Just getting coffee.":
                alex "That's all you ever have to do."
                $ add_rel("alex", 3)

    hide alex with dissolve
    return


label alex_not_yet:
    alex "What did you have in mind?"
    mc "I thought maybe we could—"
    alex "Ask me again sometime. When you know me better."
    narrator "She says it without cruelty. Just clarity."
    $ add_rel("alex", 2)
    return


label alex_date_propose:
    alex "What did you have in mind?"
    menu:
        "Walk in the park? You mentioned you paint outside sometimes.":
            alex "..."
            narrator "She looks at you for a moment."
            alex "Yeah. Saturday afternoon. I'll show you the spot."
            $ add_rel("alex", 15)
            $ add_diary("Alex agreed to show me her painting spot on Saturday.")
        "Just coffee somewhere nicer than here.":
            alex "I work here. You're calling this not nice?"
            mc "I — no — I meant—"
            alex "I'm kidding. Sure. Give me a day that works."
            $ add_rel("alex", 10)
    return
