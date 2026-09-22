# Network Security with Python

**Type:** Lab
**Status:** Complete (pending Docker test)

## Objective

Build a network auditing tool in Python that:

- Lists active IPv4 and IPv6 network interfaces
- Tests connectivity to `8.8.8.8`
- Tests DNS resolution for `flatironschool.com`
- Audits open ports and listening processes
- Enforces administrative privileges

## Files

| File | Purpose |
|---|---|
| `problem-statement.txt` | Assignment brief from Canvas |
| `network_test_lab.py` | Solution script |

## Environment

Runs inside the Docker container `nwendlo1/c1w2m6` (Ubuntu 22.04, Python 3.12).

## How to run

    sudo python3 network_test_lab.py
