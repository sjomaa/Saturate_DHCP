# DHCP Server Testing Tool

This tool sends a specified number of DHCP discovery requests to a DHCP server. Each time a request is sent, the MAC address of the network card is changed. This allows the tool to receive responses from the DHCP server.

## Dependencies

This tool requires the following Python libraries:

- Scapy
- argparse

You can install these dependencies using pip:

```bash
sudo pip3 install scapy argparse
```
## Usage

To use this tool, you need to run the DHCP.py script with sudo, as it uses system commands. You also need to specify the number of DHCP requests to send and the name of the network interface to use.

Here's an example command:
```bash
sudo python3 DHCP.py -n 210 -i eth0
```
This command sends 210 DHCP requests using the eth0 interface.

## Note
Please ensure you have the necessary permissions to change the MAC address of your network card and to send DHCP requests.


