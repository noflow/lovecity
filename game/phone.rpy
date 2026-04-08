## -----------------------------------------------------
## Licensed under MIT (provided below) with Additional Clause(s)
## -----------------------------------------------------
## Copyright (c) 2025 Zoey (KleineLuka) 
##
## Permission is hereby granted, free of charge, to any person obtaining a copy
## of this software and associated documentation files (the “Software”), to deal
## in the Software without restriction, including without limitation the rights
## to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
## copies of the Software, and to permit persons to whom the Software is
## furnished to do so, subject to the following conditions:
##
## The above copyright notice and this permission notice shall be included in
## all copies or substantial portions of the Software.
##
## THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
## AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
## OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
## SOFTWARE.
## -----------------------------------------------------
## Additional Transformative-Works Clause:
## This asset is intended primarily for use as part of larger, *transformative* works,
## such as games, visual novels, or creative tools. You may not redistribute, re-host, or 
## re-sell the raw source code or assets by themselves, whether modified or unmodified.
## Use in original works (such as completed games or interactive media) is welcomed 
## and encouraged — provided appropriate credit is given.
##
## Additional Attribution & Notice Clause:
## You must retain:
## - All original comments in the code, including license information
## - Any links to the creator (Zoey / KleineLuka) or this project
## - Any included watermarks, embedded credits, or attribution mentions
## A visible credit in your project (README, in-game credits, etc.) is required
## -----------------------------------------------------

## -----------------------------------------------------
## Where to find me, and this project! And more of my projects!
## -----------------------------------------------------
## Website: https://luka.moe
## Contacts: https://luka.moe/socials
## Discord: kleineluka
## Email: lukazoeysong@gmail.com
## Gumroad: https://kleineluka.gumroad.com
## Itch: https://kleineluka.itch.io/
## -----------------------------------------------------

