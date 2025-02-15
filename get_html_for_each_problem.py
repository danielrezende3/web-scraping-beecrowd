import csv
from docling.document_converter import DocumentConverter

import cloudscraper
import docling
import pandas as pd
from bs4 import BeautifulSoup

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
    "DNT": "1",
    "Sec-GPC": "1",
    "Connection": "keep-alive",
    "Cookie": (
        "cf_clearance=OZs8v49MXSuB3L9CvUoVMuA4L40X41Djp9kJvC2BDN8-1733926360-1.2.1.1-dxoXqeY6oOqEHv4iZa0om1Z5hXKJ.1tZl6pm_CgSP_IGLE2xR7Gyj4ScH3upeY6Nz6J1NB7U_AAzdXYI1ida.AUrPmm0ueqdo.MM_4TAvgSQelXVS00.VfqXXpzIUi3a1j5MDLjuw26GXe.ZLGhGx9iIz3bjY8xY924jqpCoMQeomMInMTZWJ_5Xnz.uTBlVwgFxfT4360wbslFmQHgKwtbrtY.eMGx8rF6Femc.mwpQFfC9e65Mp3MxrehSPds8Wu58Rkv50ASAqVIjPaPuuU5rKsvFKrcOeGJS9z8kp8L0sCb_2ZbzI422wc2Apds66wkekmK4dLhyzD5AvgP6vOJRQyXZOH5.zlOmdpR1iVgqC.Xpl0v9XvOo4anXIfmHm00e6L2B19lIVwsoXoiD4w; popup=view; cookieBubble=true; judge=eklfipkrceppiqmku98vk5jcol; csrfToken=79wDuZpMm9r%2FHmuvs5XO3jgwM2YyMjZiM2Y5MDRjZTU3MjIzMTYwNzM2NDI2MDkwYmE3OGIxZjc%3D"
    ),
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Priority": "u=0, i",
}


def fetch_problem_markdown(link: str) -> str:
    """
    Given a question link, fetches the problem detail page, extracts the problem content,
    and converts its HTML to Markdown using docling.
    """
    print(f"Fetching problem detail: {link}")
    scraper = cloudscraper.create_scraper()
    response = scraper.get(link, headers=HEADERS)
    if response.status_code != 200:
        print(
            f"Failed to fetch problem detail at {link}: Status code {response.status_code}"
        )
        return ""

    soup = BeautifulSoup(response.text, "html.parser")

    # First, try to find the div with class "problem"
    problem_div = soup.find("div", class_="problem")
    if problem_div:
        return str(problem_div)
    else:
        print("Problem content not found in main page; checking for iframe...")
        # Look for an iframe that might contain the problem description
        iframe = soup.find("iframe", id="description-html")
        if iframe and iframe.has_attr("src"):
            iframe_src = iframe["src"]
            print(f"Fetching iframe content from: {iframe_src}")
            iframe_response = scraper.get(iframe_src, headers=HEADERS)
            if iframe_response.status_code == 200:
                iframe_soup = BeautifulSoup(iframe_response.text, "html.parser")
                return str(iframe_soup.find("div", class_="problem"))
            else:
                print(
                    f"Failed to fetch iframe content: Status {iframe_response.status_code}"
                )
                return ""
        else:
            print("No suitable iframe found in the page.")
            return ""


def main():
    csv_filename = "beecrowd_problems.csv"
    df = pd.read_csv(csv_filename)
    link_question_series = df["question_link"]
    id_number_series = df["id_number"]

    for link, id in zip(link_question_series, id_number_series):
        print(f"Fetching problem {id} at {link}")
        text = fetch_problem_markdown(link)
        with open(f"data/{id}.html", "w", encoding="utf-8") as f:
            f.write(text)


if __name__ == "__main__":
    main()
