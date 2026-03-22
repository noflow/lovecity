# LoveCity — Ren'Py Sandbox VN
## Project Structure

```
lovecity_renpy/
└── game/
    ├── options.rpy          ← Game settings (name, resolution, etc.)
    ├── variables.rpy        ← All game state, stats, relationships, helper functions
    ├── characters.rpy       ← All 34 character definitions + NPC_DATA registry
    ├── locations.rpy        ← Locations, home rooms, NPC schedules, helper functions
    ├── screens.rpy          ← All UI: HUD, hub, travel, stats, diary, phone, etc.
    ├── sandbox.rpy          ← Core sandbox loop + all location actions
    ├── bg_colors.rpy        ← Background colour fallbacks + image declarations
    ├── gui.rpy              ← GUI styling (colours, fonts, dialogue box)
    ├── backgrounds/         ← Drop .webp/.jpg BG images here (1280×720px)
    │   └── bedroom.webp     ← Your existing bedroom image goes here
    └── story/
        ├── intro.rpy        ← Opening day: wake up, mom, sister, cora
        ├── alex.rpy         ← Alex Rivera arc (café barista)
        ├── dr_rivera.rpy    ← Dr. Rivera therapy arc (transformation hub)
        ├── maya_kai.rpy     ← Maya Chen + Kai Nakamura meet scenes
        └── luna.rpy         ← Luna Voss meet scene (night nurse)
```

## How To Run

1. Download Ren'Py from https://renpy.org
2. Open Ren'Py launcher
3. Click "Open Project" and navigate to the `lovecity_renpy/` folder
4. Click Launch Project

## Adding Backgrounds

Copy image files to `game/backgrounds/` named after room/location IDs:
- `bedroom.webp` (copy from your existing Vite project)
- `kitchen.jpg`
- `cafe.jpg`
- `park.jpg`
- etc.

Then in `bg_colors.rpy`, uncomment the matching `image bg_X = "backgrounds/X.webp"` line.

## Adding Character Sprites

Create `game/images/characters/<id>/` folders with:
- `neutral.png`  — default pose
- `happy.png`
- `sad.png`
- `surprised.png`
- `shy.png`
- `love.png`

In `characters.rpy`, add after the character define:
```
image alex neutral = "characters/alex/neutral.png"
image alex happy   = "characters/alex/happy.png"
```

Then in dialogue use: `show alex neutral` / `show alex happy`

## Sandbox Loop

The game runs in a loop:
1. Player sees current location + who's there
2. Player chooses: Talk to someone / Do an action / Travel / Wait
3. If talking → runs the character's dialogue label
4. If action → runs `action_<location>_<action_id>`
5. If travel → changes `current_location`, crossfades background
6. If wait → advances time period, triggers any scheduled events

## Time System

4 periods per day: Morning (0) → Afternoon (1) → Evening (2) → Night (3)
- `advance_time(1)` moves forward one period
- `is_weekend()` returns True on Sat/Sun
- NPCs have different schedules on weekdays vs weekends
- Use `get_npc_location("alex")` to find where Alex is right now

## Writing New Scenes

1. Open the relevant `story/<character>.rpy` file
2. Add a new label: `label talk_alex_date_park:`
3. Write the scene with standard Ren'Py dialogue syntax
4. At the end: `return` (or `jump sandbox_hub` to end cleanly)
5. Link to it from `talk_alex` or an event trigger in `sandbox.rpy`

## Character Relationships

- `add_rel("alex", 10)` — increase relationship by 10
- `get_rel("alex")` — get current relationship value
- `rel_label(get_rel("alex"))` — returns "Stranger" / "Friend" / etc.
- Relationships gate dialogue options and unlock new scenes

## Using the Story System

The LoveCity Story System HTML tool exports `.rpy` files.
Drop exported files into `game/story/` and they'll be loaded automatically.
