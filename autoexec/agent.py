from autoexec.backends.local import LocalBackend
from autoexec.llm import fix_code
from autoexec.diff import unified_diff
from autoexec.memory import FixMemory
from autoexec.tester import run_tests


NON_FIXABLE_ERRORS = {
    "TimeoutError",
    "ExecutionTimeout",
    "KeyboardInterrupt",
    "DaemonError",
    "DockerError",
    "BackendError",
    "ModuleNotFoundError",
    "ImportError",
    "UnicodeEncodeError",
    None,
}


def section(title: str):
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)


def sub_section(title: str):
    print("\n" + "-" * 40)
    print(title)
    print("-" * 40)


class AutoExecAgent:
    def __init__(self, max_retries: int = 5, backend: str = "local"):
        self.max_retries = max_retries
        self.memory = FixMemory()

        if backend == "daytona":
            print("Daytona backend is experimental and disabled")
            print("Falling back to local execution backend")
            self.backend = LocalBackend()
        else:
            print("Using local execution backend")
            self.backend = LocalBackend()

    def run(self, code: str, tests: str | None = None, language: str = "python"):
        current_code = code

        for attempt in range(1, self.max_retries + 1):
            section(f"ATTEMPT {attempt} / {self.max_retries}")

            result = self.backend.execute(current_code, language)

            sub_section("Execution Output")

            print("STDOUT:")
            print(result.stdout if result.stdout else "<empty>")

            if result.stderr:
                print("\nSTDERR:")
                print(result.stderr)

            print("\nResult :", "SUCCESS" if result.success else "FAILED")

            
            if not result.success:
                error_type = result.error_type
                print("\nError detected:", error_type)

                if error_type in NON_FIXABLE_ERRORS:
                    print("Non-fixable error detected. Aborting retries.")
                    return result

                remembered_fix = self.memory.get(error_type)
                if remembered_fix:
                    print("Using remembered fix")
                    fixed_code = remembered_fix
                else:
                    print("Fixing crash with LLM...")
                    fixed_code = fix_code(
                        current_code,
                        error_type,
                        result.error_message
                    )
                    self.memory.store(error_type, fixed_code)

            
            elif tests:
                sub_section("Running Tests")
                test_result = run_tests(result.stdout, tests)

                if test_result.passed:
                    print("Tests passed")
                    return result

                print("Tests failed:", test_result.error)
                print("Fixing code to satisfy tests...")

                fixed_code = fix_code(
                    current_code,
                    "TestFailure",
                    test_result.error
                )

            
            else:
                return result

            
            diff = unified_diff(current_code, fixed_code)
            if diff.strip():
                sub_section("Code Diff")
                print(diff)

            current_code = fixed_code

        section("FINAL RESULT")
        print("Max retries reached. Returning last result.")
        return result
