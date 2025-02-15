from pathlib import Path
from markdownify import markdownify as md


def main():
    folder_path = Path("data/")
    html_files = folder_path.glob("*.html")
    for file in html_files:
        with open(file, "r", encoding="utf-8") as f:
            html_content = f.read()
        markdown_content = md(html_content)
        md_final = f"# Problem {file.stem}\n\nDescrição\n----------{markdown_content}"
        with open(file.with_suffix(".md"), "w", encoding="utf-8") as f:
            f.write(md_final)


if __name__ == "__main__":
    main()
