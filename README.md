# CodeAlpha Network Sniffer

A basic network sniffer built with **Python and Scapy** as part of the CodeAlpha Cyber Security Internship.

The program captures network packets and analyzes basic packet information such as source and destination IP addresses, protocols, ports, and payload data.

## Features

* Capture network packets using Scapy
* Display source IP address
* Display destination IP address
* Identify network protocols such as TCP and UDP
* Display source and destination ports
* Calculate payload size
* Display a small preview of the captured payload
* Handle packets that do not contain TCP or UDP information

## Technologies Used

* **Python 3.13**
* **Scapy 2.7.0**
* **Npcap**
* **Visual Studio Code**

## How It Works

The program uses Scapy's `sniff()` function to capture a specified number of packets.

For each captured packet, the program:

1. Checks whether the packet contains an IP layer.
2. Extracts the source and destination IP addresses.
3. Checks whether the packet uses TCP or UDP.
4. Extracts the source and destination ports.
5. Checks whether the packet contains a Raw payload.
6. Calculates the payload length.
7. Displays the first 20 bytes of the payload as a preview.

## Example Output

```text
Starting packet capture...
Packet capture complete!

Source IP: 192.168.100.5
Destination IP: 57.144.149.32
Protocol: TCP
Source Port: 64414
Destination Port: 443
Payload Length: 75
Payload Preview: b'\x17\x03\x03\x00F\x83\xcdl...'
-------------------------
```

## Project Structure

```text
CodeAlpha_NetworkSniffer/
│
├── sniffer.py
└── README.md
```

## Installation

### 1. Install Python

Make sure Python is installed on your system.

### 2. Install Scapy

Open a terminal and run:

```bash
py -3.13 -m pip install scapy
```

### 3. Install Npcap

On Windows, Npcap is required by Scapy for packet capture.

Install Npcap with the appropriate options for your system.

### 4. Run the Program

Navigate to the project directory and run:

```bash
py -3.13 sniffer.py
```

The program will capture 5 packets and display their information.

## Important Note

Network packet capture should only be performed on networks and systems that you own or have explicit permission to monitor.

Also, HTTPS traffic is encrypted. Therefore, the payload preview may appear as seemingly random bytes rather than readable application data.

## Learning Objectives

This project helped me understand:

* How network packets are structured
* Source and destination IP addresses
* TCP and UDP protocols
* Source and destination ports
* Packet payloads
* Basic network traffic analysis
* Using Python and Scapy for cybersecurity tasks

## Internship

**CodeAlpha Cyber Security Internship**

**Task 1: Basic Network Sniffer**

Built as part of the CodeAlpha Cyber Security Internship program.