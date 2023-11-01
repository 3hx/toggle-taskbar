import argparse
from . import keys


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Toggle taskbar visibility with a hotkey."
    )
    parser.add_argument(
        "-k", "--hotkey", type=str, help="The hotkey to toggle the taskbar."
    )
    return parser.parse_args()


def main():
    args = parse_arguments()
    if args.hotkey:
        keys.change_hotkey(args.hotkey)
    else:
        keys.default_hotkey()
