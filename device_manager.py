import yaml
import random


def load_devices(config_file):
    with open(config_file, "r") as file:
        data = yaml.safe_load(file)
    return data["devices"]


def generate_simulated_output():
    """
    Generates realistic Cisco 'show ip interface brief' output
    """

    interfaces = [
        "GigabitEthernet0/0",
        "GigabitEthernet0/1",
        "GigabitEthernet0/2",
        "GigabitEthernet0/3"
    ]

    output = "Interface              IP-Address      OK? Method Status                Protocol\n"

    for intf in interfaces:
        ip = f"192.168.{random.randint(1,10)}.{random.randint(1,254)}"

        # Randomly decide status
        if random.random() > 0.7:
            status = "administratively down"
            protocol = "down"
        else:
            status = "up"
            protocol = "up"

        output += f"{intf:<22} {ip:<15} YES manual {status:<20} {protocol}\n"

    return output


def fetch_device_output(device, demo=False):
    if demo:
        return generate_simulated_output()

    # Real router mode (will work only if router exists)
    from netmiko import ConnectHandler

    connection = ConnectHandler(**device)
    output = connection.send_command("show ip interface brief")
    connection.disconnect()

    return output