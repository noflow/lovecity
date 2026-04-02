## locations.rpy — Where characters are at each time period
## ═══════════════════════════════════════════════════════════════
##
## Locations:  home, school, cafe, mall, park, clinic,
##             gym, office, bar, library, salon, street
##
## time_period: 0=Morning 1=Afternoon 2=Evening 3=Night
## time_weekday: 0=Sun 1=Mon 2=Tue 3=Wed 4=Thu 5=Fri 6=Sat
## ═══════════════════════════════════════════════════════════════

init python:

    # ── LOCATION METADATA ────────────────────────────────────────
    LOCATIONS = {
        "home":     {"name": "Home",              "icon": "🏠", "bg": "bg_home",      "always_open": True},
        "school":   {"name": "Highbrook Academy", "icon": "🎓", "bg": "bg_school",    "hours": (7, 17)},
        "cafe":     {"name": "Moondrop Café",     "icon": "☕", "bg": "bg_cafe",      "hours": (7, 22)},
        "mall":     {"name": "Sakura Mall",       "icon": "🛍️", "bg": "bg_mall",      "hours": (10, 22)},
        "park":     {"name": "Riverside Park",    "icon": "🌳", "bg": "bg_park",      "always_open": True},
        "clinic":   {"name": "Luminos Clinic",    "icon": "🏥", "bg": "bg_clinic",    "hours": (8, 20)},
        "gym":      {"name": "Iron Peak Gym",     "icon": "💪", "bg": "bg_gym",       "hours": (6, 22)},
        "office":   {"name": "City Office",       "icon": "🏢", "bg": "bg_office",    "hours": (8, 18)},
        "bar":      {"name": "Neon Lounge",       "icon": "🍸", "bg": "bg_bar",       "hours": (21, 2)},
        "library":  {"name": "Grand Library",     "icon": "📚", "bg": "bg_library",   "hours": (9, 21)},
        "salon":    {"name": "Glam Studio",       "icon": "✂️", "bg": "bg_salon",     "hours": (9, 20)},
        "street":   {"name": "City Streets",      "icon": "🏙️", "bg": "bg_street",    "always_open": True},
        "hospital": {"name": "Luminos Clinic",    "icon": "🏥", "bg": "bg_clinic",    "hours": (8, 20)},
        "realestate":     {"name": "Whitfield Realty",  "icon": "🏘️", "bg": "bg_realestate",    "hours": (9, 18)},
        "apt_complex":    {"name": "Apartment Complex", "icon": "🏢", "bg": "bg_apt_complex",   "always_open": True},
        "townhomes":      {"name": "Townhomes",         "icon": "🏠", "bg": "bg_townhomes",     "always_open": True},
        "house_elm":      {"name": "House on Elm St",   "icon": "🏡", "bg": "bg_house_elm",     "always_open": True},
        "house_oak":      {"name": "House on Oak Ave",  "icon": "🏡", "bg": "bg_house_oak",     "always_open": True},
        "penthouse_tower":{"name": "Penthouse Tower",   "icon": "🏙️", "bg": "bg_penthouse",     "always_open": True},
    }

    # ── HOME ROOMS ───────────────────────────────────────────────
    HOME_ROOMS = {
        "bedroom":   {"name": "Your Bedroom",   "icon": "🛏️", "bg": "bg_bedroom"},
        "kitchen":   {"name": "Kitchen",        "icon": "🍳", "bg": "bg_kitchen"},
        "livingroom":{"name": "Living Room",    "icon": "📺", "bg": "bg_livingroom"},
        "bathroom":  {"name": "Bathroom",       "icon": "🚿", "bg": "bg_bathroom"},
        "garden":    {"name": "Garden",         "icon": "🌿", "bg": "bg_garden"},
        "momsroom":  {"name": "Mom's Room",     "icon": "🚪", "bg": "bg_momsroom"},
        "sisroom":   {"name": "Emma's Room",    "icon": "🚪", "bg": "bg_sisroom"},
    }

    # ── NPC SCHEDULE ─────────────────────────────────────────────
    # Format: npc_id -> list of (weekday_mask, period, location, room, activity)
    # weekday_mask: "weekday" | "weekend" | "all" | specific day name
    # period: 0-3

    NPC_SCHEDULE = {
        "mom": [
            ("weekday", 0, "home",   "kitchen",    "Making breakfast"),
            ("weekday", 1, "office", None,         "At work"),
            ("weekday", 2, "home",   "kitchen",    "Cooking dinner"),
            ("weekday", 3, "home",   "livingroom", "Watching TV"),
            ("weekend", 0, "home",   "kitchen",    "Making brunch"),
            ("weekend", 1, "mall",   None,         "Shopping"),
            ("weekend", 2, "park",   None,         "Reading outside"),
            ("weekend", 3, "home",   "livingroom", "Movie night"),
        ],
        "sister": [
            ("weekday", 0, "home",   "kitchen",    "Getting ready"),
            ("weekday", 1, "school", None,         "In class"),
            ("weekday", 2, "park",   None,         "Hanging out"),
            ("weekday", 3, "home",   "bedroom",    "Doing homework"),
            ("weekend", 0, "home",   "bedroom",    "Sleeping in"),
            ("weekend", 1, "mall",   None,         "Shopping"),
            ("weekend", 2, "cafe",   None,         "With friends"),
            ("weekend", 3, "home",   "livingroom", "Watching shows"),
        ],
        "alex": [
            ("all",     0, "home",   None,         "Sleeping"),
            ("weekday", 1, "cafe",   None,         "Working"),
            ("weekday", 2, "park",   None,         "Unwinding"),
            ("weekday", 3, "library",None,         "Reading"),
            ("weekend", 1, "cafe",   None,         "Weekend shift"),
            ("weekend", 2, "park",   None,         "Painting outdoors"),
            ("weekend", 3, "bar",    None,         "Socialising"),
        ],
        "maya": [
            ("weekday", 0, "home",   None,         "Getting ready"),
            ("weekday", 1, "school", None,         "In class"),
            ("weekday", 2, "library",None,         "Studying"),
            ("weekday", 3, "home",   None,         "Resting"),
            ("weekend", 0, "home",   None,         "Sleeping in"),
            ("weekend", 1, "park",   None,         "Jogging"),
            ("weekend", 2, "cafe",   None,         "Coffee and study"),
            ("weekend", 3, "home",   None,         "Quiet night"),
        ],
        "kai": [
            ("all",     0, "gym",    None,         "Morning training"),
            ("weekday", 1, "gym",    None,         "Training clients"),
            ("weekday", 2, "park",   None,         "Evening run"),
            ("weekday", 3, "home",   None,         "Recovery"),
            ("weekend", 1, "gym",    None,         "Weekend sessions"),
            ("weekend", 2, "cafe",   None,         "Meal prep coffee"),
            ("weekend", 3, "home",   None,         "Rest"),
        ],
        "luna": [
            ("all",     0, "clinic", None,         "Night shift ending"),
            ("weekday", 1, "home",   None,         "Sleeping (day off)"),
            ("weekday", 2, "library",None,         "Reading"),
            ("weekday", 3, "clinic", None,         "Night shift"),
            ("weekend", 1, "cafe",   None,         "Quiet morning"),
            ("weekend", 2, "park",   None,         "Walking"),
            ("weekend", 3, "clinic", None,         "Night shift"),
        ],
        "dr_rivera": [
            ("weekday", 0, "clinic", None,         "Preparing for patients"),
            ("weekday", 1, "clinic", None,         "Seeing patients"),
            ("weekday", 2, "clinic", None,         "Late appointments"),
            ("weekday", 3, "home",   None,         "Resting"),
            ("weekend", 0, "cafe",   None,         "Reading over coffee"),
            ("weekend", 1, "park",   None,         "Morning walk"),
            ("weekend", 2, "home",   None,         "Private time"),
            ("weekend", 3, "home",   None,         "Quiet evening"),
        ],
        "cora": [
            ("all",     0, "home",   None,         "Morning garden"),
            ("weekday", 1, "mall",   None,         "Flower stall"),
            ("weekday", 2, "home",   None,         "Arranging flowers"),
            ("weekday", 3, "home",   None,         "Evening"),
            ("weekend", 1, "mall",   None,         "Busy market day"),
            ("weekend", 2, "park",   None,         "Gathering flowers"),
            ("weekend", 3, "bar",    None,         "Weekend drink"),
        ],
        "zane": [
            ("all",     0, "home",   None,         "Sleeping late"),
            ("weekday", 1, "cafe",   None,         "Working on music"),
            ("weekday", 2, "bar",    None,         "Soundcheck"),
            ("weekday", 3, "bar",    None,         "DJ set"),
            ("weekend", 1, "home",   None,         "Producing"),
            ("weekend", 2, "bar",    None,         "Big night"),
            ("weekend", 3, "bar",    None,         "After party"),
        ],
        "ronnie": [
            ("all",     0, "home",   None,         "Sleeping"),
            ("all",     1, "bar",    None,         "Managing the bar"),
            ("all",     2, "bar",    None,         "Busy shift"),
            ("all",     3, "bar",    None,         "Running the night"),
        ],
        "theo": [
            ("weekday", 0, "home",   None,         "Getting ready"),
            ("weekday", 1, "school", None,         "In class"),
            ("weekday", 2, "library",None,         "Studying"),
            ("weekday", 3, "cafe",   None,         "Evening coffee"),
            ("weekend", 0, "home",   None,         "Sleeping in"),
            ("weekend", 1, "library",None,         "Weekend study"),
            ("weekend", 2, "park",   None,         "Break"),
            ("weekend", 3, "home",   None,         "Night in"),
        ],
        "prof_harlow": [
            ("weekday", 0, "school", None,         "Office hours"),
            ("weekday", 1, "school", None,         "Teaching"),
            ("weekday", 2, "school", None,         "Marking papers"),
            ("weekday", 3, "home",   None,         "Reading"),
            ("weekend", 0, "library",None,         "Research"),
            ("weekend", 1, "library",None,         "Research"),
            ("weekend", 2, "home",   None,         "Rest"),
            ("weekend", 3, "home",   None,         "Rest"),
        ],
        "sera": [
            ("weekday", 0, "home",   None,         "Getting ready"),
            ("weekday", 1, "school", None,         "In class"),
            ("weekday", 2, "library",None,         "Studying"),
            ("weekday", 3, "home",   None,         "Reading"),
            ("weekend", 0, "home",   None,         "Sleeping in"),
            ("weekend", 1, "library",None,         "Quiet study"),
            ("weekend", 2, "cafe",   None,         "Reading over coffee"),
            ("weekend", 3, "home",   None,         "Night in"),
        ],
        "nadia": [
            ("weekday", 0, "home",   None,         "Getting ready"),
            ("weekday", 1, "library",None,         "Law studies"),
            ("weekday", 2, "cafe",   None,         "Study break"),
            ("weekday", 3, "home",   None,         "Reviewing cases"),
            ("weekend", 0, "home",   None,         "Sleeping in"),
            ("weekend", 1, "library",None,         "Research"),
            ("weekend", 2, "park",   None,         "Walking"),
            ("weekend", 3, "bar",    None,         "Weekend out"),
        ],
        "simone": [
            ("weekday", 0, "home",   None,         "Morning routine"),
            ("weekday", 1, "mall",   None,         "Content creation"),
            ("weekday", 2, "salon",  None,         "Getting styled"),
            ("weekday", 3, "bar",    None,         "Networking"),
            ("weekend", 0, "home",   None,         "Sleeping in"),
            ("weekend", 1, "cafe",   None,         "Brunch content"),
            ("weekend", 2, "mall",   None,         "Shopping haul"),
            ("weekend", 3, "home",   None,         "Editing posts"),
        ],
        "dom": [
            ("all",     0, "home",   None,         "Morning prep"),
            ("weekday", 1, "cafe",   None,         "Lunch prep"),
            ("weekday", 2, "cafe",   None,         "Dinner service"),
            ("weekday", 3, "home",   None,         "Winding down"),
            ("weekend", 1, "cafe",   None,         "Busy brunch"),
            ("weekend", 2, "cafe",   None,         "Weekend rush"),
            ("weekend", 3, "bar",    None,         "Post-shift drink"),
        ],
        "reo": [
            ("all",     0, "clinic", None,         "Early shift"),
            ("weekday", 1, "clinic", None,         "On call"),
            ("weekday", 2, "gym",    None,         "Working out"),
            ("weekday", 3, "home",   None,         "Recovery"),
            ("weekend", 1, "clinic", None,         "Weekend shift"),
            ("weekend", 2, "park",   None,         "Decompressing"),
            ("weekend", 3, "bar",    None,         "Socialising"),
        ],
        "jamie": [
            ("weekday", 0, "home",   None,         "Getting ready"),
            ("weekday", 1, "school", None,         "In class"),
            ("weekday", 2, "gym",    None,         "Cheer practice"),
            ("weekday", 3, "home",   None,         "Homework"),
            ("weekend", 0, "home",   None,         "Sleeping in"),
            ("weekend", 1, "mall",   None,         "Shopping"),
            ("weekend", 2, "park",   None,         "Hanging out"),
            ("weekend", 3, "home",   None,         "Night in"),
        ],
        "river": [
            ("all",     0, "home",   None,         "Sleeping late"),
            ("weekday", 1, "salon",  None,         "Tattoo appointments"),
            ("weekday", 2, "salon",  None,         "Walk-ins"),
            ("weekday", 3, "bar",    None,         "Evening out"),
            ("weekend", 1, "salon",  None,         "Busy day"),
            ("weekend", 2, "park",   None,         "Sketching"),
            ("weekend", 3, "bar",    None,         "Weekend night"),
        ],
        "sasha": [
            ("all",     0, "home",   None,         "Sleeping"),
            ("weekday", 1, "home",   None,         "Planning events"),
            ("weekday", 2, "bar",    None,         "Setting up"),
            ("weekday", 3, "bar",    None,         "Promoting"),
            ("weekend", 1, "mall",   None,         "Shopping"),
            ("weekend", 2, "bar",    None,         "Big event"),
            ("weekend", 3, "bar",    None,         "Main event"),
        ],
        "petra": [
            ("weekday", 0, "home",   None,         "Morning routine"),
            ("weekday", 1, "mall",   None,         "Running boutique"),
            ("weekday", 2, "mall",   None,         "Late appointments"),
            ("weekday", 3, "home",   None,         "Evening"),
            ("weekend", 0, "home",   None,         "Relaxing"),
            ("weekend", 1, "mall",   None,         "Weekend sales"),
            ("weekend", 2, "cafe",   None,         "Afternoon off"),
            ("weekend", 3, "home",   None,         "Quiet night"),
        ],
        "august": [
            ("weekday", 0, "library",None,         "Opening up"),
            ("weekday", 1, "library",None,         "Shelving"),
            ("weekday", 2, "library",None,         "Closing duties"),
            ("weekday", 3, "home",   None,         "Reading"),
            ("weekend", 0, "cafe",   None,         "Morning coffee"),
            ("weekend", 1, "library",None,         "Weekend hours"),
            ("weekend", 2, "park",   None,         "Afternoon walk"),
            ("weekend", 3, "home",   None,         "Quiet evening"),
        ],
        "arlo": [
            ("all",     0, "home",   None,         "Sleeping"),
            ("weekday", 1, "street", None,         "Painting murals"),
            ("weekday", 2, "park",   None,         "Sketching"),
            ("weekday", 3, "bar",    None,         "Hanging out"),
            ("weekend", 1, "street", None,         "Big project"),
            ("weekend", 2, "cafe",   None,         "Taking a break"),
            ("weekend", 3, "bar",    None,         "Weekend vibes"),
        ],
        "eli": [
            ("all",     0, "home",   None,         "Sleeping late"),
            ("weekday", 1, "home",   None,         "Practising"),
            ("weekday", 2, "bar",    None,         "Soundcheck"),
            ("weekday", 3, "bar",    None,         "Playing a set"),
            ("weekend", 1, "home",   None,         "Recording"),
            ("weekend", 2, "cafe",   None,         "Coffee run"),
            ("weekend", 3, "bar",    None,         "Late gig"),
        ],
        "milo": [
            ("all",     0, "home",   None,         "Coding"),
            ("weekday", 1, "cafe",   None,         "Working remotely"),
            ("weekday", 2, "library",None,         "Research"),
            ("weekday", 3, "home",   None,         "Gaming"),
            ("weekend", 1, "cafe",   None,         "Coffee + code"),
            ("weekend", 2, "park",   None,         "Touch grass"),
            ("weekend", 3, "home",   None,         "Game night"),
        ],
        "oz": [
            ("all",     0, "home",   None,         "Prep work"),
            ("weekday", 1, "street", None,         "Food truck lunch"),
            ("weekday", 2, "street", None,         "Dinner rush"),
            ("weekday", 3, "bar",    None,         "Late hang"),
            ("weekend", 1, "park",   None,         "Park pop-up"),
            ("weekend", 2, "street", None,         "Weekend spot"),
            ("weekend", 3, "bar",    None,         "Celebrating"),
        ],
        "vesper": [
            ("all",     0, "home",   None,         "Unknown"),
            ("weekday", 1, "library",None,         "Researching"),
            ("weekday", 2, "cafe",   None,         "People watching"),
            ("weekday", 3, "bar",    None,         "Observing"),
            ("weekend", 1, "park",   None,         "Walking"),
            ("weekend", 2, "library",None,         "Reading"),
            ("weekend", 3, "home",   None,         "Private time"),
        ],
        "rio": [
            ("weekday", 0, "home",   None,         "Getting ready"),
            ("weekday", 1, "salon",  None,         "Styling clients"),
            ("weekday", 2, "salon",  None,         "Appointments"),
            ("weekday", 3, "home",   None,         "Relaxing"),
            ("weekend", 0, "home",   None,         "Sleeping in"),
            ("weekend", 1, "salon",  None,         "Weekend rush"),
            ("weekend", 2, "cafe",   None,         "Day off"),
            ("weekend", 3, "bar",    None,         "Night out"),
        ],
        "dana": [
            ("all",     0, "gym",    None,         "Morning training"),
            ("weekday", 1, "gym",    None,         "Client sessions"),
            ("weekday", 2, "park",   None,         "Outdoor training"),
            ("weekday", 3, "home",   None,         "Rest"),
            ("weekend", 1, "gym",    None,         "Weekend clients"),
            ("weekend", 2, "cafe",   None,         "Refuelling"),
            ("weekend", 3, "home",   None,         "Recovery"),
        ],
        "ines": [
            ("weekday", 0, "home",   None,         "Getting ready"),
            ("weekday", 1, "cafe",   None,         "Barista shift"),
            ("weekday", 2, "cafe",   None,         "Closing shift"),
            ("weekday", 3, "home",   None,         "Journaling"),
            ("weekend", 0, "home",   None,         "Sleeping in"),
            ("weekend", 1, "cafe",   None,         "Weekend shift"),
            ("weekend", 2, "park",   None,         "Wandering"),
            ("weekend", 3, "home",   None,         "Quiet night"),
        ],
        "vivienne": [
            ("weekday", 0, "park",   None,         "Outdoor yoga"),
            ("weekday", 1, "gym",    None,         "Teaching class"),
            ("weekday", 2, "home",   None,         "Meditation"),
            ("weekday", 3, "home",   None,         "Evening tea"),
            ("weekend", 0, "park",   None,         "Morning practice"),
            ("weekend", 1, "gym",    None,         "Weekend class"),
            ("weekend", 2, "cafe",   None,         "Relaxing"),
            ("weekend", 3, "home",   None,         "Quiet evening"),
        ],
        "camille": [
            ("weekday", 0, "home",   None,         "Getting ready"),
            ("weekday", 1, "office", None,         "At work"),
            ("weekday", 2, "office", None,         "Late hours"),
            ("weekday", 3, "home",   None,         "Decompressing"),
            ("weekend", 0, "home",   None,         "Sleeping in"),
            ("weekend", 1, "cafe",   None,         "Coffee and reading"),
            ("weekend", 2, "park",   None,         "Walking"),
            ("weekend", 3, "home",   None,         "Quiet night"),
        ],
        "hana": [
            ("weekday", 0, "home",   None,         "Morning routine"),
            ("weekday", 1, "library",None,         "Translating"),
            ("weekday", 2, "cafe",   None,         "Working remotely"),
            ("weekday", 3, "home",   None,         "Evening"),
            ("weekend", 0, "home",   None,         "Relaxing"),
            ("weekend", 1, "library",None,         "Personal reading"),
            ("weekend", 2, "park",   None,         "Quiet walk"),
            ("weekend", 3, "home",   None,         "Night in"),
        ],
        "dr_obi": [
            ("weekday", 0, "clinic", None,         "Morning rounds"),
            ("weekday", 1, "clinic", None,         "Seeing patients"),
            ("weekday", 2, "clinic", None,         "Late patients"),
            ("weekday", 3, "home",   None,         "Resting"),
            ("weekend", 0, "park",   None,         "Morning walk"),
            ("weekend", 1, "home",   None,         "Day off"),
            ("weekend", 2, "cafe",   None,         "Afternoon out"),
            ("weekend", 3, "home",   None,         "Quiet evening"),
        ],
    }

    def get_npc_location(npc_id, period=None, weekday=None):
        """Return (location, room, activity) for an NPC at the current time."""
        if period is None:
            period = store.time_period
        if weekday is None:
            weekday = store.time_weekday

        schedule = NPC_SCHEDULE.get(npc_id, [])
        is_weekend = weekday in (0, 6)

        best = None
        for (day_mask, sched_period, loc, room, activity) in schedule:
            if sched_period != period:
                continue
            if day_mask == "all":
                best = (loc, room, activity)
            elif day_mask == "weekday" and not is_weekend:
                best = (loc, room, activity)
            elif day_mask == "weekend" and is_weekend:
                best = (loc, room, activity)
        return best or ("home", None, "Around")

    def npcs_at_location(location, period=None, weekday=None):
        """Return list of NPC ids present at a location right now."""
        result = []
        for npc_id in NPC_SCHEDULE:
            loc, room, activity = get_npc_location(npc_id, period, weekday)
            if loc == location:
                result.append(npc_id)
        return result
