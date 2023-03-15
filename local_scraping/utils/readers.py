import requests


def read_file(path: str) -> str:
    data = open(path, 'r')
    code = data.read()
    data.close()
    return code


def read_web(url: str) -> str:
    page = requests.get(url)
    html_content = page.text
    return html_content
