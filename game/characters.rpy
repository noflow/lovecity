## characters.rpy — Character definitions for LoveCity
## ═══════════════════════════════════════════════════════════════
##
## Sprites go in:  images/characters/<id>/
##   neutral.png   happy.png   sad.png   angry.png
##   surprised.png shy.png     love.png  thinking.png
##
## To add a sprite:
##   Add image <id> neutral = "characters/<id>/neutral.png"
##   Then use: show alex neutral
## ═══════════════════════════════════════════════════════════════

# Narrator
define narrator = Character(None,
    what_italic = True,
    what_color  = "#c0c0c0")

# Inner monologue (player thinking)
define mc = Character("[player_name]",
    color         = "#a78bfa",
    what_color    = "#e2d9f3",
    who_suffix    = " (you)",
    kind          = nvl if False else adv)

define thought = Character(None,
    what_italic   = True,
    what_color    = "#94a3b8",
    what_prefix   = "[ ",
    what_suffix   = " ]")

# ── FAMILY ──────────────────────────────────────────────────────
define mom = Character("Sarah (Mom)",
    color       = "#f59e0b",
    who_bold    = True)

define sister = Character("Emma",
    color       = "#ec4899",
    who_bold    = True)

# ── FEMALE CHARACTERS ───────────────────────────────────────────
define alex = Character("Alex Rivera",
    color       = "#f59e0b",
    who_bold    = True)

define maya = Character("Maya Chen",
    color       = "#ec4899",
    who_bold    = True)

define kai = Character("Kai Nakamura",
    color       = "#3b82f6",
    who_bold    = True)

define luna = Character("Luna Voss",
    color       = "#8b5cf6",
    who_bold    = True)

define sera = Character("Sera Blum",
    color       = "#f43f5e",
    who_bold    = True)

define nadia = Character("Nadia Osman",
    color       = "#38bdf8",
    who_bold    = True)

define simone = Character("Simone Dubois",
    color       = "#f472b6",
    who_bold    = True)

define dr_rivera = Character("Dr. Elena Rivera",
    color       = "#c084fc",
    who_bold    = True)

define cora = Character("Cora Finch",
    color       = "#eab308",
    who_bold    = True)

define petra = Character("Petra Novak",
    color       = "#be185d",
    who_bold    = True)

define vivienne = Character("Vivienne Marsh",
    color       = "#059669",
    who_bold    = True)

define camille = Character("Camille Ford",
    color       = "#1d4ed8",
    who_bold    = True)

define hana = Character("Hana Ishida",
    color       = "#0d9488",
    who_bold    = True)

define dom = Character("Dominique Reyes",
    color       = "#f97316",
    who_bold    = True)

define reo = Character("Reo Tanaka",
    color       = "#34d399",
    who_bold    = True)

define august = Character("August Wren",
    color       = "#92400e",
    who_bold    = True)

define arlo = Character("Arlo Kim",
    color       = "#16a34a",
    who_bold    = True)

define eli = Character("Eli Strand",
    color       = "#7c3aed",
    who_bold    = True)

define milo = Character("Milo Park",
    color       = "#06b6d4",
    who_bold    = True)

define oz = Character("Oz Brennan",
    color       = "#f59e0b",
    who_bold    = True)

# ── TRANS MTF CHARACTERS ────────────────────────────────────────
define zane = Character("Zane Okafor",
    color       = "#10b981",
    who_bold    = True)

define river = Character("River Thorne",
    color       = "#a78bfa",
    who_bold    = True)

define sasha = Character("Sasha Bell",
    color       = "#d946ef",
    who_bold    = True)

define vesper = Character("Vesper Lane",
    color       = "#6366f1",
    who_bold    = True)

define rio = Character("Rio Santos",
    color       = "#ec4899",
    who_bold    = True)

define ronnie = Character("Ronnie Vega",
    color       = "#7c3aed",
    who_bold    = True)

define dana = Character("Dana Cross",
    color       = "#dc2626",
    who_bold    = True)

define ines = Character("Ines Cavalho",
    color       = "#a16207",
    who_bold    = True)

define jamie = Character("Jamie Reeves",
    color       = "#f97316",
    who_bold    = True)

# ── MALE CHARACTERS (only 3) ────────────────────────────────────
define prof_harlow = Character("Professor Harlow",
    color       = "#64748b",
    who_bold    = True)

define dr_obi = Character("Dr. Marcus Obi",
    color       = "#0891b2",
    who_bold    = True)

define theo = Character("Theo Walsh",
    color       = "#78716c",
    who_bold    = True)

