import ctypes
import keyboard

# Define the necessary constants
SW_HIDE = 0
SW_SHOW = 5
GWL_STYLE = -16
WS_VISIBLE = 268435456
# State
isActive = False


# Hide the taskbar
def toggle_taskbar():
    # Toggles isPressed
    global isActive
    isActive = not isActive

    taskbar = ctypes.windll.user32.FindWindowW("Shell_TrayWnd", None)
    style = ctypes.windll.user32.GetWindowLongW(taskbar, GWL_STYLE)
    if isActive:
        ctypes.windll.user32.ShowWindow(taskbar, SW_HIDE)
    else:
        if not style & WS_VISIBLE:
            ctypes.windll.user32.ShowWindow(taskbar, SW_SHOW)

    return False  # This suppresses the key event


def check_ctrl_esc(e):
    if keyboard.is_pressed("ctrl"):  # Check if Ctrl is pressed along with Esc
        return toggle_taskbar()
    return True  # Don't suppress the key event if Ctrl is not pressed


# Bind the function to a key
keyboard.on_press_key("esc", check_ctrl_esc, suppress=True)

# Keep the program running to listen for key presses
keyboard.wait()