## -----------------------------------------------------
## Phone Program Python
## -----------------------------------------------------
default phone_mode = False
init -1 python:
    import re

    # configurable variables for easy plug-and-play
    phone_config = {
        # Sound Configuration
        "play_sound_send": True,
        "play_sound_receive": True,
        "no_sound_current_chat": False, # For incoming messages, only play if not viewing the chat
        # String Configurations
        "preview_no_message": "Empty chat...",
        "channels_title": "Messages",
        "history_timestamp_prefix": "Time:",
        "phone_player_name": "Me",
        "group_added": "{adder} added {participant} to the group.",
        "group_joined": "{participant} joined the group.",
        "group_left": "{participant} left the group.",
        # UI Configurations
        "message_font_size": 22,
        "choice_font_size": 22,
        "timestamp_font_size": 18,
        "auto_scroll": True,
        "show_sender_in_preview": True,
        "default_icon": "gui/phone/icon.png",
        "user_colour": "#FFFFFF",
        "character_colour": "#000000",
        "timestamp_colour": "#000000",
        "sort_channels_by_latest": True,
        "message_padding": 0.025,
        "preview_max_length": 25,
        "emojis": {
            "size": 32,
        },
        "phone_theme": "dark",  # LoveCity uses dark mode
        "light": {
            # colours for light mode
            "message_player_text_colour": "#FFFFFF",
            "message_character_text_colour": "#000000",
            "timestamp_text_colour": "#000000",
            "header_text_colour": "#000000",
            "channel_name_text_colour": "#000000",
            "channel_preview_text_colour": "#555555",
            "sender_name_text_colour": "#666666",
            "channel_divider_colour": "#E0E0E0",
            "channel_button_hover_background": "#EFEFEF",
            "empty_channel_text_colour": "#000000",
            # images for light mode
            "screen_background_image": "gui/phone/screen.png",
            "header_background_image": "gui/phone/header.png",
            "base_background_image": "gui/phone/base.png",
            "back_button_idle_image": "gui/phone/back.png",
            "back_button_notif_image": "gui/phone/back_notif.png",
            "notification_dot_image": "gui/phone/notif.png",
            "player_bubble_image": "gui/phone/player_bubble.png",
            "player_bubble_hover_image": "gui/phone/player_bubble_hover.png",
            "character_bubble_image": "gui/phone/character_bubble.png",
            "home_button_image": "gui/phone/home.png",
        },
        "dark": {
            # LoveCity dark mode — pink/purple player, slate character
            "message_player_text_colour": "#FFFFFF",
            "message_character_text_colour": "#E2E8F0",
            "timestamp_text_colour": "#64748b",
            "header_text_colour": "#F472B6",
            "channel_name_text_colour": "#E2E8F0",
            "channel_preview_text_colour": "#94A3B8",
            "sender_name_text_colour": "#F472B6",
            "channel_divider_colour": "#1E293B",
            "channel_button_hover_background": "#1E293B",
            "empty_channel_text_colour": "#94A3B8",
            # dark mode images — layered as backgrounds (screen → header → base)
            "screen_background_image": "gui/phone/skins/dark_mode/screen.png",
            "header_background_image": "gui/phone/skins/dark_mode/header.png",
            "base_background_image": "gui/phone/skins/dark_mode/base.png",
            "back_button_idle_image": "gui/phone/skins/dark_mode/back.png",
            "back_button_notif_image": "gui/phone/skins/dark_mode/back_notif.png",
            "notification_dot_image": "gui/phone/skins/dark_mode/notif.png",
            "player_bubble_image": "gui/phone/skins/dark_mode/player_bubble.png",
            "player_bubble_hover_image": "gui/phone/skins/dark_mode/player_bubble_hover.png",
            "character_bubble_image": "gui/phone/skins/dark_mode/character_bubble.png",
            "home_button_image": "gui/phone/skins/dark_mode/home.png",
        },
        "flip": {
            # colours for flip phone mode
            "message_player_text_colour": "#FFFFFF",
            "message_character_text_colour": "#000000",
            "timestamp_text_colour": "#000000",
            "header_text_colour": "#000000",
            "channel_name_text_colour": "#000000",
            "channel_preview_text_colour": "#555555",
            "sender_name_text_colour": "#666666",
            "channel_divider_colour": "#E0E0E0",
            "channel_button_hover_background": "#EFEFEF",
            "empty_channel_text_colour": "#000000",
            # images for flip phone mode
            "screen_background_image": "gui/phone/skins/flip_phone/screen.png",
            "header_background_image": "gui/phone/header.png",
            "base_background_image": "gui/phone/skins/flip_phone/base.png",
            "back_button_idle_image": "gui/phone/back.png",
            "back_button_notif_image": "gui/phone/back_notif.png",
            "notification_dot_image": "gui/phone/notif.png",
            "player_bubble_image": "gui/phone/player_bubble.png",
            "player_bubble_hover_image": "gui/phone/player_bubble_hover.png",
            "character_bubble_image": "gui/phone/character_bubble.png",
            "home_button_image": "gui/phone/home.png",
        },
        "status_bar": {
            # colours for status bar phone mode
            "message_player_text_colour": "#FFFFFF",
            "message_character_text_colour": "#000000",
            "timestamp_text_colour": "#000000",
            "header_text_colour": "#000000",
            "channel_name_text_colour": "#000000",
            "channel_preview_text_colour": "#555555",
            "sender_name_text_colour": "#666666",
            "channel_divider_colour": "#E0E0E0",
            "channel_button_hover_background": "#EFEFEF",
            "empty_channel_text_colour": "#000000",
            # images for status bar phone mode
            "screen_background_image": "gui/phone/screen.png",
            "header_background_image": "gui/phone/skins/status_bar/header.png",
            "base_background_image": "gui/phone/base.png",
            "back_button_idle_image": "gui/phone/back.png",
            "back_button_notif_image": "gui/phone/back_notif.png",
            "notification_dot_image": "gui/phone/notif.png",
            "player_bubble_image": "gui/phone/player_bubble.png",
            "player_bubble_hover_image": "gui/phone/player_bubble_hover.png",
            "character_bubble_image": "gui/phone/character_bubble.png",
            "home_button_image": "gui/phone/home.png",
        },
        # Gameplay Configurations
        "pause": { # no pause = messages will not wait for user time or user input before sending the next one
            "do_pause": True, # should we wait for a click to send the next message? like traditional dialogue
            "pause_time": False, # if we want to pause, should we auto-continue after a set amount of time? if false, just wait for a click
            "pause_length": 1.0 # if using pause_time, how long do we wait?
        }
    }

    # variables to hold the phone data
    phone_channel_data = {} # {channel_name: {"display_name": "...", "icon": "...", "participants": [], "is_group": False}}
    phone_channels = {}  # {channel_name: [(id, sender, message_string, kind, ...), ...]}
    channel_last_message_id = {} # {channel_name: last_id}
    channel_seen_latest = {} # {channel_name: seen_status} (this could be more intricate to track if EACH message was seen, but that's overkill)
    channel_notifs = {} # {channel_name: notification_status} (True/False)
    channel_visible = {} # {channel_name: visible_status} (True/False)
    current_phone_view = "channel_list" # where when the phone starts it should start at
    disable_phone_menu_switch = False # lock back button, basically
    phone_choice_options = [] # this will hold the currently active choices
    phone_choice_channel = None  # this holds the channel that the above choice aligns to (one at a time)
    channel_latest_global_id = {} # latest global channel id
    _phone_global_message_counter = 0  # latest global message counter

    # replace inline images natively
    def replace_emojis(text):
        """ Replaces custom emoji tags like <emoji_name> with Ren'Py image tags.
            This is an internal helper function to allow for easy emoji syntax in messages.
            Args:
                text (str): The message text that might contain emoji tags.
        """
        def sub(match):
            name = match.group(1)
            return "{image=%s}" % name
        return re.sub(r"<([A-Za-z0-9_]+)>", sub, text)

    # creates a new phone channel
    def create_phone_channel(channel_id, display_name, participants, icon_path, is_group=False):
        """ Creates a new phone channel, like a DM or a group chat.
            This function sets up the basic information for a new chat conversation.
            Args:
                channel_id (str): A unique identifier for the channel (e.g., "vanessa_dm").
                display_name (str): The name that appears at the top of the chat screen.
                participants (list): A list of strings with the names of everyone in the chat.
                icon_path (str): The file path to the icon for this channel.
                is_group (bool, optional): Set to True if this is a group chat. Defaults to False.
        """
        global phone_channel_data, phone_channels, channel_last_message_id, channel_notifs, channel_seen_latest, channel_visible
        if channel_id not in phone_channel_data:
            phone_channel_data[channel_id] = {
                "display_name": display_name,
                "icon": icon_path,
                "participants": participants,
                "is_group": is_group
            }
            phone_channels[channel_id] = []
            channel_last_message_id[channel_id] = 0
            channel_notifs[channel_id] = False
            channel_seen_latest[channel_id] = True
            channel_visible[channel_id] = True
            channel_latest_global_id[channel_id] = 0

    # add messages to a channel in the phone (kind 0 = normal message, kind 1 = timestamp, kind 2 = photo, kind 3 = has emojis)
    def send_phone_message(sender, message_text, channel_name, message_kind=0, summary_alt="none", image_x=320, image_y=320, do_pause=True):
        """ Sends a message to a specific phone channel and updates the UI.
            Args:
                sender (str): The name of the character sending the message.
                message_text (str): The content of the message or the path to an image.
                channel_name (str): The unique ID of the channel to send the message to.
                message_kind (int, optional): The type of message. 
                    0=text, 1=timestamp, 2=photo, 3=text with emoji. Defaults to 0.
                summary_alt (str, optional): Alternative text for the channel preview list. Defaults to "none".
                image_x (int, optional): The max width for a photo message. Defaults to 320.
                image_y (int, optional): The max height for a photo message. Defaults to 320.
                do_pause (bool, optional): Whether to pause the game after the message is sent. Defaults to True.
        """
        global _phone_global_message_counter, current_global_id
        # in case a channel doesn't exist, we now expect them to be explicitly made before-hand~
        if channel_name not in phone_channels:
            renpy.log("Tried to send message to non-existent channel: " + channel_name)
            return
        # sound logic (except for time stamps)
        if message_kind != 1:
            if sender == phone_config["phone_player_name"]:
                if phone_config.get("play_sound_send", False):
                    renpy.sound.play("audio/phone/send.mp3", channel="sound")
            else:
                play_the_sound = True
                if phone_config.get("no_sound_current_chat", False):
                    if current_phone_view == channel_name:
                        play_the_sound = False
                if phone_config.get("play_sound_receive", False) and play_the_sound:
                    renpy.sound.play("audio/phone/receive.mp3", channel="sound")
        _phone_global_message_counter += 1
        current_global_id = _phone_global_message_counter
        channel_latest_global_id[channel_name] = current_global_id
        last_id = channel_last_message_id.get(channel_name, 0)
        current_id = last_id + 1
        channel_last_message_id[channel_name] = current_id
        message_data = (current_id, sender, message_text, message_kind, current_global_id, summary_alt, image_x, image_y)
        phone_channels[channel_name].append(message_data)
        channel_notifs[channel_name] = True
        channel_seen_latest[channel_name] = False
        renpy.restart_interaction()
        if message_kind == 0:
            narrator.add_history(kind="adv", who=sender, what=message_text)
        elif message_kind == 1:
            narrator.add_history(kind="adv", who=phone_config["history_timestamp_prefix"], what=message_text)
        elif message_kind == 2:
            narrator.add_history(kind="adv", who=sender, what="Sent a photo.")
        renpy.checkpoint()
        if do_pause and phone_config["pause"]["do_pause"]:
            if phone_config["pause"]["pause_time"]:
                renpy.pause(phone_config["pause"]["pause_length"])
            else:
                renpy.pause()

    # basically clear notifs / mark as read for all
    def clear_notifications():
        """ Marks all channels as read and clears all notification dots.
            This is useful for when the story starts, to clear any pre-loaded messages,
            or if you want to programmatically mark everything as seen.
        """
        global channel_notifs, channel_seen_latest
        for channel_name in phone_channel_data.keys():
            if channel_name in channel_notifs:
                channel_notifs[channel_name] = False
            if channel_name in channel_seen_latest:
                channel_seen_latest[channel_name] = True
        renpy.restart_interaction()
    
    # function to reset the phone data
    def reset_phone_data():
        """ Resets all phone data to a clean slate.
            This function clears all channels, messages, and notifications.
            You can add initial setup calls (like create_phone_channel)
            inside this function to pre-populate the phone.
        """
        global current_phone_view, phone_channels, channel_last_message_id, channel_notifs, channel_seen_latest, channel_visible, phone_channel_data
        global channel_latest_global_id, _phone_global_message_counter
        # reset all our data
        phone_channel_data = {}
        phone_channels = {}
        channel_last_message_id = {}
        channel_notifs = {}
        channel_seen_latest = {}
        channel_visible = {}
        channel_latest_global_id = {}
        _phone_global_message_counter = 0
        current_phone_view = "channel_list"
        # ── LoveCity Contacts ────────────────────────────────────────
        # Maps channel_id → flag that must be True for the contact to appear.
        # Family channels (None = always visible from start).
        _me = phone_config["phone_player_name"]
        _ic = phone_config["default_icon"]

        # Family — always visible
        create_phone_channel("ch_mom",      "Mom",          ["Mom",          _me], "gui/phone/icons/Sarah.png")
        create_phone_channel("ch_sister",   "Emma",         ["Emma",         _me], "gui/phone/icons/Emma.png")
        # Friends / School
        create_phone_channel("ch_alex",     "Alex",         ["Alex",         _me], _ic)
        create_phone_channel("ch_maya",     "Maya",         ["Maya",         _me], _ic)
        create_phone_channel("ch_kai",      "Kai",          ["Kai",          _me], _ic)
        create_phone_channel("ch_theo",     "Theo",         ["Theo",         _me], _ic)
        create_phone_channel("ch_cora",     "Cora Finch",   ["Cora Finch",   _me], _ic)
        # Romance
        create_phone_channel("ch_luna",     "Luna",         ["Luna",         _me], _ic)
        create_phone_channel("ch_zane",     "Zane",         ["Zane",         _me], _ic)
        create_phone_channel("ch_nadia",    "Nadia",        ["Nadia",        _me], _ic)
        create_phone_channel("ch_ronnie",   "Ronnie",       ["Ronnie",       _me], _ic)
        # Professional
        create_phone_channel("ch_rivera",   "Dr. Rivera",   ["Dr. Rivera",   _me], _ic)
        create_phone_channel("ch_dr_obi",   "Dr. Obi",      ["Dr. Obi",      _me], _ic)
        # Lifestyle / Community
        create_phone_channel("ch_sera",     "Sera",         ["Sera",         _me], _ic)
        create_phone_channel("ch_simone",   "Simone",       ["Simone",       _me], _ic)
        create_phone_channel("ch_reo",      "Reo",          ["Reo",          _me], _ic)
        create_phone_channel("ch_dom",      "Dom",          ["Dom",          _me], _ic)
        create_phone_channel("ch_jamie",    "Jamie",        ["Jamie",        _me], _ic)
        create_phone_channel("ch_river",    "River",        ["River",        _me], _ic)
        create_phone_channel("ch_sasha",    "Sasha",        ["Sasha",        _me], _ic)
        create_phone_channel("ch_petra",    "Petra",        ["Petra",        _me], _ic)
        create_phone_channel("ch_august",   "August",       ["August",       _me], _ic)
        create_phone_channel("ch_arlo",     "Arlo",         ["Arlo",         _me], _ic)
        create_phone_channel("ch_eli",      "Eli",          ["Eli",          _me], _ic)
        create_phone_channel("ch_milo",     "Milo",         ["Milo",         _me], _ic)
        create_phone_channel("ch_oz",       "Oz",           ["Oz",           _me], _ic)
        create_phone_channel("ch_vesper",   "Vesper",       ["Vesper",       _me], _ic)
        create_phone_channel("ch_rio",      "Rio",          ["Rio",          _me], _ic)
        create_phone_channel("ch_dana",     "Dana",         ["Dana",         _me], _ic)
        create_phone_channel("ch_ines",     "Ines",         ["Ines",         _me], _ic)
        create_phone_channel("ch_vivienne", "Vivienne",     ["Vivienne",     _me], _ic)
        create_phone_channel("ch_camille",  "Camille",      ["Camille",      _me], _ic)
        create_phone_channel("ch_hana",     "Hana",         ["Hana",         _me], _ic)
        create_phone_channel("ch_harlow",   "Prof. Harlow", ["Prof. Harlow", _me], _ic)

        # Hide everyone except family — contacts unlock when you meet them
        for _ch_id in phone_channel_data:
            if _ch_id not in ("ch_mom", "ch_sister"):
                channel_visible[_ch_id] = False
        # clear notifications so phone starts clean
        clear_notifications()
        renpy.restart_interaction()

    # pause the text messages for a certain length
    def phone_pause(length=1.0):
        """ Pauses the game for a specific amount of time within the phone.
            This is a simple wrapper around renpy.pause() for convenience, allowing for
            timed delays between messages without relying on the automatic pause config.
            Args:
                length (float, optional): The duration of the pause in seconds. Defaults to 1.0.
        """
        renpy.pause(length)

    # hide the text box stuff when the phone is up
    def phone_start():
        """ Activates phone mode, preparing the UI for the phone screen.
            This function sets a flag that can be used to hide the normal
            dialogue window, ensuring the phone UI doesn't overlap with it.
            It should be called right before showing the phone_ui screen.
        """
        global phone_mode
        phone_mode = True
        renpy.restart_interaction()

    # restore the text box stuff when the phone is down
    def phone_end():
        """ Deactivates phone mode, restoring the normal game UI.
            This function resets the flag set by phone_start(), which should
            bring back the standard dialogue window. It should be called
            right after hiding the phone_ui screen.
        """
        global phone_mode
        phone_mode = False
        renpy.restart_interaction()

    # disable switching phone screens
    def lock_phone_screen():
        """ Disables the back button on the phone screen.
            This locks the player into the current view (a specific chat)
            and prevents them from returning to the channel list. Useful for
            scripted sequences where you need the player's focus.
        """
        global disable_phone_menu_switch
        disable_phone_menu_switch = True

    # enable switching phone screens
    def unlock_phone_screen():
        """ Enables the back button on the phone screen.
            This restores the player's ability to navigate back to the channel
            list from a chat view (basically just undoing the effect of lock_phone_screen()).
        """
        global disable_phone_menu_switch
        disable_phone_menu_switch = False

    # present choices to the user in the phone
    def present_phone_choices(choices, channel_name):
        """ Presents a set of choices to the player within a phone channel.
            This function displays tappable choice bubbles for the player. The game
            will pause and wait for the player to make a selection.
            Args:
                choices (list): A list of tuples defining the choices. Each tuple is in the
                    format ("preview_text", "message_to_send", action).
                    - "preview_text": The text shown on the choice button.
                    - "message_to_send": The message text that gets sent. If None, uses preview_text.
                    - "action": A Ren'Py action (like Call() or Jump()) to run after sending. Can be None.
                channel_name (str): The unique ID of the channel where the choices will appear.
        """
        # choices should be a list of tuples, like:
        # [("Choice Text 1", Jump("response_label_1")), ("Choice Text 2", Jump("response_label_2"))]
        global phone_choice_options, phone_choice_channel
        phone_choice_options = choices
        phone_choice_channel = channel_name
        renpy.ui.interact()  # make the game wait for the user..

    # gets the last message to show in the phone preview
    def get_channel_preview(channel_name):
        """ Gets the preview text for a channel to display on the channel list.
            This function retrieves the last message of a channel, formats it for
            the preview (e.g., adding sender for group chats, truncating), and
            returns it. It's an internal function used by the phone_ui screen.

            Args:
                channel_name (str): The unique ID of the channel to get the preview for.
        """
        if channel_name in phone_channels and phone_channels[channel_name]:
            for last_message_tuple in reversed(phone_channels[channel_name]):
                if last_message_tuple[3] != 1:  # skip message_kind=1 (index is now 3)
                    summary_alt = last_message_tuple[5] if len(last_message_tuple) > 5 else None
                    if summary_alt and summary_alt != "none":
                        return summary_alt
                    sender = last_message_tuple[1]
                    message_text = last_message_tuple[2]
                    message_kind = last_message_tuple[3]
                    preview_text = message_text
                    if message_kind == 3: # has emojis, get rid of them with fire
                        preview_text = re.sub(r"<[^>]+>", "", preview_text).strip()
                    # prepend sender if it's a group chat and not from the player
                    is_group = phone_channel_data.get(channel_name, {}).get("is_group", False)
                    if is_group and sender != phone_config["phone_player_name"]:
                        full_preview = "{}: {}".format(sender, preview_text)
                    else:
                        full_preview = preview_text
                    max_len = phone_config.get("preview_max_length", 35) 
                    if len(full_preview) > max_len:
                        # Slice it to make room for the "..."
                        return full_preview[:max_len - 3] + "..."
                    else:
                        return full_preview
        return phone_config["preview_no_message"]

    # force the user to go to a certain channel (can also be channel_list)
    def switch_channel_view(channel_name):
        """ Forces the phone to open a specific channel or the channel list.
            This can be used to guide the player to a new message or event in a
            different chat without requiring them to tap on it manually.
            Args:
                channel_name (str): The unique ID of the channel to switch to. Can also be
                    "channel_list" to return to the main message list.
        """
        global current_phone_view, channel_notifs, channel_seen_latest
        current_phone_view = channel_name
        channel_notifs[channel_name] = False
        channel_seen_latest[channel_name] = True
        renpy.restart_interaction()

    # hide a channel without deleting the data
    def hide_phone_channel(channel_name):
        """ Hides a channel from the channel list without deleting its history.
            The channel and its messages are preserved and can be made visible again
            using show_phone_channel().
            Args:
                channel_name (str): The unique ID of the channel to hide.
        """
        global channel_visible
        if channel_name in channel_visible:
            channel_visible[channel_name] = False
            renpy.restart_interaction()

    # show a channel that was hidden
    def show_phone_channel(channel_name):
        """ Makes a previously hidden channel visible again on the channel list.
            This function reverses the effect of hide_phone_channel().
            Args:
                channel_name (str): The unique ID of the channel to show.
        """
        global channel_visible
        if channel_name in channel_visible:
            channel_visible[channel_name] = True
            renpy.restart_interaction()

    # perma hide a channel aka delete it lol
    def delete_phone_channel(channel_name):
        """ Permanently deletes a channel and all of its associated data.
            This action is irreversible and will remove the channel, its messages,
            and all related settings from the phone.
            Args:
                channel_name (str): The unique ID of the channel to delete.
        """
        global phone_channel_data, phone_channels, channel_last_message_id, channel_seen_latest, channel_notifs, channel_visible, channel_latest_global_id, current_phone_view
        if channel_name in phone_channel_data:
            del phone_channel_data[channel_name]
        if channel_name in phone_channels:
            del phone_channels[channel_name]
        if channel_name in channel_last_message_id:
            del channel_last_message_id[channel_name]
        if channel_name in channel_seen_latest:
            del channel_seen_latest[channel_name]
        if channel_name in channel_notifs:
            del channel_notifs[channel_name]
        if channel_name in channel_visible:
            del channel_visible[channel_name]
        if channel_name in channel_latest_global_id:
            del channel_latest_global_id[channel_name]
        # make sure they aren't viewing a dead chat
        if current_phone_view == channel_name:
            switch_channel_view("channel_list")
        renpy.restart_interaction()

    # add someone to a group
    def add_participant_to_group(channel_name, new_participant_name, added_by_name=None):
        """ Adds a participant to a group chat and posts a notification message.
            This will update the channel's participant list and send a system message
            (like "X added Y to the group") to the chat.
            Args:
                channel_name (str): The unique ID of the group channel.
                new_participant_name (str): The name of the character being added.
                added_by_name (str, optional): The name of the character who added the new
                    participant. If None, a generic "joined" message is shown. Defaults to None.
        """
        if channel_name in phone_channel_data and phone_channel_data[channel_name]["is_group"]:
            phone_channel_data[channel_name]["participants"].append(new_participant_name)
            if added_by_name:
                template = phone_config.get("group_added", "{adder} added {participant} to the group.")
                message_text = template.format(adder=added_by_name, participant=new_participant_name)
            else:
                template = phone_config.get("group_joined", "{participant} joined the group.")
                message_text = template.format(participant=new_participant_name)
            send_phone_message("", message_text, channel_name, message_kind=1, do_pause=True)

    def remove_participant_from_group(channel_name, participant_to_remove):
        """Removes a participant from a group chat and posts a notification message.
            This will update the channel's participant list and send a system message
            (like "X left the group") to the chat.
            Args:
                channel_name (str): The unique ID of the group channel.
                participant_to_remove (str): The name of the character to remove.
        """
        if channel_name in phone_channel_data and phone_channel_data[channel_name]["is_group"]:
            if participant_to_remove in phone_channel_data[channel_name]["participants"]:
                phone_channel_data[channel_name]["participants"].remove(participant_to_remove)
                template = phone_config.get("group_left", "{participant} left the group.")
                message_text = template.format(participant=participant_to_remove)
                send_phone_message("", message_text, channel_name, message_kind=1, do_pause=True)

    # see if there is any current notifications at all
    def has_any_notification():
        """Checks if any channel has an active notification."""
        return any(channel_notifs.values())

    # same as above, but ignore the active channel (for instance, used to change the back icon)
    def has_any_notification_not_active():
        """Checks if any channel OTHER than the current one has an active notification."""
        return any(has_notif for channel, has_notif in channel_notifs.items() if channel != current_phone_view)

    # helper to grab values per theme
    def get_phone_theme_value(key):
        """Retrieves a theme-specific value from phone_config based on the current theme."""
        current_theme = phone_config["phone_theme"]
        # Accessing directly using the theme name as a key
        return phone_config[current_theme].get(key)

    # set the phone's theme to change via code (ex. if user wants dark mode instead)
    def set_phone_theme(theme_name):
        """Sets the phone's theme to a new value.
            This function changes the current theme of the phone UI, which can be used
            to switch between light, dark, or flip themes dynamically.
            Args:
                theme_name (str): The name of the theme to switch to (e.g., "light", "dark", "flip").
        """
        if theme_name in phone_config:
            phone_config["phone_theme"] = theme_name
            renpy.restart_interaction()
        else:
            renpy.log("Invalid phone theme: " + theme_name)

