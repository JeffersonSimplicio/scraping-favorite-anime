from bs4 import BeautifulSoup
from strategy.main import FavoritesAnimes
from interface.selectors import Selectors
from interface.controls import Controls


def interface():
    code = Selectors.file()
    soup = BeautifulSoup(code, "html.parser")

    filter = Selectors.filter(soup)
    filterAnime = FavoritesAnimes(filter, soup)

    total_favorites = filterAnime.len_favorites()

    if (total_favorites == 0):
        print('Você não possui nenhum anime na lista de favoritos')
    elif (total_favorites == 1):
        print('Você possui 1 anime na lista de favoritos')
    else:
        print(f'Você possui {filterAnime.len_favorites()} animes favoritos')

    selected = Selectors.options()

    response = Controls.empty_file(total_favorites)

    if response:
        Controls.operation(filterAnime, selected)
