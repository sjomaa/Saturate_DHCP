import random
from scapy.all import Ether, IP, UDP, BOOTP, DHCP, srp1
import MAC_Changer

# Dictionary to store transaction IDs for each MAC address
mac_xid = {}

def mac2str(mac):
    """Convert a MAC address from string format to binary format."""
    return ''.join(chr(int(x, 16)) for x in mac.split(':'))

def dhcp_request(mac_address):
    """Send a DHCP request and return the offered IP address."""
    # Generate a random transaction ID for this MAC address if it doesn't have one
    if mac_address not in mac_xid:
        mac_xid[mac_address] = random.randint(0x0, 0xffffffff)

    # Create the DHCP request packet
    dhcp_request = Ether(src=mac_address, dst="ff:ff:ff:ff:ff:ff") / \
                   IP(src="0.0.0.0", dst="255.255.255.255") / \
                   UDP(sport=68, dport=67) / \
                   BOOTP(chaddr=mac2str(mac_address), xid=mac_xid[mac_address]) / \
                   DHCP(options=[("message-type", "request"), "end"])

    # Send the DHCP request and get the response
    response = srp1(dhcp_request, verbose=False, timeout=8)

def test_dhcp(num_requests):
    """Test the DHCP server by sending multiple requests."""
    for _ in range(num_requests):
        mac_address = MAC_Changer.generate_and_change_mac("wlo1")
        offered_ip = dhcp_request(mac_address)

# Replace with your DHCP server IP and the number of requests you want to send
test_dhcp(210)