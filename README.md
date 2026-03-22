# LoveCity — Ren'Py Sandbox VN

## Project Structure

```
lovecity/
├── .gitignore
├── README.md
└── game/
    ├── options.rpy          ← Game settings (name, resolution, etc.)
    ├── variables.rpy        ← All game state, stats, relationships, helper functions
    ├── characters.rpy       ← All 34 character defines + NPC_DATA registry
    ├── locations.rpy        ← Locations, home rooms, NPC schedules, helper functions
    ├── screens.rpy          ← All UI: stats, diary, relationships, pause menu
    ├── map_screen.rpy       ← Clickable city map (Summertime Saga style)
    ├── location_hub.rpy     ← In-location hub (characters + actions panel)
    ├── sandbox.rpy          ← Core sandbox loop + all location actions
    ├── bg_colors.rpy        ← BG colour fallbacks + image declarations
    ├── gui.rpy              ← GUI styling (colours, fonts, dialogue box)
    ├── backgrounds/         ← Drop .webp/.jpg BG images here (1280×720px)
    │   └── bedroom.webp     ← First room background (included)
    └── story/
        ├── intro.rpy        ← Opening day: wake up, mom, sister, cora
        ├── alex.rpy         ← Alex Rivera arc (café barista)
        ├── dr_rivera.rpy    ← Dr. Rivera therapy arc
        ├── maya_kai.rpy     ← Maya Chen + Kai Nakamura meet scenes
        └── luna.rpy         ← Luna Voss meet scene (night nurse)
```

---

## Git Workflow

### Clone and run:
```bash
git clone https://github.com/noflow/lovecity.git
```
Open the cloned folder in the Ren'Py launcher → Launch Project.

### After writing new scenes in the Story System tool:
```bash
git pull origin main
# drop exported .rpy files into game/story/
git add -A
git commit -m "add scenes: describe what changed"
git push origin main
```

---

## How To Run

1. Download Ren'Py: https://renpy.org
2. Ren'Py launcher → **Open Project** → select the `lovecity/` folder
3. **Launch Project**

---

## Navigation (Clickable Map)

City map fills the screen. Click a location to enter it. Each button shows:
- Icon + name, NPCs currently present (pink dots), closed state
- Home → room picker (bedroom / kitchen / living room / bathroom / garden)

Bottom bar: ⏭️ Wait · 📊 Stats · 📓 Diary · 💕 Relationships

---

## Time System

4 periods: ☀️ Morning → 🌤️ Afternoon → 🌇 Evening → 🌙 Night

```python
advance_time(1)       # move forward one period
is_weekend()          # True on Sat/Sun
get_npc_location("alex")  # → (loc, room, activity)
```

---

## Adding Backgrounds

Drop 1280×720px images into `game/backgrounds/` then uncomment in `bg_colors.rpy`:
```renpy
image bg_cafe = "backgrounds/cafe.webp"
```

---

## Adding Character Sprites

```
game/images/characters/<id>/neutral.png
game/images/characters/<id>/happy.png
...
```

In `characters.rpy`:
```renpy
image alex neutral = "characters/alex/neutral.png"
```

In dialogue:
```renpy
show alex happy at center with dissolve
```

---

## Writing Scenes

Use the **Story System** HTML tool → Export → Ren'Py → drop into `game/story/`.

Or write directly:
```renpy
label talk_alex_coffee:
    show alex happy at center with dissolve
    alex "The usual?"
    $ add_rel("alex", 5)
    hide alex with dissolve
    return
```

---

## Key Helper Functions

```python
add_rel("alex", 10)          # relationship +10
get_rel("alex")              # current value 0-200
rel_label(get_rel("alex"))   # "Stranger" / "Friend" / "Crush" / "Partner"
add_stat("happiness", 10)    # stat +10 (clamped 0-100)
advance_time(1)              # next time period
add_diary("entry text")      # write to player diary
add_item("rose")             # add to inventory
has_item("rose")             # check inventory
```