# ── NPC DATA REGISTRY ────────────────────────────────────────────
# Used by sandbox hub screen to show character info
init python:
    NPC_DATA = {
        "mom":        {"name": "Sarah (Mom)",       "age": 45, "job": "Office Administrator",  "gender": "female",    "traits": "warm · perceptive · strong"},
        "sister":     {"name": "Emma",              "age": 19, "job": "University Student",    "gender": "female",    "traits": "ambitious · dramatic · loyal"},
        "alex":       {"name": "Alex Rivera",       "age": 20, "job": "Barista",               "gender": "female",    "traits": "warm · creative · restless"},
        "maya":       {"name": "Maya Chen",         "age": 19, "job": "Student/Cheerleader",   "gender": "female",    "traits": "bright · competitive · guarded"},
        "kai":        {"name": "Kai Nakamura",      "age": 22, "job": "Personal Trainer",      "gender": "female",    "traits": "focused · intense · private"},
        "luna":       {"name": "Luna Voss",         "age": 24, "job": "Nurse",                 "gender": "female",    "traits": "calm · perceptive · tender"},
        "sera":       {"name": "Sera Blum",         "age": 19, "job": "Student/Cheerleader",   "gender": "female",    "traits": "quiet · thoughtful · surprising"},
        "nadia":      {"name": "Nadia Osman",       "age": 22, "job": "Law Student",           "gender": "female",    "traits": "driven · sharp · longing"},
        "simone":     {"name": "Simone Dubois",     "age": 25, "job": "Fashion Blogger",       "gender": "female",    "traits": "glamorous · fragile · real"},
        "dr_rivera":  {"name": "Dr. Elena Rivera",  "age": 34, "job": "Therapist",             "gender": "female",    "traits": "composed · empathic · complex"},
        "cora":       {"name": "Cora Finch",        "age": 28, "job": "Florist",               "gender": "female",    "traits": "warm · nosy · loyal"},
        "petra":      {"name": "Petra Novak",       "age": 31, "job": "Boutique Owner",        "gender": "female",    "traits": "elegant · exacting · playful"},
        "vivienne":   {"name": "Vivienne Marsh",    "age": 33, "job": "Yoga Instructor",       "gender": "female",    "traits": "serene · direct · observant"},
        "camille":    {"name": "Camille Ford",      "age": 41, "job": "Office Manager",        "gender": "female",    "traits": "professional · wry · vulnerable"},
        "hana":       {"name": "Hana Ishida",       "age": 27, "job": "Translator",            "gender": "female",    "traits": "gentle · precise · guarded"},
        "dom":        {"name": "Dominique Reyes",   "age": 26, "job": "Head Chef",             "gender": "female",    "traits": "intense · warm · devoted"},
        "reo":        {"name": "Reo Tanaka",        "age": 23, "job": "Paramedic",             "gender": "female",    "traits": "funny · grounded · hurting"},
        "august":     {"name": "August Wren",       "age": 40, "job": "Senior Librarian",      "gender": "female",    "traits": "patient · old-world · modern"},
        "arlo":       {"name": "Arlo Kim",          "age": 20, "job": "Street Artist",         "gender": "female",    "traits": "free · impulsive · centred"},
        "eli":        {"name": "Eli Strand",        "age": 25, "job": "Session Musician",      "gender": "female",    "traits": "nocturnal · creative · lonely"},
        "milo":       {"name": "Milo Park",         "age": 21, "job": "Freelance Developer",   "gender": "female",    "traits": "nerdy · funny · perceptive"},
        "oz":         {"name": "Oz Brennan",        "age": 29, "job": "Food Truck Owner",      "gender": "female",    "traits": "chaotic · generous · deep"},
        "zane":       {"name": "Zane Okafor",       "age": 23, "job": "DJ",                    "gender": "trans_mtf", "traits": "charismatic · restless · feeling"},
        "river":      {"name": "River Thorne",      "age": 21, "job": "Tattoo Artist",         "gender": "trans_mtf", "traits": "fierce · guarded · loyal"},
        "sasha":      {"name": "Sasha Bell",        "age": 23, "job": "Club Promoter",         "gender": "trans_mtf", "traits": "vivid · restless · hard to read"},
        "vesper":     {"name": "Vesper Lane",       "age": 26, "job": "Unknown",               "gender": "trans_mtf", "traits": "enigmatic · intelligent · watchful"},
        "rio":        {"name": "Rio Santos",        "age": 24, "job": "Hair Stylist",          "gender": "trans_mtf", "traits": "expressive · boundary-pushing · wise"},
        "ronnie":     {"name": "Ronnie Vega",       "age": 38, "job": "Bar Owner",             "gender": "trans_mtf", "traits": "magnetic · mysterious · morally grey"},
        "dana":       {"name": "Dana Cross",        "age": 26, "job": "Personal Trainer",      "gender": "trans_mtf", "traits": "intense · straightforward · warm"},
        "ines":       {"name": "Ines Cavalho",      "age": 24, "job": "Barista",               "gender": "trans_mtf", "traits": "opinionated · passionate · complicated"},
        "jamie":      {"name": "Jamie Reeves",      "age": 19, "job": "Student/Cheerleader",   "gender": "trans_mtf", "traits": "sharp · competitive · secretly kind"},
        "prof_harlow":{"name": "Professor Harlow",  "age": 48, "job": "Professor",             "gender": "male",      "traits": "brilliant · dry · encouraging"},
        "dr_obi":     {"name": "Dr. Marcus Obi",    "age": 42, "job": "Doctor",                "gender": "male",      "traits": "calm · honest · carrying something heavy"},
        "theo":       {"name": "Theo Walsh",        "age": 22, "job": "Student",               "gender": "male",      "traits": "quiet · reliable · slow to open up"},
    }
