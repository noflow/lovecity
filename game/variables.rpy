## variables.rpy — All persistent game state
## ═══════════════════════════════════════════════════════════════

# ── PLAYER ──────────────────────────────────────────────────────
default player_name    = "Player"
default player_age     = 18

# ── CORE STATS ──────────────────────────────────────────────────
default stat_money       = 1000
default stat_energy      = 100
default stat_happiness   = 50
default stat_intelligence= 20
default stat_charm       = 20
default stat_fitness     = 20

# ── PROGRESSION STATS ───────────────────────────────────────────
default stat_trust       = 0     # Trust built with Dr. Rivera / therapy
default stat_confidence  = 50    # Self-confidence
default stat_acceptance  = 0     # Acceptance of changes
default stat_curiosity   = 20    # Willingness to explore

# ── BODY STATS ──────────────────────────────────────────────────
default body_femininity  = 0
default body_bust        = 0
default body_hips        = 0
default body_muscle      = 20
default body_hair        = 20

# ── EMOTIONAL STATS ─────────────────────────────────────────────
default stat_love        = 0
default stat_lust        = 0
default stat_arousal     = 0
default stat_corruption  = 0

# ── APPEARANCE / PRESENTATION ───────────────────────────────────
default appearance_makeup     = 0     # 0-100 scale
default appearance_clothing   = 0     # 0-100 scale
default stat_public_presentation = 0  # How "out" the player is publicly
default stat_social_acceptance   = 0  # Community acceptance level

# ── TRANSFORMATION STAGE ────────────────────────────────────────
default transformation_stage  = 0     # 0=Pre, 1=Early, 2=Mid, 3=Advanced, 4=Complete
default hrt_started           = False
default hrt_day               = 0     # Days since starting HRT

# ── TIME SYSTEM ─────────────────────────────────────────────────
# Period: 0=Morning 1=Afternoon 2=Evening 3=Night
default time_day         = 1
default time_period      = 0    # 0=Morning 1=Afternoon 2=Evening 3=Night
default time_period_names = ["Morning", "Afternoon", "Evening", "Night"]
default time_period_icons = ["☀️", "🌤️", "🌇", "🌙"]

# Days of the week
default time_weekday     = 1    # 0=Sun 1=Mon ... 6=Sat
default time_weekday_names = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

# ── CURRENT LOCATION ────────────────────────────────────────────
default current_location = "home"
default current_room     = "bedroom"

# ── RELATIONSHIPS (0–200) ────────────────────────────────────────
default rel_mom         = 80
default rel_sister      = 60
default rel_alex        = 0
default rel_maya        = 0
default rel_kai         = 0
default rel_luna        = 0
default rel_zane        = 0
default rel_sera        = 0
default rel_river       = 0
default rel_dom         = 0
default rel_nadia       = 0
default rel_simone      = 0
default rel_reo         = 0
default rel_dr_rivera   = 0
default rel_jamie       = 0
default rel_prof_harlow = 0
default rel_cora        = 0
default rel_theo        = 0
default rel_milo        = 0
default rel_ines        = 0
default rel_dana        = 0
default rel_ronnie      = 0
default rel_sasha       = 0
default rel_petra       = 0
default rel_august      = 0
default rel_dr_obi      = 0
default rel_arlo        = 0
default rel_vivienne    = 0
default rel_camille     = 0
default rel_eli         = 0
default rel_hana        = 0
default rel_rio         = 0
default rel_oz          = 0
default rel_vesper      = 0

# ── NPC LOVE / LUST (per character) ─────────────────────────────
default npc_love        = {}
default npc_lust        = {}
default npc_arousal     = {}
default npc_corruption  = {}
default dating          = {}    # dating[npc_id] = True/False

# ── STORY FLAGS ──────────────────────────────────────────────────
default flag_intro_done          = False
default flag_met_mom             = False
default flag_met_sister          = False
default flag_met_alex            = False
default flag_met_maya            = False
default flag_met_kai             = False
default flag_met_luna            = False
default flag_met_dr_rivera       = False
default flag_met_cora            = False
default flag_met_theo            = False
default flag_met_sera            = False
default flag_met_nadia           = False
default flag_met_simone          = False
default flag_met_zane            = False
default flag_met_ronnie          = False
default flag_met_river           = False
default flag_met_sasha           = False
default flag_met_petra           = False
default flag_met_dom             = False
default flag_met_reo             = False
default flag_met_jamie           = False
default flag_met_august          = False
default flag_met_prof_harlow     = False
default flag_met_dr_obi          = False
default flag_therapy_started     = False
default flag_first_day_done      = False

# ── INVENTORY ────────────────────────────────────────────────────
default inventory = []

# ── DIARY / LOG ──────────────────────────────────────────────────
default diary = []

# ── HELPER FUNCTIONS ────────────────────────────────────────────
init python:

    ## Screen action wrappers — work in ALL contexts (call screen, use, etc.)
    ## Use these instead of ShowScreen/HideScreen/ShowMenu/MainMenu in action=
    def lc_show_screen(name): renpy.show_screen(name)
    def lc_hide_screen(name): renpy.hide_screen(name)
    def lc_show_menu(name):   renpy.show_screen(name)
    def lc_main_menu():       renpy.full_restart()

    def lc_show_phone():
        """Show the phone — ensures data initialised, calls phone_start() then shows screen."""
        if not hasattr(store, "reset_phone_data"):
            return  # phone.rpy not installed
        if not store.phone_channel_data:
            store.reset_phone_data()
        store.phone_start()
        renpy.show_screen("phone_ui")

    def lc_hide_phone():
        """Hide the phone."""
        if hasattr(store, "reset_phone_data"):
            renpy.hide_screen("phone_ui")
            store.phone_end()

    def add_rel(char_id, amount):
        """Adjust a relationship value, clamped 0-200."""
        var = "rel_" + char_id
        current = getattr(store, var, 0)
        setattr(store, var, max(0, min(200, current + amount)))

    def get_rel(char_id):
        return getattr(store, "rel_" + char_id, 0)

    def rel_label(pts):
        if pts < 10:   return "Stranger"
        if pts < 30:   return "Acquaintance"
        if pts < 60:   return "Friend"
        if pts < 100:  return "Close Friend"
        if pts < 150:  return "Crush"
        return "Partner"

    def add_stat(stat_name, amount, min_val=0, max_val=100):
        """Adjust any stat, clamped."""
        var = "stat_" + stat_name
        current = getattr(store, var, 0)
        setattr(store, var, max(min_val, min(max_val, current + amount)))

    def advance_time(periods=1):
        """Advance time by N periods. Wraps day."""
        global time_period, time_day, time_weekday
        store.time_period += periods
        while store.time_period >= 4:
            store.time_period -= 4
            store.time_day    += 1
            store.time_weekday = (store.time_weekday + 1) % 7

    def is_weekend():
        return store.time_weekday in (0, 6)

    def time_str():
        p = store.time_period
        names = ["Morning", "Afternoon", "Evening", "Night"]
        icons = ["☀️", "🌤️", "🌇", "🌙"]
        return icons[p] + " " + names[p]

    def add_diary(entry):
        store.diary.append({"day": store.time_day, "period": store.time_period, "text": entry})

    def has_item(item_id):
        return item_id in store.inventory

    def add_item(item_id):
        if item_id not in store.inventory:
            store.inventory.append(item_id)

    def remove_item(item_id):
        if item_id in store.inventory:
            store.inventory.remove(item_id)
