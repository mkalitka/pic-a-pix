import argparse

from PIL import Image


def img_path(path: str) -> str:
    """Check if string is a valid path to an image"""
    try:
        with Image.open(path):
            return path
    except IOError as exc:
        raise argparse.ArgumentTypeError(f"{path} is not a valid image path") from exc


def level(lvl: str) -> int:
    """Check if size is valid"""
    try:
        if 0 <= int(lvl) <= 2:
            return int(lvl)
        raise argparse.ArgumentTypeError("invalid level (0-2)")
    except ValueError as exc:
        raise argparse.ArgumentTypeError("invalid level (0-2)") from exc


def threshold(img_threshold: str) -> int:
    """Check if threshold is valid"""
    try:
        if 0 <= int(img_threshold) <= 255:
            return int(img_threshold)
        raise argparse.ArgumentTypeError("invalid threshold (0-255)")
    except ValueError as exc:
        raise argparse.ArgumentTypeError("invalid threshold (0-255)") from exc
