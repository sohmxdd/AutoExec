"""
Run with:
python -m autoexec.examples.test_agent
"""

from autoexec.agent import AutoExecAgent

agent = AutoExecAgent()


result = agent.run(
    code="""
print("Hello!")
"""
)

print("\n=== FINAL RESULT ===")
print("STDOUT:", result.stdout)
print("SUCCESS:", result.success)
