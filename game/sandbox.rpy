## sandbox.rpy — Core sandbox loop (clickable map edition)
## ═══════════════════════════════════════════════════════════════

## ── ENTRY POINT ─────────────────────────────────────────────────
label sandbox_loop:
    call show_map
    jump sandbox_loop

## ── SHOW MAP ────────────────────────────────────────────────────
label show_map:
    scene Expression("Solid('#0a0f1a')") with dissolve
    call screen lc_map
    return

label sandbox_wait_from_map:
    call sandbox_wait
    call show_map
    return

## ── ENTER LOCATION (called by map click) ────────────────────────
label sandbox_location_enter:
    call set_background(current_location)
    if current_location == "home":
        jump sandbox_home_hub
    else:
        jump sandbox_hub_loop

## ── HOME HUB ────────────────────────────────────────────────────
label sandbox_home_hub:
    call set_background("home", None)
    $ result = renpy.call_screen("lc_home_hub")
    if result[0] == "enter_room":
        $ current_room = result[1]
        call set_background("home", result[1])
        call check_room_event(result[1])
        jump sandbox_room_loop
    elif result[0] == "goto_map":
        jump sandbox_loop

## ── HOME ROOM LOOP ──────────────────────────────────────────────
label sandbox_room_loop:
    python:
        loc_actions = get_room_actions(current_room)
        npcs_here   = []
        for npc_id in ["mom", "sister"]:
            npc_loc, npc_room, _ = get_npc_location(npc_id)
            if npc_loc == "home" and (npc_room == current_room or npc_room is None):
                npcs_here.append(npc_id)
    $ result = renpy.call_screen("lc_location_hub",
        loc_id       = "home",
        npcs_here    = npcs_here,
        loc_actions  = loc_actions)
    if result[0] == "talk":
        call expression "talk_" + result[1]
        jump sandbox_room_loop
    elif result[0] == "action":
        call expression "action_home_" + result[1]
        call check_scheduled_events
        jump sandbox_room_loop
    elif result[0] == "wait":
        call sandbox_wait
        jump sandbox_room_loop
    elif result[0] == "goto_map":
        jump sandbox_loop
    jump sandbox_room_loop

## ── LOCATION HUB LOOP ───────────────────────────────────────────
label sandbox_hub_loop:
    python:
        loc_id      = current_location
        npcs_here   = npcs_at_location(loc_id)
        loc_actions = get_location_actions(loc_id)
    call check_location_event(current_location)
    $ result = renpy.call_screen("lc_location_hub",
        loc_id       = current_location,
        npcs_here    = npcs_here,
        loc_actions  = loc_actions)
    if result[0] == "talk":
        call expression "talk_" + result[1]
        jump sandbox_hub_loop
    elif result[0] == "action":
        call expression "action_" + current_location + "_" + result[1]
        call check_scheduled_events
        jump sandbox_hub_loop
    elif result[0] == "wait":
        call sandbox_wait
        jump sandbox_hub_loop
    elif result[0] == "goto_map":
        jump sandbox_loop
    jump sandbox_hub_loop

## ── WAIT ────────────────────────────────────────────────────────
label sandbox_wait:
    $ advance_time(1)
    python:
        p_icons = ["☀️", "🌤️", "🌇", "🌙"]
        p_names = ["Morning", "Afternoon", "Evening", "Night"]
        p = time_period
    "[p_icons[p]] You wait a while. It's now [p_names[p]]."
    call check_scheduled_events
    return

## ── EVENT CHECKS ────────────────────────────────────────────────
label check_location_event(loc_id):
    python:
        event_key = "loc_evt_" + loc_id + "_d" + str(time_day) + "_p" + str(time_period)
        already_fired = getattr(store, event_key, False)
        setattr(store, event_key, True)
    if loc_id == "street" and not flag_met_cora and flag_met_mom and not already_fired:
        call meet_cora
    return

label check_scheduled_events:
    if time_day == 1 and time_period == 1 and not flag_first_day_done:
        $ flag_first_day_done = True
        call event_first_afternoon
    if time_day >= 3 and not flag_therapy_started and time_period == 0:
        call event_therapy_nudge
    return

label check_room_event(room_id):
    if room_id == "kitchen" and time_day == 1 and time_period == 0 and not flag_met_sister:
        call meet_sister_intro
    return

## ── STORY EVENTS ────────────────────────────────────────────────
label event_first_afternoon:
    "[time_str()] The first day is underway."
    thought "There's a lot of city out there. No rush."
    $ add_diary("Made it through the first morning. The city is bigger than I expected.")
    return

label event_therapy_nudge:
    if current_location == "home":
        thought "I keep thinking about the clinic. Dr. Rivera's name keeps coming up."
        thought "Maybe I should go."
    return

