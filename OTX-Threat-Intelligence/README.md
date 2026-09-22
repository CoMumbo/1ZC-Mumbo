# OTX Threat Intelligence

**Type:** Lab
**Status:** Complete

## Objective

Build a Python script that:

- Loads a set of threat intelligence pulses
- Extracts pulse names, tags, and indicators
- Assigns a priority (HIGH/LOW) based on tags
- Writes a formatted report to `otx_intelligence_report.txt`

## Priority logic

Tags are checked case-insensitively. Pulses containing any of the
following tags are marked HIGH; everything else is LOW:

- `ransomware`
- `phishing`
- `apt`
- `malware`

## Files

| File | Purpose |
|---|---|
| `problem-statement.txt` | Assignment brief from Canvas |
| `starter-files/otx_starter.py` | Original starter code |
| `otx.py` | Solution script |
| `otx_intelligence_report.txt` | Generated report (sample output) |

## How to run

    cd OTX-Threat-Intelligence
    python otx.py

This produces `otx_intelligence_report.txt` in the current directory.

## Concepts used

- Functions and modular design
- JSON parsing
- Sets for fast tag matching
- File I/O
- F-strings and formatting
