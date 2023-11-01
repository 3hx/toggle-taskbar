# Bind the function to a key
import keyboard
from .utils import toggle_taskbar


current_hotkey = "ctrl+esc"


def change_hotkey(new_hotkey):
    # global current_hotkey
    # keyboard.remove_hotkey(current_hotkey)
    current_hotkey = new_hotkey
    keyboard.add_hotkey(current_hotkey, toggle_taskbar, suppress=True)


def default_hotkey():
    keyboard.add_hotkey(current_hotkey, toggle_taskbar, suppress=True)
