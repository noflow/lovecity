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
        # Extra locations
        "bg_realestate":   "#1e2535",
        "bg_apt_complex":  "#1a1a2e",
        "bg_townhomes":    "#1e2020",
        "bg_house_elm":    "#1a1e15",
        "bg_house_oak":    "#1e1a10",
        "bg_penthouse":    "#0a0a20",
        # Home rooms
        "bg_bedroom":    "#1a1230",
        "bg_kitchen":    "#251808",
        "bg_livingroom": "#1a1520",
        "bg_bathroom":   "#0a2030",
        "bg_garden":     "#1e350a",
        "bg_momsroom":   "#2e1a28",
        "bg_sisroom":    "#2e1040",
        # Default
        "bg_default":    "#0a0a1e",
    }

## ── IMAGE DECLARATIONS ──────────────────────────────────────────
## Each bg_X image tries the file first, falls back to a solid color.
## When you add a real image file, Ren'Py will use it automatically.

image bg_bedroom    = "backgrounds/bedroom.webp" if renpy.loadable("backgrounds/bedroom.webp") else Solid("#1a1230")
image bg_kitchen    = "backgrounds/kitchen.webp"    if renpy.loadable("backgrounds/kitchen.webp")    else "backgrounds/kitchen.jpg"    if renpy.loadable("backgrounds/kitchen.jpg")    else Solid("#251808")
image bg_livingroom = "backgrounds/livingroom.webp" if renpy.loadable("backgrounds/livingroom.webp") else "backgrounds/livingroom.jpg" if renpy.loadable("backgrounds/livingroom.jpg") else Solid("#1a1520")
image bg_bathroom   = "backgrounds/bathroom.webp"   if renpy.loadable("backgrounds/bathroom.webp")   else "backgrounds/bathroom.jpg"   if renpy.loadable("backgrounds/bathroom.jpg")   else Solid("#0a2030")
image bg_garden     = "backgrounds/garden.webp"     if renpy.loadable("backgrounds/garden.webp")     else "backgrounds/garden.jpg"     if renpy.loadable("backgrounds/garden.jpg")     else Solid("#1e350a")
image bg_home       = "backgrounds/home.webp"       if renpy.loadable("backgrounds/home.webp")       else "backgrounds/home.jpg"       if renpy.loadable("backgrounds/home.jpg")       else Solid("#1a1230")
image bg_school     = "backgrounds/school.webp"     if renpy.loadable("backgrounds/school.webp")     else "backgrounds/school.jpg"     if renpy.loadable("backgrounds/school.jpg")     else Solid("#0f1e35")
image bg_cafe       = "backgrounds/cafe.webp"       if renpy.loadable("backgrounds/cafe.webp")       else "backgrounds/cafe.jpg"       if renpy.loadable("backgrounds/cafe.jpg")       else Solid("#3b2010")
image bg_mall       = "backgrounds/mall.webp"       if renpy.loadable("backgrounds/mall.webp")       else "backgrounds/mall.jpg"       if renpy.loadable("backgrounds/mall.jpg")       else Solid("#3b1e5f")
image bg_park       = "backgrounds/park.webp"       if renpy.loadable("backgrounds/park.webp")       else "backgrounds/park.jpg"       if renpy.loadable("backgrounds/park.jpg")       else Solid("#0f2e1a")
image bg_clinic     = "backgrounds/clinic.webp"     if renpy.loadable("backgrounds/clinic.webp")     else "backgrounds/clinic.jpg"     if renpy.loadable("backgrounds/clinic.jpg")     else Solid("#1a2e3b")
image bg_gym        = "backgrounds/gym.webp"        if renpy.loadable("backgrounds/gym.webp")        else "backgrounds/gym.jpg"        if renpy.loadable("backgrounds/gym.jpg")        else Solid("#2e1a1a")
image bg_office     = "backgrounds/office.webp"     if renpy.loadable("backgrounds/office.webp")     else "backgrounds/office.jpg"     if renpy.loadable("backgrounds/office.jpg")     else Solid("#1a1e2e")
image bg_bar        = "backgrounds/bar.webp"        if renpy.loadable("backgrounds/bar.webp")        else "backgrounds/bar.jpg"        if renpy.loadable("backgrounds/bar.jpg")        else Solid("#1a0a2e")
image bg_library    = "backgrounds/library.webp"    if renpy.loadable("backgrounds/library.webp")    else "backgrounds/library.jpg"    if renpy.loadable("backgrounds/library.jpg")    else Solid("#2e1e0a")
image bg_salon      = "backgrounds/salon.webp"      if renpy.loadable("backgrounds/salon.webp")      else "backgrounds/salon.jpg"      if renpy.loadable("backgrounds/salon.jpg")      else Solid("#2e0a1e")
image bg_street     = "backgrounds/street.webp"     if renpy.loadable("backgrounds/street.webp")     else "backgrounds/street.jpg"     if renpy.loadable("backgrounds/street.jpg")     else Solid("#1a1a20")
image bg_momsroom   = "backgrounds/momsroom.webp"   if renpy.loadable("backgrounds/momsroom.webp")   else "backgrounds/momsroom.jpg"   if renpy.loadable("backgrounds/momsroom.jpg")   else Solid("#2e1a28")
image bg_sisroom    = "backgrounds/sisroom.webp"    if renpy.loadable("backgrounds/sisroom.webp")    else "backgrounds/sisroom.jpg"    if renpy.loadable("backgrounds/sisroom.jpg")    else Solid("#2e1040")
image bg_realestate = "backgrounds/realestate.webp" if renpy.loadable("backgrounds/realestate.webp") else "backgrounds/realestate.jpg" if renpy.loadable("backgrounds/realestate.jpg") else Solid("#1e2535")
image bg_apt_complex= "backgrounds/apt_complex.webp"if renpy.loadable("backgrounds/apt_complex.webp")else "backgrounds/apt_complex.jpg"if renpy.loadable("backgrounds/apt_complex.jpg")else Solid("#1a1a2e")
image bg_townhomes  = "backgrounds/townhomes.webp"  if renpy.loadable("backgrounds/townhomes.webp")  else "backgrounds/townhomes.jpg"  if renpy.loadable("backgrounds/townhomes.jpg")  else Solid("#1e2020")
image bg_house_elm  = "backgrounds/house_elm.webp"  if renpy.loadable("backgrounds/house_elm.webp")  else "backgrounds/house_elm.jpg"  if renpy.loadable("backgrounds/house_elm.jpg")  else Solid("#1a1e15")
image bg_house_oak  = "backgrounds/house_oak.webp"  if renpy.loadable("backgrounds/house_oak.webp")  else "backgrounds/house_oak.jpg"  if renpy.loadable("backgrounds/house_oak.jpg")  else Solid("#1e1a10")
image bg_penthouse  = "backgrounds/penthouse.webp"  if renpy.loadable("backgrounds/penthouse.webp")  else "backgrounds/penthouse.jpg"  if renpy.loadable("backgrounds/penthouse.jpg")  else Solid("#0a0a20")
