import re
from collections import Counter

log_data = """
192.168.1.10 - - [08/Jun/2026:10:00:01] "GET /home HTTP/1.1" 200 2326
192.168.1.12 - - [08/Jun/2026:10:00:05] "POST /login HTTP/1.1" 401 512
192.168.1.10 - - [08/Jun/2026:10:01:15] "GET /about HTTP/1.1" 200 1243
192.168.1.15 - - [08/Jun/2026:10:02:45] "GET /index HTTP/1.1" 404 312
192.168.1.12 - - [08/Jun/2026:10:03:12] "GET /home HTTP/1.1" 200 2326
192.168.1.20 - - [08/Jun/2026:10:04:01] "POST /submit HTTP/1.1" 500 843
192.168.1.10 - - [08/Jun/2026:10:05:00] "GET /home HTTP/1.1" 200 2326
"""

def analyze_logs(logs):
    log_pattern = r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?"\s*(?P<status>\d{3})'
    
    ips = []
    status_codes = []
    
    for line in logs.strip().split('\n'):
        match = re.search(log_pattern, line)
        if match:
            ips.append(match.group('ip'))
            status_codes.append(match.group('status'))
            
    ip_counts = Counter(ips)
    status_counts = Counter(status_codes)
    
    return ip_counts, status_counts

def display_report(ip_counts, status_counts):
    print("=== LOG ANALYSIS REPORT ===")
    
    print("\n[+] Requests per IP Address:")
    for ip, count in sorted(ip_counts.items(), key=lambda item: item[1], reverse=True):
        print(f"  {ip:<15} : {count} requests")
        
    print("\n[+] HTTP Status Code Breakdown:")
    for status, count in status_counts.items():
        status_meanings = {"200": "OK", "401": "Unauthorized", "404": "Not Found", "500": "Server Error"}
        meaning = status_meanings.get(status, "Unknown")
        print(f"  {status} ({meaning}) : {count} times")

if __name__ == "__main__":
    ip_data, status_data = analyze_logs(log_data)
    display_report(ip_data, status_data)