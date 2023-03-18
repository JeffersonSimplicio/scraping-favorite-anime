import requests


def read_file(path: str) -> str:
    with open(path, 'r', encoding="utf-8") as data:
        code = data.read()
    return code


def read_web(url: str) -> str:
    page = requests.get(url)
    html_content = page.text
    return html_content
