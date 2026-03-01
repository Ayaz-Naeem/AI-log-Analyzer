from agents.log_agent import analyze_logs
from agents.cve_agent import cve_agent
from agents.mitre_agent import mitre_agent
from agents.report_agent import report_agent

def main():
    # Load logs
    with open("sample_logs.txt", "r") as f:
        logs = f.read()

    print("\n" + "="*50)
    print("🤖 MULTI-AGENT SECURITY ANALYSIS STARTING")
    print("="*50)

    # Agent 1
    print("\n[Agent 1] 📋 Analyzing logs...")
    log_analysis = analyze_logs(logs)
    print("✅ Log analysis complete")

    # Agent 2
    print("\n[Agent 2] 🔍 Searching CVE database...")
    keywords, cve_results = cve_agent(log_analysis)
    print("✅ CVE lookup complete")

    # Agent 3
    print("\n[Agent 3] 🗺️  Mapping to MITRE ATT&CK...")
    mitre_mapping = mitre_agent(log_analysis, cve_results)
    print("✅ MITRE mapping complete")

    # Agent 4
    print("\n[Agent 4] 📝 Generating final report...")
    final_report, filename = report_agent(log_analysis, cve_results, mitre_mapping, keywords)
    print(f"✅ Report saved to: {filename}")

    print("\n" + "="*50)
    print("📊 FINAL REPORT PREVIEW")
    print("="*50)
    print(final_report)

if __name__ == "__main__":
    main()