import socket
import struct
import threading
import logging

# Configure logging
logging.basicConfig(filename='network_traffic_log.txt', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Define the network interface (Use "eth0" for Linux, "Wi-Fi" or "Ethernet" for Windows)
NETWORK_INTERFACE = "eth0"  # Change accordingly

# Function to parse and analyze captured packets
def packet_analyzer(packet):
    try:
        # Extract IP header (first 20 bytes)
        ip_header = packet[0:20]
        iph = struct.unpack('!BBHHHBBH4s4s', ip_header)

        version = iph[0] >> 4
        ip_header_len = (iph[0] & 0xF) * 4
        ttl = iph[5]
        protocol = iph[6]
        source_ip = socket.inet_ntoa(iph[8])
        dest_ip = socket.inet_ntoa(iph[9])

        # Determine protocol type
        protocol_name = "UNKNOWN"
        if protocol == 6:
            protocol_name = "TCP"
        elif protocol == 17:
            protocol_name = "UDP"

        log_message = (f"IP Version: {version}, Header Length: {ip_header_len}, TTL: {ttl}, "
                       f"Protocol: {protocol_name} ({protocol}), Source IP: {source_ip}, "
                       f"Destination IP: {dest_ip}")

        logging.info(log_message)

        # Detect possible malicious traffic
        if protocol == 6:  # TCP
            tcp_header = packet[ip_header_len:ip_header_len + 20]
            tcph = struct.unpack('!HHLLBBHHH', tcp_header)
            src_port = tcph[0]
            dst_port = tcph[1]

            logging.info(f"TCP Packet - Source Port: {src_port}, Destination Port: {dst_port}")

            if dst_port in [445, 3389]:  # Common ransomware ports
                logging.warning(f"⚠️ Possible ransomware-related traffic detected to port {dst_port} from {source_ip}")

        elif protocol == 17:  # UDP
            udp_header = packet[ip_header_len:ip_header_len + 8]
            udph = struct.unpack('!HHHH', udp_header)
            src_port = udph[0]
            dst_port = udph[1]

            logging.info(f"UDP Packet - Source Port: {src_port}, Destination Port: {dst_port}")

        # Additional detection rules can be implemented based on traffic patterns

    except Exception as e:
        logging.error(f"Error analyzing packet: {e}")

# Function to capture packets using raw socket
def packet_capture():
    try:
        # Create a raw socket
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)

        # Bind to network interface
        s.bind((NETWORK_INTERFACE, 0))

        # Set the socket to capture incoming packets
        s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

        logging.info(f"Started capturing packets on {NETWORK_INTERFACE}...")

        while True:
            packet, _ = s.recvfrom(65565)
            packet_analyzer(packet)

    except PermissionError:
        logging.error("Permission denied! Run the script as an administrator/root.")
    except Exception as e:
        logging.error(f"Error in packet capture: {e}")

# Start network traffic monitoring in a separate thread
def start_network_traffic_analysis():
    try:
        analysis_thread = threading.Thread(target=packet_capture, daemon=True)
        analysis_thread.start()
        logging.info("Network traffic monitoring started.")
    except Exception as e:
        logging.error(f"Error in starting traffic analysis thread: {e}")

# Run the module
if __name__ == "__main__":
    start_network_traffic_analysis()
