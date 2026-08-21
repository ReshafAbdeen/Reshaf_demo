import requests

def fetch_user_posts(user_id: int):
    url = f"https://jsonplaceholder.typicode.com/posts?userId={user_id}"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Check for HTTP errors (4xx, 5xx)
        posts = response.json()
        
        print(f"Fetched {len(posts)} posts for User ID {user_id}:\n")
        for post in posts[:3]:  # Top 3 posts
            print(f"Title: {post['title']}")
            print(f"Body: {post['body'][:50]}...\n")

    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}")

# Usage
fetch_user_posts(user_id=1)