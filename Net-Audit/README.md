# Net-Audit
### Low-Level Network Reconnaissance Tool

**Status:** Active Development / Educational  
**Language:** Python 3

---

### 🎯 Project Purpose
**Net-Audit** is a Python-based network scanner developed to understand the fundamentals of **Network Reconnaissance** at the socket level.

While industry-standard tools like Nmap are powerful, they often abstract away the underlying mechanics of the TCP/IP stack. This project was built to demonstrate a "hands-on" understanding of:
*   **Socket Programming:** Creating and managing raw network connections.
*   **The TCP Handshake:** How connections are established (SYN, SYN-ACK, ACK).
*   **Port States:** distinguishing between Open, Closed, and Filtered ports programmatically.

### 🛠 How it Works
The tool bypasses high-level abstractions and interacts directly with the OS network stack via the Python `socket` library.

1.  **Socket Creation:** Initializes an IPv4/TCP socket (`AF_INET`, `SOCK_STREAM`).
2.  **Connection Attempt:** Sends a SYN packet to the target port using `connect_ex()`.
3.  **Analysis:** 
    *   If the return code is `0`, the target completed the handshake -> **Port is OPEN**.
    *   If the connection times out or returns an error, the port is considered Closed or Filtered.

### 🚀 Roadmap
*   **v1.0:** Basic Port Detection.
*   **Feature:** Core socket connectivity logic (`socket.connect_ex`).
*   **Function:** Identifies Open vs Closed ports based on TCP response codes.  
<img width="321" height="49" alt="net-audit v1.0" src="https://github.com/user-attachments/assets/e1f2a64a-b888-4f0a-9f9d-00c340bf2b97" />

*   **v1.1:** Banner Grabbing (Service Version Detection).
*   **Feature:** Added service fingerprinting capability.
*   **Technical Detail:** Upon establishing a TCP connection (3-way handshake), the script now attempts to `recv()` data bytes immediately.
*   **Result:** Successfully retrieves banners from "chatty" protocols like SSH, FTP, and SMTP to identify software versions (e.g., `OpenSSH 6.6.1p1`).
*   **CLI Update:** Migrated from hardcoded variables to `argparse`. Usage: `python3 scanner.py <target_domain_or_ip>`.
<img width="537" height="76" alt="net-audit v1.1" src="https://github.com/user-attachments/assets/1b10adb5-6f42-4133-be75-80c8d8a09411" />

*   **v1.2:** Multi-threading for performance optimization.
*   **Feature:** Implemented concurrent scanning using `ThreadPoolExecutor`.
*   **Impact:** Drastically reduced scan time. The tool can now scan 1,000 ports in under 10 seconds (previously ~15 minutes sequentially).
*   **Logic:** Replaced the sequential `for` loop with a thread pool management system that assigns port checks to 50+ concurrent worker threads.
*   **CLI Update:** Added arguments `--ports` (range limit) and `--threads` (concurrency level).
<img width="706" height="113" alt="net-audit v1.2" src="https://github.com/user-attachments/assets/415ea74e-bd2e-48ec-b6c7-8d5dae7722dc" />

---

### ⚠️ Disclaimer
*This tool is developed for educational purposes and authorized security testing only. Scanning networks without permission is illegal.*
