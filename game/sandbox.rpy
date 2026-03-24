## sandbox.rpy — Core sandbox loop
## ═══════════════════════════════════════════════════════════════
## ARCHITECTURE:
##   - No call/return pairs that escape via jump (corrupts call stack)
##   - All navigation uses jump only, from top-level labels only
##   - renpy.call_screen() returns values — result drives next jump
##   - lc_set_bg() is a Python function, never a label — no scene calls
##   - Backgrounds rendered inside screens via 'add', never via scene
## ═══════════════════════════════════════════════════════════════

## ── BACKGROUND HELPER ────────────────────────────────────────────
init python:
    def lc_set_bg(loc_id, room_id=None):
        bg_map = {
            "home":"bg_home","school":"bg_school","cafe":"bg_cafe",
            "mall":"bg_mall","park":"bg_park","clinic":"bg_clinic",
            "gym":"bg_gym","office":"bg_office","bar":"bg_bar",
            "library":"bg_library","salon":"bg_salon","street":"bg_street",
            "bedroom":"bg_bedroom","kitchen":"bg_kitchen",
            "livingroom":"bg_livingroom","bathroom":"bg_bathroom",
            "garden":"bg_garden",
        }
        key = bg_map.get(room_id or loc_id, bg_map.get(loc_id, "bg_default"))
        store._current_bg_key   = key
        store._current_bg_color = bg_colors.get(key, "#0a0a1e")

    def get_room_actions(room_id):
        return {
            "bedroom":    [("sleep","💤 Sleep"),("nap","😴 Nap"),("meditate","🧘 Meditate"),("change","👗 Change outfit")],
            "kitchen":    [("snack","🍎 Snack"),("breakfast","🥣 Breakfast"),("cook","🍳 Cook")],
            "livingroom": [("tv","📺 Watch TV"),("games","🎮 Games"),("relax","😌 Relax")],
            "bathroom":   [("shower","🚿 Shower"),("glam","💄 Full glam"),("mirror","🪞 Mirror")],
            "garden":     [("garden","🌿 Garden"),("sit","🪑 Sit outside")],
        }.get(room_id, [])

    def get_location_actions(loc_id):
        return {
            "cafe":    [("coffee","☕ Coffee"),("study","📖 Study"),("people","👀 People-watch")],
            "gym":     [("lift","🏋️ Weights"),("cardio","🏃 Cardio"),("swim","🏊 Swim")],
            "park":    [("walk","🚶 Walk"),("jog","🏃 Jog"),("sit","🪑 Sit"),("flowers","🌸 Flowers")],
            "library": [("read","📖 Read"),("research","🔬 Research"),("rest","😌 Rest")],
            "mall":    [("shop","🛍️ Browse"),("food","🍜 Food court"),("arcade","🕹️ Arcade")],
            "clinic":  [("checkup","🩺 Check-up"),("therapy","🛋️ Therapy")],
            "bar":     [("drink","🍸 Drink"),("dance","🕺 Dance"),("watch","🎶 Watch DJ")],
            "school":  [("class","📖 Class"),("studyhall","✏️ Study hall"),("mingle","😊 Mingle")],
            "salon":   [("haircut","✂️ Haircut"),("makeup","💄 Makeup"),("nails","💅 Nails")],
        }.get(loc_id, [])

default _current_bg_key   = "bg_bedroom"
default _current_bg_color = "#1a1230"

## ── MAIN ENTRY — all navigation starts here ──────────────────────
label sandbox_loop:
    jump sandbox_map_loop

## ── MAP LOOP — show map, wait for location click ─────────────────
label sandbox_map_loop:
    $ lc_set_bg("street")
    $ _map_result = renpy.call_screen("lc_map")
    if _map_result[0] == "wait":
        jump sandbox_map_wait
    elif _map_result[0] == "travel":
        jump sandbox_location_enter
    jump sandbox_map_loop

label sandbox_map_wait:
    $ advance_time(1)
    python:
        p = time_period
        icons = ["☀️","🌤️","🌇","🌙"]
        names = ["Morning","Afternoon","Evening","Night"]
    "[icons[p]] You wait. It's now [names[p]]."
    jump sandbox_map_loop

