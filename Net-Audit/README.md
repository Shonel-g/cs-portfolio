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
*   **v1.0:** Basic Port Detection (Current).
<img width="321" height="49" alt="net-audit v1.0" src="https://github.com/user-attachments/assets/e1f2a64a-b888-4f0a-9f9d-00c340bf2b97" />

*   **v1.1:** Banner Grabbing (Service Version Detection).
*   **v1.2:** Multi-threading for performance optimization.

---

### ⚠️ Disclaimer
*This tool is developed for educational purposes and authorized security testing only. Scanning networks without permission is illegal.*
