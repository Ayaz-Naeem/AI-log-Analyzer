import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_logs(log_text):
    prompt = f"""
    Analyze these logs and extract:
    1. What type of attack or event occurred
    2. Which services or software are involved (e.g. SSH, Apache, Windows)
    3. Source IPs
    4. Key keywords I should search for in CVE databases

    Return your answer in clear labeled sections.

    LOGS:
    {log_text}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a SOC analyst expert at reading system logs."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content