## ── LOCATION ENTER — jumped to by map button ─────────────────────
label sandbox_location_enter:
    if current_location == "home":
        jump sandbox_home_loop
    else:
        jump sandbox_hub_loop

## ── HOME LOOP ─────────────────────────────────────────────────────
label sandbox_home_loop:
    $ current_room = "bedroom"
    jump sandbox_room_loop

label sandbox_room_loop:
    $ lc_set_bg("home", current_room)
    python:
        _room_actions = get_room_actions(current_room)
        _npcs_here    = []
        for _npc_id in ["mom", "sister"]:
            _nloc, _nroom, _ = get_npc_location(_npc_id)
            if _nloc == "home" and (_nroom == current_room or _nroom is None):
                _npcs_here.append(_npc_id)
    $ _room_result = renpy.call_screen("lc_home_room",
        current_room_id = current_room,
        npcs_here       = _npcs_here,
        room_actions    = _room_actions)
    if _room_result[0] == "talk":
        $ _talk_target = _room_result[1]
        jump sandbox_room_talk
    elif _room_result[0] == "action":
        $ _action_id = _room_result[1]
        jump sandbox_room_action
    elif _room_result[0] == "wait":
        jump sandbox_room_wait
    elif _room_result[0] == "goto_room":
        $ current_room = _room_result[1]
        jump sandbox_room_enter_event
    elif _room_result[0] == "goto_map":
        jump sandbox_map_loop
    jump sandbox_room_loop

label sandbox_room_enter_event:
    ## Check for one-time room entry events
    if current_room == "kitchen" and time_day == 1 and time_period == 0 and not flag_met_sister:
        $ flag_met_sister = True
        show sister at right with dissolve
        sister "Oh — you actually came in here."
        mc "Morning."
        sister "You look nervous."
        menu:
            "I'm not nervous.":
                sister "Your left eye is doing that thing."
                $ add_rel("sister", 3)
            "A little, maybe.":
                sister "Don't be. They're just people."
                $ add_rel("sister", 6)
                $ add_stat("confidence", 3)
            "I'm fine. Mind your business.":
                sister "Rude. Good luck anyway."
                $ add_rel("sister", 1)
        hide sister with dissolve
    jump sandbox_room_loop

label sandbox_room_talk:
    call expression "talk_" + _talk_target
    jump sandbox_room_loop

label sandbox_room_action:
    call expression "action_home_" + _action_id
    jump sandbox_room_loop

label sandbox_room_wait:
    $ advance_time(1)
    python:
        p = time_period
        icons = ["☀️","🌤️","🌇","🌙"]
        names = ["Morning","Afternoon","Evening","Night"]
    "[icons[p]] Time passes. It's now [names[p]]."
    jump sandbox_room_loop

## ── LOCATION HUB LOOP ────────────────────────────────────────────
label sandbox_hub_loop:
    $ lc_set_bg(current_location)
    python:
        _loc_id      = current_location
        _npcs_here   = npcs_at_location(_loc_id)
        _loc_actions = get_location_actions(_loc_id)
    $ _hub_result = renpy.call_screen("lc_location_hub",
        loc_id      = current_location,
        npcs_here   = _npcs_here,
        loc_actions = _loc_actions)
    if _hub_result[0] == "talk":
        $ _talk_target = _hub_result[1]
        jump sandbox_hub_talk
    elif _hub_result[0] == "action":
        $ _action_id = _hub_result[1]
        jump sandbox_hub_action
    elif _hub_result[0] == "wait":
        jump sandbox_hub_wait
    elif _hub_result[0] == "goto_map":
        jump sandbox_map_loop
    jump sandbox_hub_loop

label sandbox_hub_talk:
    call expression "talk_" + _talk_target
    jump sandbox_hub_loop

label sandbox_hub_action:
    call expression "action_" + current_location + "_" + _action_id
    jump sandbox_hub_loop

