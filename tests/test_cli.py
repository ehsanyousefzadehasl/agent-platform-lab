from agent_platform.cli import build_parser


def test_parser_accepts_task() -> None:
    args = build_parser().parse_args(["inspect the repository"])

    assert args.task == "inspect the repository"