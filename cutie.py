import json
import re
from urllib.request import Request, urlopen


class BookScraper:
    """Scrapes book data from books.toscrape.com."""

    def __init__(self):
        self.base_url = "http://books.toscrape.com/"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    def fetch_html(self, url):
        """Fetches raw HTML text from a given URL."""
        try:
            req = Request(url, headers=self.headers)
            with urlopen(req) as response:
                return response.read().decode("utf-8")
        except Exception as e:
            print(f"Error fetching URL: {e}")
            return None

    def scrape_books(self):
        """Parses book titles and prices using Regular Expressions."""
        print("Connecting to website and fetching data...")
        html_content = self.fetch_html(self.base_url)

        if not html_content:
            return []

        title_pattern = r'title="([^"]+)"'
        price_pattern = r"£([0-9]+\.[0-9]{2})"

        print("Parsing HTML content using Regex...")
        titles = re.findall(title_pattern, html_content)
        prices = re.findall(price_pattern, html_content)

        unique_titles = []
        for t in titles:
            if t not in unique_titles:
                unique_titles.append(t)

        books_data = []
        for title, price in zip(unique_titles, prices):
            books_data.append(
                {"title": title, "price_gbp": float(price), "currency": "GBP"}
            )

        return books_data


class DataAnalyzer:
    """Analyzes collected book data and saves it to disk."""

    def __init__(self, data):
        self.data = data

    def calculate_metrics(self):
        """Performs math operations over the collected dataset."""
        if not self.data:
            print("No data available to analyze.")
            return

        prices = [book["price_gbp"] for book in self.data]

        avg_price = sum(prices) / len(prices)
        max_book = max(self.data, key=lambda x: x["price_gbp"])
        min_book = min(self.data, key=lambda x: x["price_gbp"])

        print("\n=== DATA METRICS ===")
        print(f"Total Books Scraped: {len(self.data)}")
        print(f"Average Book Price:  £{avg_price:.2f}")
        print(f"Most Expensive:      '{max_book['title']}' (£{max_book['price_gbp']})")
        print(f"Cheapest:            '{min_book['title']}' (£{min_book['price_gbp']})")

    def save_to_json(self, filename="books_dataset.json"):
        """Saves the structured dictionary list into a JSON file."""
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(self.data, f, indent=4, ensure_ascii=False)
            print(f"\nData successfully exported to '{filename}'")
        except IOError as e:
            print(f"Failed to save file: {e}")


def main():
    print("=== INTERMEDIATE WEB SCRAPER & ANALYZER ===")

    scraper = BookScraper()
    scraped_data = scraper.scrape_books()

    if scraped_data:
        analyzer = DataAnalyzer(scraped_data)
        analyzer.calculate_metrics()
        analyzer.save_to_json()
    else:
        print("Script ended prematurely because no data was recovered.")


if __name__ == "__main__":
    main()
