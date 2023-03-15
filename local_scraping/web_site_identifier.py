from bs4 import BeautifulSoup
from local_scraping.strategy.list_stratege import Strategys


def web_site_identifier(soup: BeautifulSoup):
    for stratege in Strategys:
        if (stratege.value.identifier(soup)):
            return stratege.value
    raise ValueError(
        'The file does not belong to any of the supported formats'
    )


if __name__ == '__main__':
    from utils.readers import readFile

    code = readFile('pages/anihub/anihub_page.html')
    soup = BeautifulSoup(code, "html.parser")

    x = web_site_identifier(soup)
    print(type(x))
