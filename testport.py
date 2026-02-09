import socket

def scan_ports(host, port_range):
    print(f"Scanning {host}...")
    for port in port_range:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)  # Set timeout to 1 second
            result = sock.connect_ex((host, port))
            if result == 0:
                print(f"Port {port} is open.")
            else:
                print(f"Port {port} is closed.")

if __name__ == "__main__":
    target_host = input("Enter target IP or hostname: ")
    start_port = 1
    end_port = 1024
    ports = range(start_port, end_port)
    scan_ports(target_host, ports)
