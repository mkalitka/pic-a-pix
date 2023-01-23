import argparse

from pic_a_pix import version, k4sia_image
from pic_a_pix.cli import argtypes


def create_argument_parser() -> argparse.ArgumentParser:
    """Parse all the command line arguments"""
    parser = argparse.ArgumentParser(
        prog="pic_a_pix",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description=(
            "A simple Python project that creates nonograms "
            "from pictures and automatically solves them."
        ),
    )

    parser.add_argument(
        "-V",
        "--version",
        action="store_true",
        default=argparse.SUPPRESS,
        help="prints installed pic-a-pix version",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        default=argparse.SUPPRESS,
        help="verbose mode (prints more logs)",
    )

    parser.add_argument(
        "-i",
        "--image",
        action="store",
        type=argtypes.img_path,
        help="path to an image to be converted",
    )

    parser.add_argument(
        "-l",
        "--level",
        action="store",
        type=argtypes.level,
        default=0,
        help="sets difficulty level (0-2)",
    )

    parser.add_argument(
        "-t",
        "--threshold",
        action="store",
        type=argtypes.threshold,
        default=160,
        help="sets threshold for black pixels from 0 to 255",
    )

    return parser


def print_version() -> None:
    """Prints installed pic_a_pix version"""
    print(f"Current pic_a_pix version: {version.__version__}")


def convert_image(img_name: str, lvl: int, threshold: int) -> None:
    """Converts and shows nonogram"""
    converted = k4sia_image.convert_img(img_name, lvl, threshold)
    converted.show()
    print(k4sia_image.columns_and_rows(converted))


def main() -> None:
    """Run as Python application"""
    parser = create_argument_parser()
    cmdline_arguments = parser.parse_args()

    if hasattr(cmdline_arguments, "version"):
        print_version()
    elif cmdline_arguments.image is not None:
        convert_image(
            cmdline_arguments.image,
            cmdline_arguments.level,
            cmdline_arguments.threshold,
        )
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
