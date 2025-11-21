import socket
import argparse
import concurrent.futures
from datetime import datetime

def grab_banner(ip, port):
    """
    Attempts to retrieve the service banner from an open port.
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1) 
        s.connect((ip, port))
        
        # Read bytes
        banner = s.recv(1024)
        s.close()
        
        return banner.decode().strip()
    except:
        return None

def scan_port(ip, port):
    """
    Checks if a port is open. 
    This function is designed to be run by a thread.
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5) # Faster timeout for multi-threading
        result = s.connect_ex((ip, port))
        s.close()
        
        if result == 0:
            # If open, try to identify the service
            banner = grab_banner(ip, port)
            if banner:
                print(f"[+] Port {port} is OPEN --> {banner}")
            else:
                print(f"[+] Port {port} is OPEN")
    except:
        pass

def main():
    parser = argparse.ArgumentParser(description="Net-Audit: Multi-threaded TCP Scanner")
    parser.add_argument("target", help="Target IP address or Domain")
    parser.add_argument("--ports", type=int, default=100, help="Number of ports to scan (default: 100)")
    parser.add_argument("--threads", type=int, default=50, help="Number of concurrent threads (default: 50)")
    
    args = parser.parse_args()
    target_ip = socket.gethostbyname(args.target)
    
    print(f"[*] Starting fast scan on target: {target_ip}")
    print(f"[*] Scanning first {args.ports} ports with {args.threads} threads...")
    print("-" * 50)
    
    start_time = datetime.now()
    
    # The ThreadPoolExecutor is our "Manager" that handles the workers
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
        # We launch a scan_port command for every port from 1 to args.ports
        # The executor manages assigning these tasks to the available threads
        for port in range(1, args.ports + 1):
            executor.submit(scan_port, target_ip, port)
            
    end_time = datetime.now()
    print("-" * 50)
    print(f"[*] Scan completed in {end_time - start_time}")

if __name__ == "__main__":
    main()
