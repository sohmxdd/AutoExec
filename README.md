AutoExec 🚀

Self-Healing Code Execution Engine

AutoExec is a developer tool that runs code, detects failures, fixes them using an LLM, retries execution, and remembers the fix so the same error is instantly resolved next time.

Think of it as an intelligent execution layer that sits between your code and runtime errors.

 Why AutoExec?

Stop wasting time fixing repetitive runtime errors

Automatically debug crashes and failing tests

Learn from past fixes using persistent memory

Inspect every change via diffs (no black boxes)

Designed to grow into CI tools, dashboards, and hosted sandboxes

 Core Features

Self-healing execution
Detects runtime errors and retries with fixes.

LLM-powered fixes
Uses an LLM to propose minimal, targeted code changes.

Fix memory
Successful fixes are stored in memory.json and reused instantly.

Test-aware
Can run tests (assert snippets) and fix logic errors, not just crashes.

Local execution backend (stable)
Runs code safely via temporary files on your machine.

Daytona backend (experimental / disabled by default)
Planned support for sandboxed execution.

CLI support
Run files directly from the terminal.

Diff visualization
Every fix is shown as a unified diff for transparency.

📂 Project Structure
AutoExec/
├─ autoexec/
│  ├─ agent.py        # Core retry + fix loop
│  ├─ core.py         # Execution interfaces & result types
│  ├─ llm.py          # LLM integration (Groq / Gemini, etc.)
│  ├─ memory.py       # Persistent fix memory
│  ├─ diff.py         # Unified diff helper
│  ├─ tester.py       # Test runner
│  ├─ cli.py          # CLI entrypoint
│  └─ backends/
│     ├─ local.py     # Local execution backend
│     └─ daytona.py   # Experimental sandbox backend
├─ examples/
│  └─ test_agent.py   # Example usage
├─ .env               # API keys (ignored)
├─ memory.json        # Runtime fix memory (ignored)
└─ README.md

 Quick Start
1️⃣ Setup
git clone https://github.com/<your-username>/AutoExec.git
cd AutoExec

python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
# source venv/bin/activate

pip install -r requirements.txt


Create a .env file if you want LLM support:

GROQ_API_KEY=your_key_here
# or
GEMINI_API_KEY=your_key_here

2️⃣ Basic Python Example
from autoexec.agent import AutoExecAgent

agent = AutoExecAgent()

result = agent.run(
    code="""
print("About to crash")
1 / 0
""",
    tests="""
assert "Cannot divide by zero" in output
"""
)

print("STDOUT:")
print(result.stdout)
print("SUCCESS:", result.success)


What happens internally:

Code crashes with ZeroDivisionError

AutoExec asks the LLM for a fix

Applies the fix and retries

Tests pass

Fix is stored in memory for next time

🖥️ CLI Usage

Run a Python file:

python -m autoexec run path/to/file.py


Run with tests:

python -m autoexec run path/to/file.py --tests "assert 'hello' in output"

🧠 Fix Memory

Successful fixes are saved to memory.json

Future runs reuse known fixes instantly

Memory is local, transparent, and editable

File is ignored by git by default

⛔ Non-Fixable Errors

AutoExec automatically aborts retries for errors that cannot be safely fixed by an LLM, such as:

Timeouts

Backend / Docker / Sandbox failures

KeyboardInterrupts

This prevents infinite loops and unsafe behavior.

 Safety & Transparency

No silent code changes — every fix shows a diff

Secrets live in .env (never committed)

Memory is local and under your control

Daytona backend is disabled by default for safety

 Roadmap

Phase 1 (current)

Core agent loop

Local backend

LLM fixes + memory

CLI

Phase 2

Better prompt strategies

More test-aware reasoning

CI integration examples

Phase 3

Web dashboard (runs, diffs, memory explorer)

pip install autoexec

Phase 4

Stable sandbox backend

Collaborative / shared fix memory (opt-in)

🤝 Contributing

Contributions are welcome!

Good first contributions:

New example scripts

CLI flags (--dry-run, --verbose)

LLM prompt improvements

Test coverage

Please do not commit .env or memory.json.
