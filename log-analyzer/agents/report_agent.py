import os
from groq import Groq
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def report_agent(log_analysis, cve_results, mitre_mapping, keywords):
    prompt = f"""
    You are a senior cybersecurity analyst writing an executive incident report.
    Combine all findings below into a clean, professional security report with these sections:

    1. EXECUTIVE SUMMARY (2-3 sentences, non-technical)
    2. INCIDENT OVERVIEW
    3. ATTACK TIMELINE
    4. CVE VULNERABILITIES IDENTIFIED
    5. MITRE ATT&CK MAPPING
    6. RISK SEVERITY (Critical / High / Medium / Low + justification)
    7. IMMEDIATE ACTIONS REQUIRED
    8. LONG-TERM RECOMMENDATIONS

    LOG ANALYSIS:
    {log_analysis}

    CVE FINDINGS:
    {cve_results}

    MITRE MAPPING:
    {mitre_mapping}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a senior cybersecurity analyst writing professional incident reports."},
            {"role": "user", "content": prompt}
        ]
    )

    report = response.choices[0].message.content

    # Save with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"security_report_{timestamp}.txt"
    
    with open(filename, "w") as f:
        f.write(f"SECURITY INCIDENT REPORT\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Keywords Analyzed: {', '.join(keywords)}\n")
        f.write("="*60 + "\n\n")
        f.write(report)

    return report, filename