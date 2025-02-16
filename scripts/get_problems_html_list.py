import cloudscraper
from bs4 import BeautifulSoup
import csv

COOKIE = ""
# Define custom headers from your cURL command
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
    "DNT": "1",
    "Sec-GPC": "1",
    "Connection": "keep-alive",
    # You can update the Cookie if needed, but cloudscraper often handles this automatically.
    "Cookie": (COOKIE),
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Priority": "u=0, i",
}


def fetch_page(page: int) -> str:
    """
    Fetches the HTML content of a given page number using cloudscraper.
    Returns the HTML as a string if successful, else None.
    """
    url = f"https://judge.beecrowd.com/en/problems/index/5?page={page}"
    print(f"Fetching page {page}: {url}")
    scraper = cloudscraper.create_scraper()
    response = scraper.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch page {page}: Status code {response.status_code}")
        return ""


def parse_problems_from_html(html: str) -> list:
    """
    Parses the HTML to extract problem data.
    Returns a list of tuples containing:
    (id_number, question_string, solved_int, level_int, question_link)
    """
    soup = BeautifulSoup(html, "html.parser")

    # Locate the main content container
    main_content = soup.find("div", class_="main-content")
    if not main_content:
        print("Main content not found!")
        return []

    # Find the table that contains the problem list
    table = main_content.find("table")
    if not table:
        print("Table not found!")
        return []

    tbody = table.find("tbody")
    if not tbody:
        print("Table body not found!")
        return []

    problems = []
    rows = tbody.find_all("tr")

    for row in rows:
        cells = row.find_all("td")
        # Verify the row has enough cells to parse the data
        if len(cells) < 7:
            continue

        # Extract problem id and the question link from the first cell
        id_cell = cells[0]
        link_tag = id_cell.find("a")
        if not link_tag:
            continue
        id_number = link_tag.text.strip()
        question_link = link_tag.get("href").strip()
        if question_link.startswith("/"):
            question_link = "https://judge.beecrowd.com" + question_link

        # Extract question string from the third cell
        question_string = cells[2].text.strip()

        # Extract solved count from the sixth cell and remove commas
        solved_text = cells[5].text.strip().replace(",", "")
        try:
            solved_int = int(solved_text)
        except ValueError:
            solved_int = None

        # Extract level from the seventh cell
        level_text = cells[6].text.strip()
        try:
            level_int = int(level_text)
        except ValueError:
            level_int = None

        problems.append(
            (id_number, question_string, solved_int, level_int, question_link)
        )

    return problems


def write_csv(filename: str, header: list, data: list):
    """
    Writes the collected data into a CSV file.
    """
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(data)
    print(f"Data successfully written to {filename}")


def main():
    csv_filename = "beecrowd_problems.csv"
    csv_header = [
        "id_number",
        "question_string",
        "solved_int",
        "level_int",
        "question_link",
    ]
    all_problems = []

    # Loop through pages 1 to 11
    for page in range(1, 12):
        html = fetch_page(page)
        if html != "":
            problems = parse_problems_from_html(html)
            all_problems.extend(problems)
        else:
            print(f"Failed to fetch page {page}")
    # Write all the scraped data to a CSV file
    write_csv(csv_filename, csv_header, all_problems)


if __name__ == "__main__":
    main()
