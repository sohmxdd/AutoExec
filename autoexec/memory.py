import json
from pathlib import Path

MEMORY_FILE = Path("memory.json")


class FixMemory:
    def __init__(self):
        if MEMORY_FILE.exists():
            self.data = json.loads(MEMORY_FILE.read_text())
        else:
            self.data = {}

    def get(self, error_type: str):
        return self.data.get(error_type)

    def store(self, error_type: str, fixed_code: str):
        self.data[error_type] = fixed_code
        MEMORY_FILE.write_text(json.dumps(self.data, indent=2))
