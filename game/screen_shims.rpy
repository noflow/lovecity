## screen_shims.rpy
## Makes screen actions available as Python-callable functions.
## Needed because 'action ShowScreen(x)' in multiline textbutton blocks
## still evaluates ShowScreen as Python, not screen language.

init python:
    def _show_screen(name, *args, **kwargs):
        renpy.show_screen(name, *args, **kwargs)

    def _hide_screen(name):
        renpy.hide_screen(name)

    def _show_menu(name):
        renpy.show_screen(name)
