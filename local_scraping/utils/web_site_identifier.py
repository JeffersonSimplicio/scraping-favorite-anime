from bs4 import BeautifulSoup
from local_scraping.strategy.list_stratege import Strategys


def web_site_identifier(soup: BeautifulSoup):
    for stratege in Strategys:
        if (stratege.value.identifier(soup)):
            return stratege.value
    raise ValueError(
        'The file does not belong to any of the supported formats'
    )