## ── SET BACKGROUND ──────────────────────────────────────────────
label set_background(loc_id, room_id=None):
    python:
        bg_map = {
            "home":"bg_home","school":"bg_school","cafe":"bg_cafe",
            "mall":"bg_mall","park":"bg_park","clinic":"bg_clinic",
            "gym":"bg_gym","office":"bg_office","bar":"bg_bar",
            "library":"bg_library","salon":"bg_salon","street":"bg_street",
            "bedroom":"bg_bedroom","kitchen":"bg_kitchen",
            "livingroom":"bg_livingroom","bathroom":"bg_bathroom",
            "garden":"bg_garden",
        }
        if room_id and room_id in bg_map:
            bg_key = bg_map[room_id]
        elif loc_id in bg_map:
            bg_key = bg_map[loc_id]
        else:
            bg_key = "bg_default"
    if renpy.loadable("backgrounds/" + bg_key + ".webp"):
        scene Expression("'backgrounds/" + bg_key + ".webp'") with dissolve
    elif renpy.loadable("backgrounds/" + bg_key + ".jpg"):
        scene Expression("'backgrounds/" + bg_key + ".jpg'") with dissolve
    else:
        scene Expression("Solid(bg_colors.get('" + bg_key + "', '#0a0a1e'))") with dissolve
    return

## ── HOME ROOM ACTIONS ────────────────────────────────────────────
init python:
    def get_room_actions(room_id):
        return {
            "bedroom":    [("sleep","💤 Sleep"),("nap","😴 Nap"),("meditate","🧘 Meditate"),("change","👗 Change outfit")],
            "kitchen":    [("snack","🍎 Snack"),("breakfast","🥣 Breakfast"),("cook","🍳 Cook meal")],
            "livingroom": [("tv","📺 Watch TV"),("games","🎮 Games"),("relax","😌 Relax")],
            "bathroom":   [("shower","🚿 Shower"),("glam","💄 Full glam"),("mirror","🪞 Mirror")],
            "garden":     [("garden","🌿 Garden"),("sit","🪑 Sit outside")],
        }.get(room_id, [])

label action_home_sleep:
    $ add_stat("energy",100); $ add_stat("happiness",5); $ advance_time(2)
    "You sleep deeply. Full energy restored."; call check_scheduled_events; return
label action_home_nap:
    $ add_stat("energy",40); $ advance_time(1)
    "A nap. You feel better. +40 energy."; return
label action_home_meditate:
    $ add_stat("happiness",10); $ add_stat("energy",5); $ advance_time(1)
    "Quiet and still. +10 happiness, +5 energy."; return
label action_home_change:
    "You look through your wardrobe."; return
label action_home_snack:
    $ add_stat("energy",15)
    "A snack. It helps. +15 energy."; return
label action_home_breakfast:
    $ add_stat("energy",35); $ add_stat("happiness",5); $ advance_time(1)
    "A proper breakfast. +35 energy, +5 happiness."; return
label action_home_cook:
    $ add_stat("energy",50); $ add_stat("happiness",10); $ advance_time(1)
    "A real meal. Worth the time. +50 energy."; return
label action_home_tv:
    $ add_stat("happiness",10); $ advance_time(1)
    "Two episodes. Nothing important. +10 happiness."; return
label action_home_games:
    $ add_stat("happiness",20); $ advance_time(1)
    "An hour vanishes. +20 happiness."; return
label action_home_relax:
    $ add_stat("happiness",6); $ add_stat("energy",5)
    "Just being still for a minute. +6 happiness."; return
label action_home_shower:
    $ add_stat("charm",10); $ add_stat("energy",10); $ advance_time(1)
    "Hot shower. Good pressure. +10 charm, +10 energy."; return
label action_home_glam:
    $ add_stat("charm",20); $ advance_time(1)
    "Full routine. You take your time. +20 charm."; return
label action_home_mirror:
    $ add_stat("acceptance",2)
    "You look. You look for a while."; thought "Not bad."; return
label action_home_garden:
    $ add_stat("happiness",10); $ advance_time(1)
    "An hour with the plants. +10 happiness."; return
label action_home_sit:
    $ add_stat("happiness",8)
    "The garden in the afternoon. The light does something good."; return

## ── LOCATION ACTIONS ─────────────────────────────────────────────
init python:
    def get_location_actions(loc_id):
        return {
            "cafe":    [("coffee","☕ Coffee"),("study","📖 Study"),("people","👀 People-watch")],
            "gym":     [("lift","🏋️ Weights"),("cardio","🏃 Cardio"),("swim","🏊 Swim")],
            "park":    [("walk","🚶 Walk"),("jog","🏃 Jog"),("sit","🪑 Sit"),("flowers","🌸 Pick flowers")],
            "library": [("read","📖 Read"),("research","🔬 Research"),("rest","😌 Rest")],
            "mall":    [("shop","🛍️ Browse"),("food","🍜 Food court"),("arcade","🕹️ Arcade")],
            "clinic":  [("checkup","🩺 Check-up"),("therapy","🛋️ Therapy")],
            "bar":     [("drink","🍸 Drink"),("dance","🕺 Dance"),("watch","🎶 Watch DJ")],
            "school":  [("class","📖 Class"),("studyhall","✏️ Study hall"),("mingle","😊 Mingle")],
            "salon":   [("haircut","✂️ Haircut"),("makeup","💄 Makeup"),("nails","💅 Nails")],
        }.get(loc_id, [])

