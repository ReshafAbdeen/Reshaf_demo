import csv
import requests
from bs4 import BeautifulSoup

def scrape_quotes(url):
    """
    Scrapes quotes, authors, and tags from a website and returns them as a list of dictionaries.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve data: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    scraped_data = []
    quote_elements = soup.find_all("div", class_="quote")

    for element in quote_elements:
        text = element.find("span", class_="text").text.strip()
        author = element.find("small", class_="author").text.strip()
        
        tag_elements = element.find("div", class_="tags").find_all("a", class_="tag")
        tags = [tag.text.strip() for tag in tag_elements]
        tags_str = ", ".join(tags) 

        scraped_data.append({
            "Quote": text,
            "Author": author,
            "Tags": tags_str
        })

    return scraped_data

def save_to_csv(data, filename="scraped_quotes.csv"):
    """
    Saves a list of dictionaries into a CSV file.
    """
    if not data:
        print("No data to save.")
        return

    headers = data[0].keys()

    try:
        with open(filename, mode="w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            
            writer.writeheader()
            writer.writerows(data)
            
        print(f"Successfully saved {len(data)} items to '{filename}'!")
    except IOError as e:
        print(f"File Error: Could not save data to file. {e}")

if __name__ == "__main__":
    TARGET_URL = "https://quotes.toscrape.com/"
    print(f"Starting scraper for: {TARGET_URL}...")
    
    results = scrape_quotes(TARGET_URL)
    
    save_to_csv(results)