## -----------------------------------------------------
## Screen: Phone Messages
## -----------------------------------------------------
# phone relevant! initial phone position and size
default phone_zoom = 0.65
default phone_x = 0.5
default phone_y = 0.5
transform phone_position(p_zoom, p_x, p_y):
    anchor(0.5, 0.5)
    pos(p_x, p_y)
    zoom p_zoom

# phone relevant! make sure to define all emojis before you use them!
image emoji_sob = "gui/phone/emoji/sob.png"
image emoji_dizzy = "gui/phone/emoji/dizzy.png"

init -1 python:
    def _phone_bubble(img_key, fallback_color):
        """Return a Frame bubble if the image exists, otherwise a solid frame."""
        path = get_phone_theme_value(img_key)
        if path and renpy.loadable(path):
            return Frame(path, 23, 23)
        return Solid(fallback_color)

screen phone_ui():
    modal True
    zorder 150
    default was_channel_unread = False

    # Ensure phone data is initialised before rendering
    if not phone_channel_data:
        $ reset_phone_data()

    # Semi-transparent backdrop (non-interactive — modal absorbs stray clicks)
    add "#00000088"

    # Escape / right-click to close
    key "game_menu" action Function(lc_hide_phone)

    # ── PHONE FRAME ──────────────────────────────────────────
    # Uses the original kleineluka structure: layered images with
    # absolutely-positioned content on top.
    window:
        at phone_position(phone_zoom, phone_x, phone_y)
        xalign 0.5
        yalign 0.5
        xsize 600
        ysize 1000

        # Layer phone images: screen → header → base (base on top with transparent center)
        $ _screen_img = get_phone_theme_value("screen_background_image")
        $ _header_img = get_phone_theme_value("header_background_image")
        $ _base_img = get_phone_theme_value("base_background_image")
        if _screen_img and renpy.loadable(_screen_img):
            add _screen_img
        else:
            add Solid("#0f172a")
        if _header_img and renpy.loadable(_header_img):
            add _header_img
        else:
            add Solid("#162032") xsize 600 ysize 107
        if _base_img and renpy.loadable(_base_img):
            add _base_img
        else:
            add Solid("#1a1a2e")

        # Back button (when inside a chat)
        if current_phone_view != "channel_list" and disable_phone_menu_switch == False:
            $ back_icon_path = get_phone_theme_value("back_button_notif_image") if has_any_notification_not_active() else get_phone_theme_value("back_button_idle_image")
            if back_icon_path and renpy.loadable(back_icon_path):
                imagebutton:
                    xalign 0.15
                    yalign 0.1075
                    idle back_icon_path
                    hover back_icon_path
                    focus_mask True
                    xysize (75, 75)
                    action SetVariable("current_phone_view", "channel_list")
            else:
                textbutton "← Back":
                    style "empty"
                    xalign 0.08
                    yalign 0.1075
                    padding (8, 6)
                    hover_background "#33415544"
                    text_size 22
                    text_color "#94a3b8"
                    text_hover_color "#f472b6"
                    action SetVariable("current_phone_view", "channel_list")

        # Home button — closes the phone (uses the circle on the bezel)
        $ _home_img = get_phone_theme_value("home_button_image")
        if _home_img and renpy.loadable(_home_img):
            imagebutton:
                xalign 0.5
                yalign 0.955
                idle _home_img
                hover _home_img
                focus_mask True
                xysize (60, 60)
                action [Function(lc_hide_phone), NullAction()]
        else:
            textbutton "⊙":
                style "empty"
                xalign 0.5
                yalign 0.95
                padding (12, 8)
                text_size 32
                text_color "#ffffff88"
                text_hover_color "#ffffff"
                action [Function(lc_hide_phone), NullAction()]

        # ── CONTENT AREA ──────────────────────────────────────
        # Positioned to align with the transparent center of the base image
        vbox:
            id "phone_viewport"
            xsize 450
            ysize 775
            yalign 0.325
            xalign 0.475
            vbox:
                spacing 10
                # Display the title/name at the top of the screen
                if current_phone_view != "channel_list":
                    null height 5
                    $ _cv_icon = phone_channel_data[current_phone_view].get("icon", "")
                    if _cv_icon and renpy.loadable(_cv_icon):
                        add _cv_icon:
                            xalign 0.5
                            xysize (50, 50)
                    text phone_channel_data[current_phone_view]["display_name"]:
                        style "phone_header_style"
                        ypos -5
                else:
                    null height 40
                    text phone_config["channels_title"]:
                        style "phone_header_style"
                null height 19

                # ── MAIN CONTENT ──────────────────────────────
                if current_phone_view == "channel_list":
                    # ── CHANNEL LIST ──────────────────────────
                    $ yadj = ui.adjustment()
                    viewport:
                        id "message_viewport"
                        xfill True
                        ysize 750
                        yadjustment yadj
                        scrollbars "vertical"
                        mousewheel True
                        # list of chats
                        vbox:
                            spacing 15
                            $ visible_channels = [ch for ch in phone_channel_data.keys() if channel_visible.get(ch, True)]
                            python:
                                if phone_config["sort_channels_by_latest"]:
                                    channel_list_to_display = sorted(visible_channels, key=lambda ch_name: channel_latest_global_id.get(ch_name, 0), reverse=True)
                                else:
                                    channel_list_to_display = visible_channels
                            for channel_name in channel_list_to_display:
                                button:
                                    action [
                                        SetDict(channel_notifs, channel_name, False),
                                        SetVariable("current_phone_view", channel_name)
                                    ]
                                    style "phone_channel_button_style"
                                    xfill True
                                    # contains the chat description and a divider after
                                    vbox:
                                        # contains chat icon, chat name, chat preview, and notification dot
                                        hbox:
                                            spacing 10
                                            # the chat channel icon
                                            $ _ch_icon_path = phone_channel_data[channel_name].get("icon", "")
                                            if _ch_icon_path and renpy.loadable(_ch_icon_path):
                                                add _ch_icon_path:
                                                    xysize (50, 50)
                                                    yalign 0.5
                                            else:
                                                # fallback: initial circle
                                                $ _ch_dname = phone_channel_data[channel_name]["display_name"]
                                                $ _ch_initial = _ch_dname[0] if _ch_dname else "?"
                                                frame:
                                                    style "empty"
                                                    xysize (50, 50)
                                                    background Solid("#f472b622")
                                                    yalign 0.5
                                                    text _ch_initial:
                                                        color "#f472b6"
                                                        size 24
                                                        bold True
                                                        xalign 0.5
                                                        yalign 0.5
                                            # the chat channel name and preview message
                                            vbox:
                                                text phone_channel_data[channel_name]["display_name"]:
                                                    style "phone_channel_name_style"
                                                text get_channel_preview(channel_name):
                                                    style "phone_channel_preview_style"
                                            # add a notification dot if the channel has one
                                            if channel_notifs.get(channel_name, False):
                                                $ _notif_img = get_phone_theme_value("notification_dot_image")
                                                if _notif_img and renpy.loadable(_notif_img):
                                                    add _notif_img:
                                                        xalign 1.0
                                                        yalign 0.6
                                                        xoffset -5
                                                        size (25, 25)
                                                else:
                                                    text "●":
                                                        color "#f43f5e"
                                                        size 18
                                                        xalign 1.0
                                                        yalign 0.5
                                        # add a line below every channel
                                        null height 10
                                        frame:
                                            style "empty"
                                            background get_phone_theme_value("channel_divider_colour")
                                            xfill True
                                            ysize 1
                else:
                    # ── CHAT VIEW ─────────────────────────────
                    $ yadj = ui.adjustment()
                    viewport:
                        id "message_viewport"
                        xfill True
                        ysize 750
                        yadjustment yadj
                        scrollbars "vertical"
                        mousewheel True
                        draggable False
                        # do this once when it opens
                        if phone_config["auto_scroll"]:
                            $ yadj.value = (yadj.range + 1000)
                        vbox:
                            spacing 8
                            xfill True
                            if current_phone_view in phone_channels:
                                $ latest_channel_id = channel_last_message_id.get(current_phone_view, 0)
                                $ last_sender_in_chat_view = None
                                # display all messages
                                for message_data in phone_channels[current_phone_view]:
                                    $ msg_id, sender, message_text, message_kind, current_global_id, summary_alt, image_x, image_y = message_data
                                    if sender == phone_config["phone_player_name"]:
                                        $ bubble_bg = _phone_bubble("player_bubble_image", "#6d28d9")
                                        $ text_colour = get_phone_theme_value("message_player_text_colour")
                                        $ anim_direction = 1
                                    else:
                                        $ bubble_bg = _phone_bubble("character_bubble_image", "#1e293b")
                                        $ text_colour = get_phone_theme_value("message_character_text_colour")
                                        $ anim_direction = -1
                                    $ msg_padding = phone_config["message_padding"]
                                    # displaying the sender's name for group chats
                                    $ is_group_chat = phone_channel_data[current_phone_view]["is_group"]
                                    if is_group_chat and sender != phone_config["phone_player_name"] and sender != last_sender_in_chat_view:
                                        text sender:
                                            style "phone_sender_name_style"
                                            xalign msg_padding
                                            xoffset 5
                                    if message_kind == 0:
                                        # now make the message bubble for text
                                        frame:
                                            style "empty"
                                            if sender == phone_config["phone_player_name"]:
                                                xpos 1.0 - msg_padding xanchor 1.0
                                            else:
                                                xpos msg_padding xanchor 0.0
                                            background bubble_bg
                                            padding (15, 10)
                                            xmaximum 360
                                            if msg_id == latest_channel_id and not channel_seen_latest[current_phone_view]:
                                                at message_appear(anim_direction)
                                                $ channel_seen_latest[current_phone_view] = True
                                                $ channel_notifs[current_phone_view] = False
                                                if phone_config["auto_scroll"]:
                                                    $ yadj.value = (yadj.range + 1000)
                                            text message_text:
                                                color text_colour
                                                size phone_config["message_font_size"]
                                                layout "tex"
                                        $ last_sender_in_chat_view = sender
                                    elif message_kind == 1:
                                        # this is a timestamp
                                        null height 15
                                        hbox:
                                            xalign 0.5
                                            xmaximum 360
                                            if msg_id == latest_channel_id and not channel_seen_latest[current_phone_view]:
                                                at timestamp_appear()
                                                $ channel_seen_latest[current_phone_view] = True
                                                $ channel_notifs[current_phone_view] = False
                                                if phone_config["auto_scroll"]:
                                                    $ yadj.value = (yadj.range + 1000)
                                            text message_text:
                                                color get_phone_theme_value("timestamp_text_colour")
                                                size phone_config["timestamp_font_size"]
                                                layout "tex"
                                        null height 15
                                        $ last_sender_in_chat_view = None
                                    elif message_kind == 2:
                                        # this is a photo
                                        frame:
                                            style "empty"
                                            if sender == phone_config["phone_player_name"]:
                                                xpos 1.0 - msg_padding xanchor 1.0
                                            else:
                                                xpos msg_padding xanchor 0.0
                                            background bubble_bg
                                            padding (10, 10)
                                            xmaximum 360
                                            if msg_id == latest_channel_id and not channel_seen_latest[current_phone_view]:
                                                at message_appear(anim_direction)
                                                $ channel_seen_latest[current_phone_view] = True
                                                $ channel_notifs[current_phone_view] = False
                                                if phone_config["auto_scroll"]:
                                                    $ yadj.value = (yadj.range + 1000)
                                            add Image(message_text) at scale_to_fit(image_x, image_y)
                                        $ last_sender_in_chat_view = sender
                                    elif message_kind == 3:
                                        # this is a message with emojis
                                        frame:
                                            style "empty"
                                            if sender == phone_config["phone_player_name"]:
                                                xpos 1.0 - msg_padding xanchor 1.0
                                            else:
                                                xpos msg_padding xanchor 0.0
                                            background bubble_bg
                                            padding (10, 10)
                                            xmaximum 360
                                            if msg_id == latest_channel_id and not channel_seen_latest[current_phone_view]:
                                                at message_appear(anim_direction)
                                                $ channel_seen_latest[current_phone_view] = True
                                                $ channel_notifs[current_phone_view] = False
                                                if phone_config["auto_scroll"]:
                                                    $ yadj.value = (yadj.range + 1000)
                                            hbox:
                                                spacing 5
                                                xmaximum 340
                                                text replace_emojis(message_text):
                                                    size phone_config["message_font_size"]
                                                    color text_colour
                                                    layout "tex"
                                        $ last_sender_in_chat_view = sender
                            else:
                                text "No messages yet.":
                                    color get_phone_theme_value("empty_channel_text_colour")
                                    size 20
                                    xalign 0.5
                                    italic True
                            # if there's a choice
                            if phone_choice_options and phone_choice_channel == current_phone_view:
                                null height 20
                                vbox:
                                    xalign 0.5
                                    spacing 8
                                    for i, (preview_text, actual_message, action) in enumerate(phone_choice_options):
                                        $ message_to_send = actual_message if actual_message is not None else preview_text
                                        $ text_colour = get_phone_theme_value("message_player_text_colour")
                                        textbutton preview_text at choice_appear(delay = i * 0.1):
                                            action [
                                                SetVariable("phone_choice_options", []),
                                                SetVariable("phone_choice_channel", None),
                                                SetVariable("disable_phone_menu_switch", False),
                                                Function(send_phone_message, sender=phone_config["phone_player_name"], message_text=message_to_send, channel_name=current_phone_view, do_pause=False),
                                                If(action is not None, action),
                                                Return()
                                            ]
                                            background Frame(get_phone_theme_value("player_bubble_image"), 23, 23)
                                            idle_background Frame(get_phone_theme_value("player_bubble_image"), 23, 23)
                                            hover_background Frame(get_phone_theme_value("player_bubble_hover_image"), 23, 23)
                                            text_color text_colour
                                            text_size phone_config["choice_font_size"]
                                            text_align 0.5
                                            xalign 0.5
                                            padding (15, 10)
                            # add a bit of extra padding to the bottom of the viewport
                            null height 30

