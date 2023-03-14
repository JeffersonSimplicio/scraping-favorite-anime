import requests


def readFile(path: str) -> str:
    data = open(path, 'r')
    code = data.read()
    data.close()
    return code


def readWeb(url: str) -> str:
    page = requests.get(url)
    html_content = page.text
    return html_content
