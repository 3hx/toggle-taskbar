import ctypes

# Define the necessary constants for Windows API
SW_HIDE = 0  # Constant to hide the window
SW_SHOW = 5  # Constant to show the window
GWL_STYLE = -16  # Constant to get window style
WS_VISIBLE = 268435456  # Constant for visible window style

# State variable to track if taskbar is active or not
isActive = False


def format_user_input():
    pass


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
