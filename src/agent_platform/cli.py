import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run and evaluate an AI coding agent."
    )
    parser.add_argument("task", help="Task to give the agent")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    print(f"Task received: {args.task}")


if __name__ == "__main__":
    main()