label action_cafe_coffee:
    $ add_stat("energy",30); $ stat_money -= 5
    "A good cortado. +30 energy."; return
label action_cafe_study:
    $ add_stat("intelligence",3); $ advance_time(1)
    "The ambient noise helps. +3 intelligence."; return
label action_cafe_people:
    $ add_stat("charm",5); $ advance_time(1)
    "You watch. You learn. +5 charm."; return
label action_gym_lift:
    $ add_stat("fitness",5); $ stat_energy -= 25; $ advance_time(1)
    "Heavy sets. Tired and great. +5 fitness."; return
label action_gym_cardio:
    $ add_stat("fitness",4); $ add_stat("happiness",5); $ stat_energy -= 20; $ advance_time(1)
    "Your lungs burn well. +4 fitness."; return
label action_gym_swim:
    $ add_stat("fitness",4); $ add_stat("happiness",10); $ stat_energy -= 20; $ advance_time(1)
    "Lap after lap. Meditative. +4 fitness, +10 happiness."; return
label action_park_walk:
    $ add_stat("happiness",10); $ add_stat("fitness",2); $ stat_energy -= 10; $ advance_time(1)
    "Fresh air. Different pace. +10 happiness."; return
label action_park_jog:
    $ add_stat("fitness",5); $ stat_energy -= 20; $ advance_time(1)
    "Three miles. You'll feel it tomorrow. +5 fitness."; return
label action_park_sit:
    $ add_stat("happiness",8); $ advance_time(1)
    "The bench is warm. You watch clouds. +8 happiness."; return
label action_park_flowers:
    $ add_item("rose")
    "You pick a rose. It's perfect. [Rose added to inventory]"; return
label action_library_read:
    $ add_stat("intelligence",5); $ stat_energy -= 15; $ advance_time(2)
    "Two good hours. +5 intelligence."; return
label action_library_research:
    $ add_stat("intelligence",8); $ stat_energy -= 25; $ advance_time(3)
    "Deep dive. Notes fill three pages. +8 intelligence."; return
label action_library_rest:
    $ add_stat("energy",10); $ advance_time(1)
    "The armchair in the corner. +10 energy."; return
label action_mall_shop:
    "You browse. Nothing today, but it passes the time."; return
label action_mall_food:
    $ add_stat("energy",25); $ stat_money -= 8; $ advance_time(1)
    "Food court ramen. Not great, not bad. +25 energy."; return
label action_mall_arcade:
    $ add_stat("happiness",15); $ stat_money -= 5; $ advance_time(1)
    "An hour on the machines. +15 happiness."; return
label action_clinic_checkup:
    if stat_money >= 30:
        $ add_stat("energy",20); $ stat_money -= 30
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
    $ add_stat("happiness",15); $ stat_money -= 12; $ advance_time(1)
    "One cocktail, well made. +15 happiness."; return
label action_bar_dance:
    $ add_stat("happiness",20); $ add_stat("charm",5); $ stat_energy -= 20; $ advance_time(2)
    "Two hours on the floor. +20 happiness."; return
label action_bar_watch:
    $ add_stat("happiness",15); $ advance_time(1)
    "The DJ is good. You let the music work. +15 happiness."; return
label action_school_class:
    $ add_stat("intelligence",5); $ stat_energy -= 20; $ advance_time(3)
    "Three hours. You pay attention when it matters. +5 intelligence."; return
label action_school_studyhall:
    $ add_stat("intelligence",3); $ stat_energy -= 10; $ advance_time(1)
    "Study hall. Focused. +3 intelligence."; return
label action_school_mingle:
    $ add_stat("charm",5); $ advance_time(1)
    "Between classes. Better at this than you thought. +5 charm."; return
label action_salon_haircut:
    if stat_money >= 40:
        $ add_stat("charm",8); $ stat_money -= 40; $ advance_time(1)
        "The stylist does something right. +8 charm."
    else:
        "You need $40."
    return
label action_salon_makeup:
    if stat_money >= 30:
        $ add_stat("charm",10); $ stat_money -= 30; $ advance_time(1)
        "You look in the mirror. Better. +10 charm."
    else:
        "You need $30."
    return
label action_salon_nails:
    if stat_money >= 25:
        $ add_stat("charm",6); $ stat_money -= 25
        "Small thing. Big impact. +6 charm."
    else:
        "You need $25."
    return
