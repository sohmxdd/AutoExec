class TestResult:
    def __init__(self, passed: bool, error: str = ""):
        self.passed = passed
        self.error = error


def run_tests(output: str, tests: str) -> TestResult:
    """
    Runs tests with access to `output` variable.
    Tests must raise AssertionError on failure.
    """
    local_env = {
        "output": output
    }

    try:
        exec(tests, {}, local_env)
        return TestResult(passed=True)
    except AssertionError as e:
        return TestResult(passed=False, error=str(e))
    except Exception as e:
        return TestResult(passed=False, error=f"Test error: {e}")
