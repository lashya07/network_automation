import csv

def analyze_interfaces(file_name):
    with open(file_name, "r") as file:
        content = file.read()

    interfaces = content.split("\n\n")
    report_data = []

    for interface in interfaces:
        lines = interface.split("\n")
        if len(lines) > 0:
            first_line = lines[0]

            interface_name = first_line.split(" ")[0]

            if "administratively down" in first_line:
                status = "DOWN"
            elif "is up" in first_line:
                status = "UP"
            else:
                status = "UNKNOWN"

            report_data.append([interface_name, status])

    return report_data


def generate_report(data):
    with open("interface_report.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Interface Name", "Status"])
        writer.writerows(data)


if __name__ == "__main__":
    result = analyze_interfaces("show_ip_interface.txt")

    generate_report(result)

    # 🔹 Add this summary section here
    down_count = sum(1 for item in result if item[1] == "DOWN")

    print(f"Total Interfaces: {len(result)}")
    print(f"Interfaces Down: {down_count}")

    print("Automation Completed!")
    print("Report saved as interface_report.csv")