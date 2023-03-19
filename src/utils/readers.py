import requests


class Read:
    @staticmethod
    def file(path: str) -> str:
        with open(path, "r", encoding="utf-8") as data:
            code = data.read()
        return code

    @staticmethod
    def web(url: str) -> str:
        page = requests.get(url)
        html_content = page.text
        return html_content
