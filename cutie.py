# API Data Fetcher & Data Extraction

import urllib.request
import json
from urllib.error import URLError, HTTPError

def fetch_user_data(limit):
    """Fetches user data from a public API and filters it."""
    url = f"https://jsonplaceholder.typicode.com/users"
    
    try:
        print(f"Fetching data from API...")
        with urllib.request.urlopen(url) as response:
            if response.status == 200:
                data = json.loads(response.read().decode('utf-8'))
                
                extracted_users = [
                    {"name": user["name"], "company": user["company"]["name"]}
                    for user in data if len(user["name"]) > 12
                ]
                
                return extracted_users[:limit]
    except HTTPError as e:
        print(f"HTTP Error: {e.code}")
    except URLError as e:
        print(f"URL Error: {e.reason}")
    return []

if __name__ == "__main__":
    users = fetch_user_data(3)
    print("Filtered Users:")
    for user in users:
        print(f"- {user['name']} (Works at: {user['company']})")