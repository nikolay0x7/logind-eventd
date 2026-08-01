from .version import __version__


def main() -> None:
    print(f"logind-eventd {__version__}")


if __name__ == "__main__":
    main()
