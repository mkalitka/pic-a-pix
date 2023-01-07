import argparse

from pic_a_pix import version


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

    return parser


def print_version() -> None:
    """Prints installed pic_a_pix version"""
    print(f"Current pic_a_pix version: {version.__version__}")


def main() -> None:
    """Run as Python application"""
    parser = create_argument_parser()
    cmdline_arguments = parser.parse_args()

    if hasattr(cmdline_arguments, "version"):
        print_version()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
