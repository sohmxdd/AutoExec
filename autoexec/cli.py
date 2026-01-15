import argparse
from pathlib import Path
import os

from autoexec.agent import AutoExecAgent


def run_command(args):
    # Resolve paths from where the user runs the command
    cwd = Path(os.getcwd())

    code_path = (cwd / args.code).resolve()
    tests_path = (cwd / args.tests).resolve() if args.tests else None

    if not code_path.exists():
        raise FileNotFoundError(f"Code file not found: {code_path}")

    if tests_path and not tests_path.exists():
        raise FileNotFoundError(f"Tests file not found: {tests_path}")

    code = code_path.read_text()

    tests = tests_path.read_text() if tests_path else None

    agent = AutoExecAgent()

    result = agent.run(
        code=code,
        tests=tests,
        language="python"
    )

    print("\n=== FINAL RESULT ===")
    print("STDOUT:")
    print(result.stdout)

    if result.stderr:
        print("\nSTDERR:")
        print(result.stderr)

    print("\nSUCCESS:", result.success)


def main():
    parser = argparse.ArgumentParser(
        prog="autoexec",
        description="AutoExec — self-healing code execution engine"
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser(
        "run",
        help="Run a Python file with automatic crash fixing"
    )

    run_parser.add_argument(
        "code",
        help="Path to Python file to execute"
    )

    run_parser.add_argument(
        "--tests",
        help="Optional tests file",
        required=False
    )

    run_parser.set_defaults(func=run_command)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
