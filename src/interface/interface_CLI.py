from bs4 import BeautifulSoup
from strategy.main import FavoritesAnimes
from interface.selectors import Selectors
from interface.controls import Controls
from interface.console import Console


def interface():
    Console.clear()
    code = Selectors.file()
    soup = BeautifulSoup(code, "html.parser")

    filter = Selectors.filter(soup)
    filterAnime = FavoritesAnimes(filter, soup)

    total_favorites = filterAnime.len_favorites()

    Console.total_favorites(total_favorites)

    selected = Selectors.options()

    response = Controls.empty_file(total_favorites)

    if response:
        Controls.operation(filterAnime, selected)
    Console.clear(1)
