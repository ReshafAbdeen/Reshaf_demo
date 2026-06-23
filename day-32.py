import concurrent.futures
import logging
import requests

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - [%(levelname)s] - %(message)s"
)

URLS = [
    "https://www.google.com",
    "https://www.github.com",
    "https://httpbin.org/delay/2",  
    "https://thisisadeadsite12345.com",  
    "https://httpbin.org/status/404",  
]


def check_website(url: str, timeout: int = 5) -> dict:
    """Fetches a URL and returns its status or error details."""
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return {"url": url, "status": response.status_code, "error": None}
    except requests.exceptions.HTTPError as http_err:
        return {"url": url, "status": response.status_code, "error": f"HTTP Error: {http_err}"}
    except requests.exceptions.RequestException as req_err:
        return {"url": url, "status": None, "error": f"Connection Error: {req_err}"}


def main():
    logging.info("Starting website status checker...")
    results = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = {executor.submit(check_website, url): url for url in URLS}

        for future in concurrent.futures.as_completed(future_to_url):
            data = future.result()
            results.append(data)
            if data["error"]:
                logging.warning(f"Failure: {data['url']} -> {data['error']}")
            else:
                logging.info(f"Success: {data['url']} -> Status {data['status']}")

    print(f"\n--- Processed {len(results)} sites ---")


if __name__ == "__main__":
    main()