init python:
    # Fix for missing yesno_prompt method in Ren'Py 8.5.2
    # This addresses the AttributeError: 'Layout' object has no attribute 'yesno_prompt'
    
    if not hasattr(layout, 'yesno_prompt'):
        def yesno_prompt_fix(message, yes=None, no=None):
            """
            Fallback yesno_prompt implementation for layouts missing this method.
            Displays a simple yes/no prompt using renpy.call_screen.
            """
            # Handle None message
            if message is None:
                message = "Are you sure?"
            
            # Convert message to string if it's not already
            message = str(message)
            
            # Use a simple menu without caption
            choice = renpy.display_menu([
                ("Yes", True),
                ("No", False)
            ], screen="choice")
            
            return choice
        
        layout.yesno_prompt = yesno_prompt_fix
