from bs4 import BeautifulSoup
from strategy.main import FavoritesAnimes
from interface.interface_controls import (
    select_file,
    select_filter,
    select_option,
    operation
)


def interface():
    code = select_file()
    soup = BeautifulSoup(code, "html.parser")

    filter = select_filter(soup)
    filterAnime = FavoritesAnimes(filter, soup)

    total_favorites = filterAnime.len_favorites()

    if (total_favorites == 0):
        print('Você não possui nenhum anime na lista de favoritos')
    elif (total_favorites == 1):
        print('Você possui 1 anime na lista de favoritos')
    else:
        print(f'Você possui {filterAnime.len_favorites()} animes favoritos')

    selected = select_option()
    operation(filterAnime, selected)
