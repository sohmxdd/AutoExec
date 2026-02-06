# AutoExec 
### **Self-Healing Code Execution Engine**

AutoExec is a developer tool that runs code, detects failures, fixes them using an LLM, retries execution, and remembers the fix so the same error is instantly resolved next time.

Think of it as an intelligent execution layer that sits between your code and runtime errors.
<img width="790" height="693" alt="image" src="https://github.com/user-attachments/assets/97f4a9b1-857d-4c9f-b8c0-a1d3b04f6f52" />

---

##  Why AutoExec?

* **Stop wasting time** fixing repetitive runtime errors.
* **Automatically debug** crashes and failing tests.
* **Learn from past fixes** using persistent memory.
* **Inspect every change** via diffs (no black boxes).
* **Designed to grow** into CI tools, dashboards, and hosted sandboxes.
<img width="776" height="396" alt="image" src="https://github.com/user-attachments/assets/2c2468cc-a381-4806-9f18-f6dc06a327f7" />

---

##  Core Features

* **Self-healing execution:** Detects runtime errors and retries with fixes.
* **LLM-powered fixes:** Uses an LLM to propose minimal, targeted code changes.
* **Fix memory:** Successful fixes are stored in `memory.json` and reused instantly.
* **Test-aware:** Can run tests (assert snippets) and fix logic errors, not just crashes.
* **Local execution backend:** Runs code safely via temporary files on your machine.
* **CLI support:** Run files directly from the terminal.
* **Diff visualization:** Every fix is shown as a unified diff for transparency.

---

## 📂 Project Structure

```text
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
├─ ui/
   └─ index.html      # Optional UI
```
## Quick Start

```text
1️⃣ Setup

git clone [https://github.com/sohmxdd/AutoExec.git](https://github.com/sohmxdd/AutoExec.git)
cd AutoExec

python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
# source venv/bin/activate

pip install -r requirements.txt
2️⃣ Configure API Keys
Create a .env file for LLM support:

Code snippet:

GROQ_API_KEY=your_key_here
# or
GEMINI_API_KEY=your_key_here
3️⃣ Basic Python Example
Python

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

print("SUCCESS:", result.success)
```
---
## CLI Usage
Run a Python file:

Bash

python -m autoexec run path/to/file.py
Run with tests:

Bash

python -m autoexec run path/to/file.py --tests "assert 'hello' in output"

## 🤝 Contributing
Contributions are welcome!
Star the Project 🌟 - It helps others discover the tool!

Fork the Project - Create your own copy to experiment.

Open an Issue - Report bugs or suggest new features.

Create a Pull Request - Submit your changes for review.
Please do not commit .env or memory.json.


---

### How to commit and push this:

Now that your rebase is finished, follow these steps to finish the job:

1.  **Save the file:** Paste the code above into your `README.md` and save it.
2.  **Stage the update:**
    ```bash
    git add README.md
    ```
3.  **Commit the formatting fix:**
    ```bash
    git commit -m "docs: fix README formatting and structure"
    ```
4.  **Push everything to GitHub:**
    ```bash
    git push origin main
    ```



