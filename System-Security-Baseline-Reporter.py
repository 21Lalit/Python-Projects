import platform
import socket
import os
from datetime import datetime


def get_ip_address():
    """
    Tries to get the local IP address of the system.
    Uses error handling in case IP detection fails.
    """
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except Exception as error:
        return f"Unable to fetch IP address: {error}"


def get_logged_in_user():
    """
    Gets the current logged-in user.
    """
    try:
        return os.getlogin()
    except Exception:
        return os.environ.get("USERNAME") or os.environ.get("USER") or "Unknown User"


def generate_system_report():
    """
    Gathers basic system security baseline information
    and returns it in formatted text.
    """

    try:
        system_type = platform.system()
        system_version = platform.version()
        system_release = platform.release()
        machine_type = platform.machine()
        processor = platform.processor()

        hostname = socket.gethostname()
        username = get_logged_in_user()
        ip_address = get_ip_address()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        report = f"""
========================================
 SYSTEM SECURITY BASELINE REPORT
========================================

Report Generated On : {timestamp}

[System Information]
System Type         : {system_type}
System Release      : {system_release}
System Version      : {system_version}
Machine Type        : {machine_type}
Processor           : {processor}

[Host Information]
Hostname            : {hostname}
Logged-in User      : {username}
IP Address          : {ip_address}

[Security Baseline Note]
This report provides basic system identification details.
It can be used as a starting point for system inventory,
security auditing, asset tracking, and automation tasks.

========================================
 End of Report
========================================
"""

        return report

    except Exception as error:
        return f"Error while generating system report: {error}"


def save_report_to_file(report_data):
    """
    Saves the generated report into system_report.txt
    """

    try:
        with open("system_report.txt", "w") as file:
            file.write(report_data)

        print("System report generated successfully.")
        print("Output saved to system_report.txt")

    except Exception as error:
        print(f"Error while saving report: {error}")


def main():
    report_data = generate_system_report()
    save_report_to_file(report_data)


if __name__ == "__main__":
    main()