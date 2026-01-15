import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise RuntimeError("GROQ_API_KEY not found in environment")

client = Groq(api_key=api_key)


def fix_code(code: str, error_type: str, error_message: str) -> str:
    prompt = f"""
You are a senior Python engineer.

The following Python code failed:

--- CODE ---
{code}
--- END CODE ---

Error:
{error_type}: {error_message}

Fix the code.

Rules:
- Return ONLY valid Python code
- Do NOT explain
- Do NOT use markdown
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You fix broken Python code."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content.strip()
