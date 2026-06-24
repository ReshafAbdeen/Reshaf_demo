import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

headlines = [h.text.strip() for h in soup.find_all("h2") if h.text]

print("--- Top BBC News Headlines ---")
for i, headline in enumerate(headlines[:5], 1):
    print(f"{i}. {headline}")