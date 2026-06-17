import sys
import requests
from bs4 import BeautifulSoup


def fetch_html(url: str) -> str:
    """Fetches the raw HTML content from a URL with basic error handling."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        sys.exit(1)


def parse_jobs(html_content: str, keyword: str) -> list[dict]:
    """Parses HTML and extracts job listings that match a specific keyword."""
    soup = BeautifulSoup(html_content, "html.parser")
    job_cards = soup.find_all("div", class_="card-content")

    matching_jobs = []

    for card in job_cards:
        title_element = card.find("h2", class_="title")
        company_element = card.find("h3", class_="company")
        location_element = card.find("p", class_="location")

        if title_element and company_element:
            title = title_element.text.strip()
            company = company_element.text.strip()
            location = (
                location_element.text.strip() if location_element else "Remote"
            )

            if keyword.lower() in title.lower():
                job_data = {
                    "title": title,
                    "company": company,
                    "location": location,
                }
                matching_jobs.append(job_data)

    return matching_jobs


def save_to_markdown(jobs: list[dict], filename: str = "jobs_report.md"):
    """Saves the scraped data into a cleanly formatted markdown file."""
    if not jobs:
        print("No jobs found matching the criteria. File not saved.")
        return

    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(f"# Job Search Results\n")
        file.write(f"Total positions found: {len(jobs)}\n\n")
        file.write("| Job Title | Company | Location |\n")
        file.write("| --- | --- | --- |\n")

        for job in jobs:
            file.write(
                f"| {job['title']} | {job['company']} | {job['location']} |\n"
            )

    print(f"Successfully saved {len(jobs)} jobs to '{filename}'!")


if __name__ == "__main__":
    SCRAPE_URL = "https://realpython.github.io/fake-jobs/"
    SEARCH_KEYWORD = "Python"

    print(f"Starting scraper for: {SCRAPE_URL}...")

    raw_html = fetch_html(SCRAPE_URL)

    filtered_jobs = parse_jobs(raw_html, SEARCH_KEYWORD)

    save_to_markdown(filtered_jobs)