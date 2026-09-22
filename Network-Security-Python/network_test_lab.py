"""
network_test_lab.py

Lab: Implementing Network Security with Python

A network auditing tool that checks interfaces, connectivity, DNS,
listening ports, and administrative permissions.
"""

import os
import socket
import subprocess
import sys


def check_local_listeners():
    """Display processes listening on open ports in a tabular format."""
    print("PROCESS    PID    IP             PORT")
    try:
        result = subprocess.run(
            ["ss", "-tulnp"],
            capture_output=True,
            text=True,
            check=True,
        )
        for line in result.stdout.splitlines()[1:]:
            parts = line.split()
            if len(parts) < 5:
                continue
            local = parts[4]
            ip, _, port = local.rpartition(":")
            process = parts[-1]
            print(f"{process:<10} {'':<6} {ip:<14} {port}")
    except (subprocess.CalledProcessError, FileNotFoundError) as err:
        print(f"Error retrieving listeners: {err}")


def check_permissions():
    """Exit with code 1 if not running as root."""
    if os.geteuid() != 0:
        print("ERROR: This script must be run with administrative privileges.")
        print("USAGE: sudo python3 network_test_lab.py")
        sys.exit(1)


def dns_ping_test():
    """Test DNS resolution against flatironschool.com."""
    domain = "flatironschool.com"
    try:
        resolved = socket.gethostbyname(domain)
        print(f"DNS resolution for {domain}: {resolved}")
    except socket.gaierror as err:
        print(f"DNS resolution failed for {domain}: {err}")


def get_local_ips():
    """Display IPv4 and IPv6 addresses for all network interfaces."""
    try:
        result = subprocess.run(
            ["ip", "-o", "addr"],
            capture_output=True,
            text=True,
            check=True,
        )
        for line in result.stdout.splitlines():
            parts = line.split()
            iface = parts[1]
            family = parts[2]
            addr = parts[3].split("/")[0]
            label = "IPv4" if family == "inet" else "IPv6"
            print(f"Interface: {iface}")
            print(f"  - {label}: {addr}")
    except (subprocess.CalledProcessError, FileNotFoundError) as err:
        print(f"Error retrieving interfaces: {err}")


def ping_test():
    """Ping Google's public DNS server to test connectivity."""
    target = "8.8.8.8"
    try:
        result = subprocess.run(
            ["ping", "-c", "1", target],
            capture_output=True,
            text=True,
            check=True,
        )
        print(result.stdout)
    except (subprocess.CalledProcessError, FileNotFoundError) as err:
        print(f"Ping failed for {target}: {err}")


def main():
    """Run the network audit."""
    check_permissions()
    get_local_ips()
    ping_test()
    dns_ping_test()
    check_local_listeners()


if __name__ == "__main__":
    main()