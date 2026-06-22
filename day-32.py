import requests
from bs4 import BeautifulSoup


class QuoteScraper:

    def __init__(self):
        self.url = "https://quotes.toscrape.com/"

    def fetch_quotes(self):
        response = requests.get(self.url)
        if response.status_code != 200:
            return "Failed to retrieve website."

        soup = BeautifulSoup(response.text, "html.parser")
        quote_elements = soup.find_all("div", class_="quote")

        scraped_data = []
        for element in quote_elements:
            text = element.find("span", class_="text").text
            author = element.find("small", class_="author").text
            scraped_data.append({"quote": text, "author": author})

        return scraped_data


if __name__ == "__main__":
    scraper = QuoteScraper()
    results = scraper.fetch_quotes()

    print(f"--- Scraped {len(results)} Quotes ---")
    for item in results[:5]:
        print(f"\"{item['quote']}\" - By: {item['author']}\n")