import subprocess
import string
import random
import re


def get_random_mac_address():
    """
    Generate a random MAC address.

    Returns:
        str: The generated MAC address.
    """
    # get the hexdigits uppercased
    uppercased_hexdigits = ''.join(set(string.hexdigits.upper()))
    # 2nd character must be 0, 2, 4, 6, 8, A, C, or E
    mac = ""
    for i in range(6):
        for j in range(2):
            if i == 0:
                mac += random.choice("02468ACE")
            else:
                mac += random.choice(uppercased_hexdigits)
        mac += ":"
    return mac.strip(":")

def get_current_mac_address(iface):
    """
    Get the current MAC address of a network interface.

    Args:
        iface (str): The name of the network interface.

    Returns:
        str: The current MAC address.
    """
    # use the ifconfig command to get the interface details, including the MAC address
    output = subprocess.check_output(f"ifconfig {iface}", shell=True).decode()
    return re.search("ether (.+) ", output).group().split()[1].strip()

def change_mac_address(iface, new_mac_address):
    """
    Change the MAC address of a network interface.

    Args:
        iface (str): The name of the network interface.
        new_mac_address (str): The new MAC address to set.
    """
    # disable the network interface
    subprocess.check_output(f"ifconfig {iface} down", shell=True)
    # change the MAC
    subprocess.check_output(f"ifconfig {iface} hw ether {new_mac_address}", shell=True)
    # enable the network interface again
    subprocess.check_output(f"ifconfig {iface} up", shell=True)
    
def generate_and_change_mac(iface):
    """
    Generate a new MAC address and change the current MAC address of a network interface.

    Args:
        iface (str): The name of the network interface.

    Returns:
        str: The new MAC address.
    """
    new_mac_address = get_random_mac_address()
    old_mac_address = get_current_mac_address(iface)
    print("[*] Old MAC address:", old_mac_address)
    # change the MAC address
    change_mac_address(iface, new_mac_address)
    # check if it's really changed
    new_mac_address = get_current_mac_address(iface)
    print("[+] New MAC address:", new_mac_address)
    return(new_mac_address)