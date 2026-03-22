## bg_colors.rpy — Fallback solid colours per location
## Used by set_background when no image file is found
## ═══════════════════════════════════════════════════════════════

init python:
    bg_colors = {
        # Locations
        "bg_home":       "#1a1230",
        "bg_school":     "#0f1e35",
        "bg_cafe":       "#3b2010",
        "bg_mall":       "#3b1e5f",
        "bg_park":       "#0f2e1a",
        "bg_clinic":     "#1a2e3b",
        "bg_gym":        "#2e1a1a",
        "bg_office":     "#1a1e2e",
        "bg_bar":        "#1a0a2e",
        "bg_library":    "#2e1e0a",
        "bg_salon":      "#2e0a1e",
        "bg_street":     "#1a1a20",
        # Home rooms
        "bg_bedroom":    "#1a1230",
        "bg_kitchen":    "#251808",
        "bg_livingroom": "#1a1520",
        "bg_bathroom":   "#0a2030",
        "bg_garden":     "#1e350a",
        # Default
        "bg_default":    "#0a0a1e",
    }

## ── IMAGE DECLARATIONS ──────────────────────────────────────────
## Once you have real background images, uncomment and adjust paths.
## Images should be 1280x720px, placed in game/backgrounds/

image bg_bedroom    = "backgrounds/bedroom.webp"
# image bg_kitchen    = "backgrounds/kitchen.jpg"
# image bg_livingroom = "backgrounds/livingroom.jpg"
# image bg_cafe       = "backgrounds/cafe.jpg"
# image bg_park       = "backgrounds/park.jpg"
# image bg_school     = "backgrounds/school.jpg"
# image bg_clinic     = "backgrounds/clinic.jpg"
# image bg_gym        = "backgrounds/gym.jpg"
# image bg_bar        = "backgrounds/bar.jpg"
# image bg_library    = "backgrounds/library.jpg"
# image bg_mall       = "backgrounds/mall.jpg"
# image bg_salon      = "backgrounds/salon.jpg"
# image bg_street     = "backgrounds/street.jpg"
# image bg_home       = "backgrounds/home.jpg"
# image bg_office     = "backgrounds/office.jpg"
# image bg_garden     = "backgrounds/garden.jpg"
# image bg_bathroom   = "backgrounds/bathroom.jpg"

## ── ADDING EXISTING BEDROOM IMAGE ───────────────────────────────
## You already have bedroom.webp from the Vite project.
## Copy it to: game/backgrounds/bedroom.webp
## Then uncomment the bg_bedroom line above.
