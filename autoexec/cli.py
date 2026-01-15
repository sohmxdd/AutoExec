import argparse
from pathlib import Path

from autoexec.agent import AutoExecAgent


def run_command(args):
    # Resolve path safely (relative → absolute)
    code_path = Path(args.code).expanduser().resolve()

    if not code_path.exists():
        raise FileNotFoundError(f"Code file not found: {code_path}")

    tests_code = None
    if args.tests:
        tests_path = Path(args.tests).expanduser().resolve()
        if not tests_path.exists():
            raise FileNotFoundError(f"Tests file not found: {tests_path}")
        tests_code = tests_path.read_text(encoding="utf-8")

    code = code_path.read_text(encoding="utf-8")

    agent = AutoExecAgent(
        max_retries=args.retries,
        backend=args.backend,
    )

    result = agent.run(
        code=code,
        tests=tests_code,
        language=args.language,
    )

    print("\n=== FINAL RESULT ===")
    print("STDOUT:", result.stdout)
    print("SUCCESS:", result.success)


def main():
    parser = argparse.ArgumentParser(
        prog="autoexec",
        description="AutoExec — self-healing code execution engine",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser("run", help="Run a code file")
    run_parser.add_argument("code", help="Path to code file")
    run_parser.add_argument(
        "--tests", help="Optional tests file", default=None
    )
    run_parser.add_argument(
        "--language", default="python", help="Programming language"
    )
    run_parser.add_argument(
        "--backend", default="local", help="Execution backend"
    )
    run_parser.add_argument(
        "--retries", type=int, default=5, help="Max retries"
    )

    run_parser.set_defaults(func=run_command)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
