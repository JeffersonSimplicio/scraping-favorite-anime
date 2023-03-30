from bs4 import BeautifulSoup
from src.strategy.main import FavoritesAnimes
from src.interface.selectors import Selectors
from src.interface.controls import Controls
from src.interface.console import Console


def interface():
    Console.clear()
    code = Selectors.file()
    soup = BeautifulSoup(code, "html.parser")

    filter = Selectors.filter(soup)
    filterAnime = FavoritesAnimes(filter, soup)

    total_favorites = filterAnime.len_favorites()

    while True:
        Console.total_favorites(total_favorites)

        selected = Selectors.options()

        response = Controls.empty_file(total_favorites)

        if response:
            Controls.operation(filterAnime, selected)
        Console.clear(1)

        continua = Selectors.willContinue()

        if not continua:
            break
