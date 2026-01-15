from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


class ExecutionBackend(ABC):
    @abstractmethod
    def execute(self, code: str, language: str = "python"):
        pass


@dataclass
class ExecutionResult:
    stdout: str
    stderr: str
    success: bool

    # error metadata (added in Step 2)
    error_type: Optional[str] = None
    error_message: Optional[str] = None
