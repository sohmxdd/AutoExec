import subprocess
from daytona import Daytona
from autoexec.core import ExecutionBackend, ExecutionResult

# NOTE: Daytona backend is intended for cloud runners, not local execution

class DaytonaBackend(ExecutionBackend):
    def __init__(self):
        self.client = Daytona()

    def _get_container_id(self, sandbox_id: str) -> str:
        """Find the Docker container for a Daytona sandbox"""
        proc = subprocess.run(
            [
                "docker",
                "ps",
                "--filter",
                f"label=daytona.sandbox_id={sandbox_id}",
                "--format",
                "{{.ID}}",
            ],
            capture_output=True,
            text=True,
        )

        container_id = proc.stdout.strip()
        if not container_id:
            raise RuntimeError(f"No container found for sandbox {sandbox_id}")

        return container_id

    def execute(self, code: str, language: str = "python") -> ExecutionResult:
        sandbox = self.client.create()

        try:
            sandbox.start()

            
            container_id = self._get_container_id(sandbox.id)

            
            proc = subprocess.run(
                [
                    "docker",
                    "exec",
                    container_id,
                    "python",
                    "-c",
                    code,
                ],
                capture_output=True,
                text=True,
            )

            stdout = proc.stdout
            stderr = proc.stderr
            success = proc.returncode == 0

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

        finally:
            try:
                sandbox.stop()
            finally:
                sandbox.delete()
