"""
Run with:
python -m autoexec.examples.test_agent
"""

from autoexec.agent import AutoExecAgent

agent = AutoExecAgent()


result = agent.run(
    code="""
print("Looping forever")
while True:
    pass
"""
)

print("\n=== FINAL RESULT ===")
print("STDOUT:", result.stdout)
print("SUCCESS:", result.success)
