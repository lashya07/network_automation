def analyze_interfaces(cli_output):
    lines = cli_output.splitlines()
    result = []

    for line in lines:
        if "GigabitEthernet" in line:
            parts = line.split()
            interface = parts[0]
            status = parts[-1]

            if status.lower() == "up":
                state = "UP"
            else:
                state = "DOWN"

            result.append([interface, state])

    return result