import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor
import time

URLS = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.wikipedia.org",
    "https://www.thisisafakewebsite12345.com",  
    "https://httpbin.org/status/404",          
    "https://httpbin.org/status/500"           
]

def check_url(url):
    """
    Worker function that attempts to connect to a URL 
    and returns its HTTP status status.
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    req = urllib.request.Request(url, headers=headers)
    
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            return url, response.getcode(), "Healthy"
    except urllib.error.HTTPError as e:
        return url, e.code, f"Server Error"
    except urllib.error.URLError as e:
        return url, None, f"Unreachable ({e.reason})"
    except Exception as e:
        return url, None, f"Unexpected Error: {str(e)}"

def run_multithreaded():
    print(f"Starting status check on {len(URLS)} URLs using multithreading...\n")
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=4) as executor:
        results = executor.map(check_url, URLS)
        
        for url, code, status in results:
            code_str = f"[{code}]" if code else "[---]"
            print(f" {code_str:<7} | {status:<15} | {url}")
            
    end_time = time.time()
    print(f"\nFinished in {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    run_multithreaded()