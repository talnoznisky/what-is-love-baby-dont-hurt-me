import argparse

OUTPUT = "baby, don't hurt me\ndon't hurt me\nno more."

def main() -> None:
    parser = argparse.ArgumentParser(
        prog="what-is-love",
        description="Prints the only correct answer to the only correct question."
    )
    
    parser.add_argument("is_", choices=["is"], help=argparse.SUPPRESS, metavar="is")
    parser.add_argument("love", choices=["love"], help=argparse.SUPPRESS)

    parser.parse_args()
    print(OUTPUT)

if __name__ == "__main__":
    main()
