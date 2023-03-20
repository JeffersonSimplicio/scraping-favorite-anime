from os import remove, listdir
from shutil import rmtree
from bs4 import BeautifulSoup
from src.utils.readers import Read
from src.strategy.main import FavoritesAnimes
from src.strategy.ba_strategy import BetterAnimeStrategy


code = Read.file("tests\\betteranime\\fakes\\fake_full_ba_page.html")
soup = BeautifulSoup(code, "html.parser")
better_anime = FavoritesAnimes(BetterAnimeStrategy, soup)


def read_delete_file(path: str) -> str:
    code = Read.file(path)
    remove(path)
    return code


def test_creation_txt_file_with_list_names():
    expectation_result = """Anime1
Anime2
Anime3
Anime4
Anime5
"""
    expectation_name_file = "name_favorites_betteranime.txt"

    better_anime.create_txt_list_favorites()

    content = read_delete_file(expectation_name_file)

    assert content == expectation_result


def test_creation_txt_file_with_list_names_thumbs():
    expectation = """Anime1 - https://betteranime.com/anime1-img.jpg

Anime2 - https://betteranime.com/anime2-img.jpg

Anime3 - https://betteranime.com/anime3-img.jpg

Anime4 - https://betteranime.com/anime4-img.jpg

Anime5 - https://betteranime.com/anime5-img.jpg

"""
    expectation_name_file = "name_url_favorites_betteranime.txt"

    better_anime.create_txt_list_favorites_url()

    content = read_delete_file(expectation_name_file)

    assert content == expectation


def test_creation_json_file_with_list_names_thumbs():
    expectation = (
        """[{"name": "Anime1", """
        + """"thunb_url": "https://betteranime.com/anime1-img.jpg"}, """
        + """{"name": "Anime2", """
        + """"thunb_url": "https://betteranime.com/anime2-img.jpg"}, """
        + """{"name": "Anime3", """
        + """"thunb_url": "https://betteranime.com/anime3-img.jpg"}, """
        + """{"name": "Anime4", """
        + """"thunb_url": "https://betteranime.com/anime4-img.jpg"}, """
        + """{"name": "Anime5", """
        + """"thunb_url": "https://betteranime.com/anime5-img.jpg"}]"""
    )
    expectation_name_file = "name_url_favorites_betteranime.json"

    better_anime.create_json_list_favorites_url()

    content = read_delete_file(expectation_name_file)

    assert content == expectation


def test_creation_list_names_download_thumbs():
    expectation_thumbs = [
        "anime1.jpg",
        "anime2.jpg",
        "anime3.jpg",
        "anime4.jpg",
        "anime5.jpg",
    ]

    better_anime.create_json_list_favorites_local()

    result = listdir("thunbs")
    rmtree("thunbs")

    assert result == expectation_thumbs


def test_creation_json_file_with_list_names_path_thumbs():
    expectation = (
        """[{"name": "Anime1", """
        + """"thunb_url": "/thunbs/anime1.jpg"}, """
        + """{"name": "Anime2", """
        + """"thunb_url": "/thunbs/anime2.jpg"}, """
        + """{"name": "Anime3", """
        + """"thunb_url": "/thunbs/anime3.jpg"}, """
        + """{"name": "Anime4", """
        + """"thunb_url": "/thunbs/anime4.jpg"}, """
        + """{"name": "Anime5", """
        + """"thunb_url": "/thunbs/anime5.jpg"}]"""
    )
    expectation_name_file = "name_local_favorites_betteranime.json"

    content = read_delete_file(expectation_name_file)

    assert content == expectation
