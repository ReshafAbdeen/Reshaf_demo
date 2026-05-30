#Multi-Threaded Web Scraper & Data Cleaner

from concurrent.futures import ThreadPoolExecutor
import json
import requests

class DataScraper:
    def __init__(self, urls):
        self.urls = urls
        self.raw_data = []
        self.cleaned_data = []

    def fetch_url(self, url):
        """Fetches data from a single URL with error handling."""
        try:
            response = requests.get(url, timeout=5)
            
            response.raise_for_status() 
            
            print(f"[SUCCESS] Fetched data from: {url}")
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"[ERROR] Failed to fetch {url}: {e}")
            return None

    def scrape_all_concurrently(self):
        """Uses a thread pool to download from multiple URLs at the same time."""
        print(f"Starting download of {len(self.urls)} sources concurrently...")
        
        with ThreadPoolExecutor(max_workers=3) as executor:
            results = executor.map(self.fetch_url, self.urls)
            
            self.raw_data = [res for res in results if res is not None]

    def clean_data(self):
        """Cleans and structures the raw text data."""
        print("\nCleaning and processing data...")
        for raw_item in self.raw_data:
            try:
                data = json.loads(raw_item)
                
                cleaned_todos = [
                    {
                        "id": item.get("id"),
                        "title": item.get("title", "").strip().capitalize(),
                        "completed": item.get("completed", False)
                    }
                    for item in data if "title" in item
                ]
                self.cleaned_data.extend(cleaned_todos)
            except json.JSONDecodeError:
                print("[WARN] Found data that wasn't valid JSON. Skipping.")

    def display_results(self, limit=5):
        """Displays a summary of the processed data."""
        print(f"\n=== SCRAPER REPORT ===")
        print(f"Total cleaned items: {len(self.cleaned_data)}")
        print(f"Showing first {limit} items:")
        
        for item in self.cleaned_data[:limit]:
            status = "✅" if item['completed'] else "❌"
            print(f" [{status}] (ID: {item['id']}) {item['title']}")


if __name__ == "__main__":
    target_urls = [
        "https://jsonplaceholder.typicode.com/todos?_limit=3",
        "https://jsonplaceholder.typicode.com/todos?_limit=4",
        "https://invalid-url-that-will-fail.com", 
        "https://jsonplaceholder.typicode.com/todos?_limit=2"
    ]

    scraper = DataScraper(target_urls)
    
    scraper.scrape_all_concurrently()
    
    scraper.clean_data()
    
    scraper.display_results()