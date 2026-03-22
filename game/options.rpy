## options.rpy — LoveCity Game Settings

define config.name = "LoveCity"
define config.version = "0.1.0"
define config.save_directory = "LoveCity-0.1"

## Screen size — 16:9 widescreen standard for VN
define config.screen_width  = 1280
define config.screen_height = 720

## Framerate
define config.framerate = 60

## Transitions
define config.enter_transition  = dissolve
define config.exit_transition   = dissolve
define config.after_load_transition = dissolve

## Skip
define config.skip_unseen_screens = False
define config.fast_skipping = True

## Auto-forward
define preferences.afm_time = 7
define preferences.afm_enable = False

## Audio channels
define config.has_music    = True
define config.has_sound    = True
define config.has_voice    = False

## Main menu music (placeholder)
# define config.main_menu_music = "audio/menu_theme.ogg"

## Log
define config.log_enable = False
