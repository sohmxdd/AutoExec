import subprocess
import tempfile
import sys
from autoexec.core import ExecutionBackend, ExecutionResult


class LocalBackend(ExecutionBackend):
    def execute(self, code: str, language: str = "python") -> ExecutionResult:
        if language != "python":
            raise ValueError("Only Python is supported in v1")

        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".py", delete=False
        ) as f:
            f.write(code)
            file_path = f.name

        try:
            proc = subprocess.run(
                [sys.executable, file_path],
                capture_output=True,
                text=True,
                timeout=5  
            )

            stdout = proc.stdout
            stderr = proc.stderr
            success = proc.returncode == 0

        except subprocess.TimeoutExpired:
            return ExecutionResult(
                stdout="",
                stderr="Execution timed out",
                success=False,
                error_type="TimeoutError",
                error_message="Code exceeded time limit",
            )

        error_type = None
        error_message = None

        if not success and stderr:
            last_line = stderr.strip().splitlines()[-1]
            if ":" in last_line:
                error_type, error_message = last_line.split(":", 1)
                error_type = error_type.strip()
                error_message = error_message.strip()

        return ExecutionResult(
            stdout=stdout,
            stderr=stderr,
            success=success,
            error_type=error_type,
            error_message=error_message,
        )
