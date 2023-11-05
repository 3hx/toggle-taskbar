from toggle_taskbar import cli, gui


def run():
    print("running")
    # Assume a condition to decide whether to run CLI or GUI
    is_cli = True  # Set to False to run GUI
    if is_cli:
        cli.main()
    else:
        gui.main()  # Assuming there's a main function in gui.py

    gui.create_tray_icon()


if __name__ == "__main__":
    run()