label sandbox_hub_wait:
    $ advance_time(1)
    python:
        p = time_period
        icons = ["☀️","🌤️","🌇","🌙"]
        names = ["Morning","Afternoon","Evening","Night"]
    "[icons[p]] Time passes. It's now [names[p]]."
    jump sandbox_hub_loop

## ── WAIT FROM MAP ────────────────────────────────────────────────
label sandbox_wait_from_map:
    jump sandbox_map_wait

## ── TALKSTUB — any unwritten character ───────────────────────────
label talk_default:
    "They nod at you. Busy."
    return

## ── HOME ACTIONS ─────────────────────────────────────────────────
label action_home_sleep:
    $ add_stat("energy", 100)
    $ add_stat("happiness", 5)
    $ advance_time(2)
    "You sleep deeply. Full energy restored."
    return

label action_home_nap:
    $ add_stat("energy", 40)
    $ advance_time(1)
    "A nap. You feel better. +40 energy."
    return

label action_home_meditate:
    $ add_stat("happiness", 10)
    $ add_stat("energy", 5)
    $ advance_time(1)
    "Quiet and still. +10 happiness."
    return

label action_home_change:
    "You look through your wardrobe."
    return

label action_home_snack:
    $ add_stat("energy", 15)
    "A snack. +15 energy."
    return

label action_home_breakfast:
    $ add_stat("energy", 35)
    $ add_stat("happiness", 5)
    $ advance_time(1)
    "A proper breakfast. +35 energy, +5 happiness."
    return

label action_home_cook:
    $ add_stat("energy", 50)
    $ add_stat("happiness", 10)
    $ advance_time(1)
    "A real meal. Worth the time. +50 energy."
    return

label action_home_tv:
    $ add_stat("happiness", 10)
    $ advance_time(1)
    "Two episodes. Nothing important. +10 happiness."
    return

label action_home_games:
    $ add_stat("happiness", 20)
    $ advance_time(1)
    "An hour vanishes. +20 happiness."
    return

label action_home_relax:
    $ add_stat("happiness", 6)
    $ add_stat("energy", 5)
    "Just being still. +6 happiness."
    return

label action_home_shower:
    $ add_stat("charm", 10)
    $ add_stat("energy", 10)
    $ advance_time(1)
    "Hot shower. +10 charm, +10 energy."
    return

label action_home_glam:
    $ add_stat("charm", 20)
    $ advance_time(1)
    "Full routine. +20 charm."
    return

label action_home_mirror:
    $ add_stat("acceptance", 2)
    "You look. You look for a while."
    thought "Not bad."
    return

label action_home_garden:
    $ add_stat("happiness", 10)
    $ advance_time(1)
    "An hour with the plants. +10 happiness."
    return

label action_home_sit:
    $ add_stat("happiness", 8)
    "The garden in the afternoon. The light does something good."
    return

## ── LOCATION ACTIONS ─────────────────────────────────────────────
label action_cafe_coffee:
    $ add_stat("energy", 30)
    $ stat_money -= 5
    "A good cortado. +30 energy."
    return

label action_cafe_study:
    $ add_stat("intelligence", 3)
    $ advance_time(1)
    "The ambient noise helps. +3 intelligence."
    return

label action_cafe_people:
    $ add_stat("charm", 5)
    $ advance_time(1)
    "You watch. You learn. +5 charm."
    return

label action_gym_lift:
    $ add_stat("fitness", 5)
    $ stat_energy -= 25
    $ advance_time(1)
    "Heavy sets. Tired and great. +5 fitness."
    return

label action_gym_cardio:
    $ add_stat("fitness", 4)
    $ add_stat("happiness", 5)
    $ stat_energy -= 20
    $ advance_time(1)
    "Your lungs burn well. +4 fitness."
    return

label action_gym_swim:
    $ add_stat("fitness", 4)
    $ add_stat("happiness", 10)
    $ stat_energy -= 20
    $ advance_time(1)
    "Lap after lap. +4 fitness."
    return

label action_park_walk:
    $ add_stat("happiness", 10)
    $ add_stat("fitness", 2)
    $ stat_energy -= 10
    $ advance_time(1)
    "Fresh air. +10 happiness."
    return

