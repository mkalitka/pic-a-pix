import os
import argparse

from PIL import Image


def img_path(path: str) -> str:
    """Check if string is a valid path to an image"""
    try:
        with Image.open(path):
            return path
    except IOError as exc:
        raise argparse.ArgumentTypeError(f"{path} is not a valid image path") from exc



def size(img_size: str) -> int:
    """Check if size is valid"""
    try:
        if 5 <= int(img_size) <= 100:
            return int(img_size)
        raise argparse.ArgumentTypeError("invalid image size (5-100)")
    except ValueError as exc:
        raise argparse.ArgumentTypeError("invalid image size (5-100)") from exc




def threshold(img_threshold: str) -> int:
    """Check if threshold is valid"""
    try:
        if 0 <= int(img_threshold) <= 255:
            return int(img_threshold)
        raise argparse.ArgumentTypeError("invalid threshold (0-255)")
    except ValueError as exc:
        raise argparse.ArgumentTypeError("invalid threshold (0-255)") from exc

