import concurrent.futures
import urllib.request

URLS = [
    'https://www.python.org',
    'https://www.google.com',
    'https://www.github.com'
]

def check_website(url: str) -> str:
    try:
        with urllib.request.urlopen(url, timeout=5) as conn:
            return f"{url}: Status Code {conn.getcode()}"
    except Exception as e:
        return f"{url}: Failed ({e})"

# ThreadPoolExecutor to run checks in parallel
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(check_website, URLS)
    for result in results:
        print(result)