"""
otx.py

Lab: Threat Intelligence with AlienVault OTX

Loads a set of threat intelligence pulses, parses them,
assigns a priority based on tags, and writes a report to
otx_intelligence_report.txt.
"""

import json

# Tags that trigger HIGH priority (case-insensitive)
HIGH_PRIORITY_TAGS = {"ransomware", "phishing", "apt", "malware"}

REPORT_PATH = "otx_intelligence_report.txt"


def fetch_threat_intelligence():
    """Return the threat intelligence payload (mock data)."""
    return load_mock_data()


def load_mock_data():
    """Return a small, realistic OTX-style dataset."""
    return {
        "results": [
            {
                "name": "APT29 Cozy Bear Campaign",
                "tags": ["apt", "russia", "malware"],
                "indicators": [
                    {"type": "domain", "indicator": "malicious.example.com"},
                    {"type": "IPv4", "indicator": "203.0.113.10"},
                    {"type": "file", "indicator": "deadbeefcafebabe"},
                ],
            },
            {
                "name": "Phishing Kit Targeting Banks",
                "tags": ["phishing", "credential-harvesting"],
                "indicators": [
                    {"type": "domain", "indicator": "fake-bank.example.net"},
                    {"type": "URL", "indicator": "http://fake-bank.example.net/login"},
                ],
            },
            {
                "name": "Generic Newsletter Spam",
                "tags": ["spam"],
                "indicators": [
                    {"type": "domain", "indicator": "spam.example.org"},
                ],
            },
            {
                "name": "LockBit Ransomware Variant",
                "tags": ["RansomWare", "extortion"],
                "indicators": [
                    {"type": "file", "indicator": "abc123def456"},
                    {"type": "IPv4", "indicator": "198.51.100.7"},
                    {"type": "domain", "indicator": "lockbit.example.com"},
                    {"type": "URL", "indicator": "http://lockbit.example.com/pay"},
                ],
            },
        ]
    }


def parse_threat_intelligence(data):
    """Validate, extract, prioritize, and report on OTX pulses."""
    if not data or not isinstance(data, dict):
        print("No usable threat intelligence data returned.")
        return

    results = data.get("results") or []
    if not results:
        print("No pulses found in the response.")
        return

    lines = ["OTX THREAT INTELLIGENCE REPORT", "=" * 40, ""]

    for pulse in results:
        name = pulse.get("name", "Unnamed Pulse")
        tags = pulse.get("tags", [])
        indicators = pulse.get("indicators", [])

        tag_set = {t.lower() for t in tags}
        priority = "HIGH" if tag_set & HIGH_PRIORITY_TAGS else "LOW"

        indicator_count = len(indicators)

        print(f"[{priority}] {name}")
        print(f"    Tags: {', '.join(tags) if tags else 'none'}")
        print(f"    Indicators: {indicator_count}")
        print()

        lines.append(f"[{priority}] {name}")
        lines.append(f"  Tags       : {', '.join(tags) if tags else 'none'}")
        lines.append(f"  Indicators : {indicator_count}")
        lines.append("")

    try:
        with open(REPORT_PATH, "w", encoding="utf-8") as report:
            report.write("\n".join(lines))
        print(f"Report written to {REPORT_PATH}")
    except OSError as err:
        print(f"Could not write report: {err}")


if __name__ == "__main__":
    payload = fetch_threat_intelligence()
    parse_threat_intelligence(payload)