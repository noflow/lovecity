## gui.rpy — LoveCity GUI configuration
## ═══════════════════════════════════════════════════════════════

## Basic colours
define gui.accent_color            = "#f472b6"
define gui.idle_color              = "#94a3b8"
define gui.idle_small_color        = "#64748b"
define gui.hover_color             = "#f472b6"
define gui.selected_color          = "#e2e8f0"
define gui.insensitive_color       = "#334155"
define gui.muted_color             = "#1e293b"
define gui.hover_muted_color       = "#334155"

## Text colours
define gui.text_color              = "#e2e8f0"
define gui.interface_text_color    = "#94a3b8"

## Fonts (use built-in if custom fonts not available)
define gui.default_font            = "gui/fonts/Aller_Rg.ttf"
define gui.interface_font          = "gui/fonts/Aller_Rg.ttf"
define gui.glyph_font              = "DejaVuSans.ttf"

define gui.text_size               = 22
define gui.name_text_size          = 24
define gui.interface_text_size     = 22
define gui.label_text_size         = 24
define gui.notify_text_size        = 18

## Dialogue box
define gui.textbox_height          = 185
define gui.textbox_yalign          = 1.0

define gui.namebox_width           = None
define gui.namebox_height          = None
define gui.namebox_borders         = Borders(5, 5, 5, 5)
define gui.namebox_tile            = False

## Dialogue text position (inside blue body area)
define gui.text_xpos               = 30
define gui.text_ypos               = 40
define gui.text_xsize              = 700
define gui.text_width              = 700
define gui.text_ysize              = 130
define gui.text_xalign             = 0.0

## Character name position (inside white top bar)
define gui.name_xpos               = 30
define gui.name_ypos               = 5

## Choice buttons
define gui.choice_button_width         = 790
define gui.choice_button_height        = None
define gui.choice_button_tile          = False
define gui.choice_button_borders       = Borders(150, 5, 150, 5)
define gui.choice_button_text_font     = gui.interface_font
define gui.choice_button_text_size     = 22
define gui.choice_button_text_xalign   = 0.5

define gui.choice_button_text_idle_color       = "#94a3b8"
define gui.choice_button_text_hover_color      = "#f472b6"
define gui.choice_button_text_selected_color   = "#e2e8f0"
define gui.choice_button_text_insensitive_color= "#334155"

## Colours continued
define gui.choice_text_size            = 22

## Bars
define gui.bar_size         = 36
define gui.scrollbar_size   = 12
define gui.slider_size      = 36

define gui.bar_tile         = False
define gui.scrollbar_tile   = False
define gui.slider_tile      = False

define gui.bar_borders         = Borders(6, 6, 6, 6)
define gui.scrollbar_borders   = Borders(6, 6, 6, 6)
define gui.slider_borders      = Borders(6, 6, 6, 6)

## Frame
define gui.frame_borders   = Borders(6, 6, 6, 6)
define gui.frame_tile      = False

## Confirm
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)

## History screen
define gui.history_height           = None
define gui.history_spacing          = 0
define gui.history_text_size        = 22
define gui.history_name_xpos        = 214
define gui.history_name_ypos        = 0
define gui.history_name_width       = None
define gui.history_name_xalign      = 1.0
define gui.history_text_xpos        = 264
define gui.history_text_ypos        = 4
define gui.history_text_width       = 750
define gui.history_text_xalign      = 0.0

## Notify
define gui.notify_ypos = 68

## Skip
define gui.skip_ypos  = 15

## Dialogue box background
## Uncomment and replace with your actual file when ready:
# define gui.textbox_background = "gui/textbox.png"
