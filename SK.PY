pip install scapy
import scapy.all as scapy

def packet_callback(packet):
    print(packet.show())

# Start sniffing on all interfaces
scapy.sniff(prn=packet_callback, store=0)
            def packet_callback(packet):
    if packet.haslayer(scapy.IP):
        ip_src = packet[scapy.IP].src
        ip_dst = packet[scapy.IP].dst
        print(f"Packet from {ip_src} to {ip_dst}")
        if packet.haslayer(scapy.TCP):
            print("TCP packet detected!")
        if packet.haslayer(scapy.UDP):
            print("UDP packet detected!")

# Start sniffing HTTP traffic
scapy.sniff(filter="tcp port 80", prn=packet_callback, store=0)
            def packet_callback(packet):
    print(packet.summary())

# Sniff and save packets to a file
scapy.sniff(filter="tcp port 80", prn=packet_callback, store=1, count=10)
            packets = scapy.sniff(count=10, filter="tcp port 80")
scapy.wrpcap("captured_packets.pcap", packets)
             def packet_callback(packet):
    if packet.haslayer(scapy.IP):
        ip_src = packet[scapy.IP].src
        ip_dst = packet[scapy.IP].dst
        print(f"Source IP: {ip_src} -> Destination IP: {ip_dst}")
        
        if packet.haslayer(scapy.TCP):
            tcp_src_port = packet[scapy.TCP].sport
            tcp_dst_port = packet[scapy.TCP].dport
            print(f"TCP Packet - Source Port: {tcp_src_port}, Destination Port: {tcp_dst_port}")
        
        if packet.haslayer(scapy.Raw):
            payload = packet[scapy.Raw].load
            print(f"Raw Data: {payload}")

# Start sniffing with more detailed analysis
scapy.sniff(prn=packet_callback, store=0, filter="tcp")
            import scapy.all as scapy

def packet_callback(packet):
    if packet.haslayer(scapy.IP):
        ip_src = packet[scapy.IP].src
        ip_dst = packet[scapy.IP].dst
        print(f"Source IP: {ip_src} -> Destination IP: {ip_dst}")
        
    if packet.haslayer(scapy.TCP):
        tcp_src_port = packet[scapy.TCP].sport
        tcp_dst_port = packet[scapy.TCP].dport
        print(f"TCP Packet - Source Port: {tcp_src_port}, Destination Port: {tcp_dst_port}")
        
    if packet.haslayer(scapy.UDP):
        udp_src_port = packet[scapy.UDP].sport
        udp_dst_port = packet[scapy.UDP].dport
        print(f"UDP Packet - Source Port: {udp_src_port}, Destination Port: {udp_dst_port}")
    
    if packet.haslayer(scapy.Raw):
        payload = packet[scapy.Raw].load
        print(f"Raw Data: {payload}")

# Start sniffing on all interfaces and filter only TCP and UDP
scapy.sniff(prn=packet_callback, store=0, filter="tcp or udp")