from scapy.all import sniff, IP, TCP, UDP, Raw

print("Starting packet capture...")

packets = sniff(count=5)

print("Packet capture complete!")

for packet in packets:
    if IP in packet:

        source_ip = packet[IP].src
        destination_ip = packet[IP].dst

        if TCP in packet:
            protocol = "TCP"
            source_port = packet[TCP].sport
            destination_port = packet[TCP].dport

        elif UDP in packet:
            protocol = "UDP"
            source_port = packet[UDP].sport
            destination_port = packet[UDP].dport

        else:
            protocol = "Other"
            source_port = "-"
            destination_port = "-"

        if Raw in packet:
            payload_length = len(packet[Raw].load)
            payload_preview = packet[Raw].load[:20]
        else:
            payload_length = 0
            payload_preview = b""

        print("Source IP:", source_ip)
        print("Destination IP:", destination_ip)
        print("Protocol:", protocol)
        print("Source Port:", source_port)
        print("Destination Port:", destination_port)
        print("Payload Length:", payload_length)
        print("Payload Preview:", payload_preview)
        print("-------------------------")