label action_park_jog:
    $ add_stat("fitness", 5)
    $ stat_energy -= 20
    $ advance_time(1)
    "Three miles. +5 fitness."
    return

label action_park_sit:
    $ add_stat("happiness", 8)
    $ advance_time(1)
    "The bench is warm. +8 happiness."
    return

label action_park_flowers:
    $ add_item("rose")
    "You pick a rose. It's perfect."
    return

label action_library_read:
    $ add_stat("intelligence", 5)
    $ stat_energy -= 15
    $ advance_time(2)
    "Two good hours. +5 intelligence."
    return

label action_library_research:
    $ add_stat("intelligence", 8)
    $ stat_energy -= 25
    $ advance_time(3)
    "Deep dive. +8 intelligence."
    return

label action_library_rest:
    $ add_stat("energy", 10)
    $ advance_time(1)
    "The armchair in the corner. +10 energy."
    return

label action_mall_shop:
    "You browse. Nothing today."
    return

label action_mall_food:
    $ add_stat("energy", 25)
    $ stat_money -= 8
    $ advance_time(1)
    "Food court ramen. +25 energy."
    return

label action_mall_arcade:
    $ add_stat("happiness", 15)
    $ stat_money -= 5
    $ advance_time(1)
    "An hour on the machines. +15 happiness."
    return

label action_clinic_checkup:
    if stat_money >= 30:
        $ add_stat("energy", 20)
        $ stat_money -= 30
        "The doctor clears you. +20 energy."
    else:
        "You need $30 for a check-up."
    return

label action_clinic_therapy:
    if not flag_met_dr_rivera:
        jump meet_dr_rivera
    else:
        jump therapy_session_regular
    return

label action_bar_drink:
    $ add_stat("happiness", 15)
    $ stat_money -= 12
    $ advance_time(1)
    "One cocktail. +15 happiness."
    return

label action_bar_dance:
    $ add_stat("happiness", 20)
    $ add_stat("charm", 5)
    $ stat_energy -= 20
    $ advance_time(2)
    "Two hours on the floor. +20 happiness."
    return

label action_bar_watch:
    $ add_stat("happiness", 15)
    $ advance_time(1)
    "The DJ is good. +15 happiness."
    return

label action_school_class:
    $ add_stat("intelligence", 5)
    $ stat_energy -= 20
    $ advance_time(3)
    "Three hours. +5 intelligence."
    return

label action_school_studyhall:
    $ add_stat("intelligence", 3)
    $ stat_energy -= 10
    $ advance_time(1)
    "Study hall. +3 intelligence."
    return

label action_school_mingle:
    $ add_stat("charm", 5)
    $ advance_time(1)
    "Between classes. +5 charm."
    return

label action_salon_haircut:
    if stat_money >= 40:
        $ add_stat("charm", 8)
        $ stat_money -= 40
        $ advance_time(1)
        "The stylist does something right. +8 charm."
    else:
        "You need $40."
    return

label action_salon_makeup:
    if stat_money >= 30:
        $ add_stat("charm", 10)
        $ stat_money -= 30
        $ advance_time(1)
        "You look in the mirror. Better. +10 charm."
    else:
        "You need $30."
    return

label action_salon_nails:
    if stat_money >= 25:
        $ add_stat("charm", 6)
        $ stat_money -= 25
        "Small thing. Big impact. +6 charm."
    else:
        "You need $25."
    return

## ── STORY EVENTS ─────────────────────────────────────────────────
label event_first_afternoon:
    thought "There's a lot of city out there. No rush."
    $ add_diary("Made it through the first morning.")
    return

label event_therapy_nudge:
    thought "I keep thinking about the clinic."
    return

## ── SET BACKGROUND (kept as label for compatibility) ─────────────
label set_background(loc_id, room_id=None):
    $ lc_set_bg(loc_id, room_id)
    return

label check_scheduled_events:
    return

label check_location_event(loc_id):
    return

label check_room_event(room_id):
    return

label sandbox_wait:
    $ advance_time(1)
    return
