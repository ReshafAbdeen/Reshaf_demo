from concurrent.futures import ThreadPoolExecutor
import urllib.request


def check_website(url):
    """Sends a request to a URL and returns its operational status."""
    formatted_url = (
        url if url.startswith(("http://", "https://")) else f"https://{url}"
    )

    try:
        with urllib.request.urlopen(formatted_url, timeout=5) as response:
            status = response.getcode()
            if status == 200:
                return f"{url} is UP (Status 200)"
    except Exception as e:
        return f"{url} is DOWN or Unreachable (Error: {type(e).__name__})"


def main():
    websites = [
        "google.com",
        "github.com",
        "python.org",
        "thisisafakewebsite12345.com",
        "http://httpbin.org/status/404",
    ]

    print(f"⚡ Starting concurrent check on {len(websites)} websites...\n")

    with ThreadPoolExecutor(max_workers=5) as executor:
        results = executor.map(check_website, websites)

    for result in results:
        print(result)


if __name__ == "__main__":
    main()