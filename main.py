import argparse
from device_manager import load_devices, fetch_device_output
from analyzer import analyze_interfaces
from report_generator import generate_html_dashboard
from logger import setup_logger
import logging


def calculate_health(result):
    total = len(result)
    down = sum(1 for item in result if item[1] == "DOWN")

    if total == 0:
        return 0, 0, "NO DATA"

    health = ((total - down) / total) * 100

    if health == 100:
        status = "HEALTHY"
    elif health >= 70:
        status = "STABLE"
    else:
        status = "CRITICAL"

    return total, down, health, status


if __name__ == "__main__":
    setup_logger()

    parser = argparse.ArgumentParser(description="Network Monitoring Toolkit")
    parser.add_argument("--config", default="config/devices.yaml")
    parser.add_argument("--demo", action="store_true", help="Run in simulation mode")

    args = parser.parse_args()

    devices = load_devices(args.config)

    # 🔥 This will store all device results for dashboard
    all_devices_data = []

    for device in devices:
        print(f"\nConnecting to {device['name']}...")

        output = fetch_device_output(device, demo=args.demo)

        result = analyze_interfaces(output)

        total, down, health, status = calculate_health(result)

        print("----------------------------------------")
        print(f"Device Name     : {device['name']}")
        print(f"Health Score    : {health:.2f}%")
        print(f"Overall Status  : {status}")
        print("----------------------------------------")

        logging.info(f"{device['name']} - {status} - {health:.2f}%")

        # 🔥 Store data for dashboard
        all_devices_data.append({
            "name": device["name"],
            "total": total,
            "down": down,
            "health": health,
            "status": status
        })

    # 🔥 Generate HTML dashboard AFTER processing all devices
    generate_html_dashboard(all_devices_data)

    print("\n📊 Dashboard generated: reports/dashboard.html")