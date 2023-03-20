from os import remove
from bs4 import BeautifulSoup
from src.utils.readers import Read
from src.strategy.main import FavoritesAnimes
from src.strategy.ba_strategy import BetterAnimeStrategy


code = Read.file("tests\\betteranime\\fakes\\fake_full_ba_page.html")
soup = BeautifulSoup(code, "html.parser")
better_anime = FavoritesAnimes(BetterAnimeStrategy, soup)


def test_creation_txt_file_with_list_names():
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


def test_creation_txt_file_with_list_names_thumbs():
    expectation = """Anime1 - https://betteranime.com/anime1-img.jpg

Anime2 - https://betteranime.com/anime2-img.jpg

Anime3 - https://betteranime.com/anime3-img.jpg

Anime4 - https://betteranime.com/anime4-img.jpg

Anime5 - https://betteranime.com/anime5-img.jpg

"""

    better_anime.create_txt_list_favorites_url()

    file = open("name_url_favorites_betteranime.txt", mode="r")
    content = file.read()
    file.close()
    remove("name_url_favorites_betteranime.txt")

    assert content == expectation
