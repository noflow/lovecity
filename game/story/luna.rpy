## story/luna.rpy — Luna Voss arc
## ═══════════════════════════════════════════════════════════════
## Night shift nurse at Luminos Clinic. Found evenings/nights.
## ═══════════════════════════════════════════════════════════════

label meet_luna_first:
    scene bg_clinic with dissolve
    show luna at right with dissolve

    narrator "The clinic corridor at 9 PM is very different from 9 AM."
    narrator "Quieter. Yellow light. A woman at the far desk, reading."
    narrator "She looks up without hurry."

    luna "Visiting hours are over."
    mc "I know. I'm not visiting."
    luna "Then what are you?"
    mc "Looking for the pharmacy. It's a long story."
    luna "Most things are."

    narrator "She closes her book. Stands."

    luna "Luna Voss. Pharmacy is around the corner. I'll show you."

    menu:
        "Thank you. I'm [player_name].":
            luna "I know who you are. Dr. Rivera mentioned she had a new patient."
            mc "She talks about her patients?"
            luna "Just that she had one. Nothing else. She doesn't do that."
            $ add_rel("luna", 10)

        "You don't have to bother.":
            luna "It's not a bother. I know where it is. You don't."
            narrator "Practical. Not unkind."
            $ add_rel("luna", 7)

    narrator "She walks you there. Doesn't say much. It's not uncomfortable."
    luna "Night shifts. If you need anything after hours."
    narrator "She says it like she's giving you a useful fact, nothing more."

    $ flag_met_luna = True
    hide luna with dissolve
    return
