import os
import requests
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def search_cves(keyword):
    """Search NVD for real CVEs - completely free, no API key needed"""
    url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch={keyword}&resultsPerPage=5"
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        
        cves = []
        for item in data.get("vulnerabilities", []):
            cve = item["cve"]
            cve_id = cve["id"]
            description = cve["descriptions"][0]["value"]
            score = cve.get("metrics", {}).get("cvssMetricV31", [{}])[0].get("cvssData", {}).get("baseScore", "N/A")
            cves.append(f"{cve_id} (Score: {score}): {description[:200]}")
        
        return cves if cves else ["No CVEs found for this keyword"]
    
    except Exception as e:
        return [f"CVE lookup failed: {str(e)}"]

def cve_agent(log_analysis):
    """Use AI to extract keywords then search CVEs"""
    
    # First use AI to pull out good search keywords from Agent 1's output
    keyword_prompt = f"""
    Based on this log analysis, give me 3 specific software/service keywords 
    to search for CVEs. Return ONLY the keywords, one per line, nothing else.
    
    Example output:
    OpenSSH
    Apache
    Windows SMB
    
    LOG ANALYSIS:
    {log_analysis}
    """
    
    keyword_response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You extract CVE search keywords from security reports."},
            {"role": "user", "content": keyword_prompt}
        ]
    )
    
    keywords = keyword_response.choices[0].message.content.strip().split("\n")
    keywords = [k.strip() for k in keywords if k.strip()][:3]  # max 3 keywords
    
    # Now search CVEs for each keyword
    all_cves = {}
    for keyword in keywords:
        print(f"  🔍 Searching CVEs for: {keyword}")
        all_cves[keyword] = search_cves(keyword)
    
    # Format results
    cve_results = ""
    for keyword, cves in all_cves.items():
        cve_results += f"\n--- {keyword} ---\n"
        for cve in cves:
            cve_results += f"  • {cve}\n"
    
    return keywords, cve_results