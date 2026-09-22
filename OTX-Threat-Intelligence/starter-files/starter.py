import json


def fetch_threat_intelligence():
    """Stub loader — returns None; replaced with mock data in otx.py."""
    return None


def parse_threat_intelligence(data):
    """
    TODO:
    - If no usable results are returned (e.g., None or empty results),
      exit gracefully.
    - For each pulse: extract name, tags, indicators
    - Assign priority: HIGH / MEDIUM / LOW (case-insensitive tag logic)
    - Compute indicator count for each pulse
    - Write a report to 'otx_intelligence_report.txt'
    """
    pass