style phone_header_style is default:
    size 28
    color get_phone_theme_value("header_text_colour")
    xalign 0.5

style phone_channel_button_style is button:
    background None
    hover_background get_phone_theme_value("channel_button_hover_background")
    xpadding 10
    ypadding 8

style phone_channel_name_style is default:
    size 22
    color get_phone_theme_value("channel_name_text_colour")
    bold True

style phone_channel_preview_style is default:
    size 18
    color get_phone_theme_value("channel_preview_text_colour")

style phone_message_style is default:
    size 20
    color get_phone_theme_value("empty_channel_text_colour")
    xalign 0.0

style phone_sender_name_style is default:
    size 16
    color get_phone_theme_value("sender_name_text_colour")
    yoffset 2
    ypadding 0
    yalign 1.0

transform message_appear(pDirection):
    alpha 0.0
    xoffset 50 * pDirection # offset based direction
    parallel:
        ease 0.5 alpha 1.0 # fade in
    parallel:
        easein_back 0.5 xoffset 0 # slide in
    alpha 1.0

transform timestamp_appear():
    alpha 0.0
    yoffset 50
    parallel:
        ease 0.5 alpha 1.0 # fade up
    parallel:
        easein_back 0.5 yoffset 0 # slide up

transform choice_appear(delay=0.0):
    alpha 0.0
    yoffset 50
    pause delay
    parallel:
        ease 0.5 alpha 1.0 # fade up
    parallel:
        easein_back 0.5 yoffset 0 # slide up

