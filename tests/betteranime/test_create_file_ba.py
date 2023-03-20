from os import remove
from bs4 import BeautifulSoup
from src.utils.readers import Read
from src.strategy.main import FavoritesAnimes
from src.strategy.ba_strategy import BetterAnimeStrategy


code = Read.file("tests\\betteranime\\fakes\\fake_full_ba_page.html")
soup = BeautifulSoup(code, "html.parser")
better_anime = FavoritesAnimes(BetterAnimeStrategy, soup)


def test_create_file_names_favorites():
    expectation = """Anime1
Anime2
Anime3
Anime4
Anime5
"""

    better_anime.create_txt_list_favorites()

    file = open("name_favorites_betteranime.txt", mode="r")
    content = file.read()
    file.close()
    remove("name_favorites_betteranime.txt")

    assert content == expectation
