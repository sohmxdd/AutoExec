AutoExec 🚀Self-Healing Code Execution EngineAutoExec is a developer-first execution layer that runs code, detects failures, and automatically heals them using Large Language Models (LLMs). It doesn't just fix errors—it remembers them, ensuring that the same runtime crash never slows you down twice.💡 Why AutoExec?Kill Repetitive Debugging: Stop fixing the same logic flaws and runtime crashes manually.Autonomous Testing: Automatically debug and patch failing tests in your suite.Persistent Learning: Uses local memory to "learn" from past fixes, providing instant resolutions for recurring issues.Full Transparency: Inspect every automated change via unified diffs. No "black box" code modification.Scalable Architecture: Designed to evolve from a local CLI tool into a CI/CD powerhouse.✨ Core FeaturesFeatureDescriptionSelf-Healing LoopAutomatically catches exceptions and retries execution with injected fixes.LLM-Powered FixesLeverages Groq or Gemini to propose minimal, targeted code changes.Fix MemorySuccessful patches are stored in memory.json for O(1) retrieval in future runs.Test-AwareSupports assertion snippets to fix logic errors even if the code doesn't "crash."Hybrid BackendsChoose between stable Local execution or experimental Daytona sandboxes.CLI FirstNative terminal support for seamless integration into existing workflows.📂 Project StructurePlaintextAutoExec/
├─ autoexec/
│  ├─ agent.py         # Core retry + fix loop
│  ├─ core.py          # Execution interfaces & result types
│  ├─ llm.py           # LLM integration (Groq / Gemini)
│  ├─ memory.py        # Persistent fix memory logic
│  ├─ diff.py          # Unified diff visualization helper
│  ├─ tester.py        # Test runner & assertion logic
│  ├─ cli.py           # CLI entrypoint
│  └─ backends/        # Local & Sandboxed execution providers
├─ examples/           # Sample scripts and use cases
├─ .env                # API keys (Secrets)
├─ memory.json         # Local fix database
└─ README.md
🚀 Quick Start1️⃣ SetupBash# Clone the repository
git clone https://github.com/<your-username>/AutoExec.git
cd AutoExec

# Setup environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
2️⃣ Configure LLMCreate a .env file in the root directory:Code snippetGROQ_API_KEY=your_key_here
# OR
GEMINI_API_KEY=your_key_here
3️⃣ Basic Usage (Python API)Pythonfrom autoexec.agent import AutoExecAgent

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

print(f"Success: {result.success}")
print(f"Output: {result.stdout}")
🖥️ CLI UsageRun any Python file directly through the self-healing engine:Bash# Standard run
python -m autoexec run path/to/file.py

# Run with specific test assertions
python -m autoexec run script.py --tests "assert 'hello' in output"
🛡️ Safety & ConstraintsNon-Fixable ErrorsTo prevent infinite loops and unsafe states, AutoExec will not attempt to fix:Execution TimeoutsBackend/Docker/Sandbox infrastructure failuresKeyboardInterrupt (Manual stops)SecurityDiff Visualization: Every fix is shown as a diff for user approval.Local Memory: memory.json stays on your machine and is ignored by Git.Sandbox Ready: Support for Daytona ensures code can be run in isolated environments.🗺️ Roadmap[x] Phase 1: Core agent loop, Local backend, CLI, and Memory.[ ] Phase 2: Advanced prompting, CI/CD integration, and logic-heavy reasoning.[ ] Phase 3: Web Dashboard for visual memory exploration and pip install autoexec.[ ] Phase 4: Stable Sandbox backends and opt-in cloud-shared fix memory.🤝 ContributingContributions are what make the open-source community amazing!Fork the ProjectCreate your Feature Branch (git checkout -b feature/AmazingFeature)Commit your Changes (git commit -m 'Add AmazingFeature')Push to the Branch (git push origin feature/AmazingFeature)Open a Pull RequestNote: Please ensure you do not commit your .env or memory.json files.