transform scale_to_fit(maxw, maxh):
    size (maxw, maxh)
    fit "contain"

#
#⠀⠀⠀⠀⠀⠀⠀   ⠀⠀⠀ ⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣶⣟⣛⠛⠋⠉⠉⠉⠉⠉⠉⠉⠉⠉⠙⢛⣛⣷⡦⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠋⠉
#⠀⠀⠀⠀⠀⠀⠀⠀⠀      
#                Made by an Angel.
# ⠀ ⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⢀⡀⠀
#  ⣴⠛⠉⠉⠱⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠞⠉⠉⠙⣦
#  ⣧⠀⠀⠀⠀⠀⠙⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡴⠋⠀⠀⠀⠀⠀⣼
#  ⠹⣄⠀⠀⠀⠀⠀⠀⠈⠙⠲⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡴⠖⠋⠀⠀⠀⠀⠀⠀⠀⣠⠏
#  ⠀⠙⢶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢦⡀⠀⠀⠀⠀⠀⢀⡴⠋⠁⠀⠀⠀⠀⠀⠀⠀⣀⣠⡾⠋⠀
# ⠀ ⠀⡼⠋⠉⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⢹⡄⠀⠀⠀⢠⡟⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠉⠙⢧⠀⠀
# ⠀ ⠈⢧⡀⠀⠀⠀⠀⠀⢀⠀⣴⠋⡉⢳⡄⣷⠀⠀⠀⣾⢠⡞⠉⠙⣦⠀⠀⢀⠀⠀⠀⠀⢀⡼⠀⠀
#  ⠀⠀⠈⠙⠒⢲⡟⠀⠀⠀⠀⢻⣄⠙⠛⣱⠇⠀⠀⠀⠸⣎⠛⠋⣠⡟⠀⠀⠈⠀⢻⡗⠒⠋⠁⠀⠀
#⠀ ⠀⠀ ⠀⠀⠈⠷⣄⣀⣀⣀⣤⠟⠛⠛⠁⠀⠀⠀⠀⠀⠈⠛⠛⠻⣤⣀⣀⣀⣤⠾⠁⠀⠀⠀⠀⠀
#⠀⠀  ⠀⠀⠀⠀⠀⠈⠁⠉⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠉⠈⠀⠀⠀⠀⠀⠀⠀⠀
#
#         more of me: https://www.luka.moe
#