import pystray
from PIL import Image
import tkinter as tk
from tkinter import simpledialog

from . import keys
import tkinter as tk

key_combination = []


# def key_pressed(event):
#     key = event.keysym
#     if key not in key_combination:
#         key_combination.append(key)


# def get_user_input() -> str:
#     global key_combination
#     key_combination = []  # Reset the key combination
#     root = tk.Tk()
#     root.title("Change Hotkey")

#     h1_label = tk.Label(root, text="Change Hotkey", font=("Arial", 24))
#     h1_label.pack(pady=10)

#     p_label = tk.Label(
#         root,
#         text="Press a combination of keys to change this title",
#         font=("Arial", 12),
#     )
#     p_label.pack(pady=10)

#     confirm_button = tk.Button(root, text="Confirm", command=root.quit)
#     confirm_button.pack(pady=10)

#     root.bind("<Key>", key_pressed)
#     root.mainloop()

#     # Convert list of keys to a string separated by '+'
#     user_input = "+".join(key_combination)
#     root.destroy()
#     return user_input


def get_user_input() -> str:
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    user_input = simpledialog.askstring("Input", "Please enter the new hotkey:")
    root.destroy()  # Close the window after getting input
    return user_input


# TODO: Add a better icon
def create_image():
    # Generate an image and return it
    width, height = 64, 64
    color1, color2 = (255, 255, 255), (0, 0, 0)  # RGB tuples for white and black

    image = Image.new("RGB", (width, height), color1)
    pixels = image.load()

    # Draw a black cross
    for i in range(width):
        pixels[i, height // 2] = color2
    for i in range(height):
        pixels[width // 2, i] = color2

    return image


def on_change_hotkey(icon, item):
    new_hotkey = get_user_input()
    keys.remove_hotkey()
    keys.change_hotkey(new_hotkey)


def on_exit(icon, item):
    icon.stop()
    keys.exit_application()


def create_tray_icon():
    image = create_image()
    menu = [
        pystray.MenuItem("Change Hotkey", on_change_hotkey),
        pystray.MenuItem("Exit", on_exit),
    ]
    tray_name = "Toggle Taskbar"
    icon = pystray.Icon(tray_name, image, tray_name, menu)
    icon.run()
