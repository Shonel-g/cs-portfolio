import socket
import argparse

def grab_banner(ip, port):
    """
    Attempts to retrieve the service banner from an open port.
    """
    try:
        # We create a new socket specifically for banner grabbing
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2) # Give a bit more time for the server to speak
        s.connect((ip, port))
        
        # Some protocols (like HTTP) wait for the client to speak first.
        # Others (like SSH, FTP, SMTP) speak immediately upon connection.
        # We try to receive data. 
        
        # Note: For HTTP ports, we might need to send a trigger byte, 
        # but for this basic version, we listen for "chatty" services.
        banner = s.recv(1024) # Read up to 1024 bytes
        s.close()
        
        return banner.decode().strip() # Convert bytes to string and remove spaces
    except:
        return None

def scan_port(ip, port):
    """
    Checks if a port is open and attempts to grab the banner.
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((ip, port))
        s.close()
        
        if result == 0:
            print(f"[+] Port {port} is OPEN", end=' ')
            
            # If open, try to identify the service
            banner = grab_banner(ip, port)
            if banner:
                print(f"--> Service: {banner}")
            else:
                print(f"--> Service: Unknown (No banner received)")
        else:
            pass # Port closed
            
    except Exception as e:
        print(f"[!] Error scanning port {port}: {e}")

def main():
    # CLI Argument Parsing
    parser = argparse.ArgumentParser(description="Net-Audit: TCP Port Scanner & Banner Grabber")
    parser.add_argument("target", help="Target IP address or Domain (e.g., scanme.nmap.org)")
    args = parser.parse_args()
    
    # Convert domain to IP if necessary
    target_ip = socket.gethostbyname(args.target)
    
    print(f"[*] Starting scan on target: {target_ip}")
    print("[*] Scanning top common ports...")
    
    # List of interesting ports to scan
    # 21: FTP, 22: SSH, 25: SMTP, 80: HTTP, 443: HTTPS
    ports = [21, 22, 25, 80, 443, 3306] 
    
    for port in ports:
        scan_port(target_ip, port)

if __name__ == "__main__":
    main()
