from bs4 import BeautifulSoup
from strategy.main import FavoritesAnimes
from strategy.ba_strategy import BetterAnimeStrategy
from interface.interface_controls import (
    select_file,
    select_option,
    operation
)


def interface():
    code = select_file()

    soup = BeautifulSoup(code, "html.parser")
    betterAnime = FavoritesAnimes(BetterAnimeStrategy, soup)

    print(f'Você possui {betterAnime.len_favorites()} animes favoritos')

    selected = select_option()
    operation(betterAnime, selected)


interface()
