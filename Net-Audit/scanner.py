import socket
import sys

def scan_port(ip, port):
    """
    Scans a specific port on the target IP.
    """
    try:
        # 1. Create the socket object
        # socket.AF_INET = IPv4 Address Family
        # socket.SOCK_STREAM = TCP Protocol
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # 2. Set timeout
        # If the port doesn't respond within 1 second, we assume it's filtered/closed.
        # This prevents the script from hanging on unresponsive hosts.
        s.settimeout(1)
        
        # 3. Attempt connection
        # connect_ex is like connect(), but returns an error indicator instead of raising an exception.
        # 0 = Success (Port Open)
        result = s.connect_ex((ip, port))
        
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        else:
            # Optional: You could print closed ports here, but it creates too much noise.
            pass
        
        # 4. Always close the connection
        s.close()
        
    except socket.error as e:
        print(f"[!] Socket error: {e}")
    except Exception as e:
        print(f"[!] General error: {e}")

if __name__ == "__main__":
    # Basic configuration for testing
    # In the next version, we will handle arguments via CLI
    target_ip = "8.8.8.8"  # Google DNS
    
    print(f"[*] Starting generic TCP scan on {target_ip}...")
    
    # Scanning common ports
    target_ports = [21, 22, 53, 80, 443]
    
    for port in target_ports:
        scan_port(target_ip, port)
