from os import remove, listdir
from shutil import rmtree
from bs4 import BeautifulSoup
from src.utils.readers import Read
from src.strategy.main import FavoritesAnimes
from src.strategy.ba_strategy import BetterAnimeStrategy
from expectation_results import (
    list_txt_anime_names,
    list_txt_anime_names_url,
    list_json_anime_names_url,
    list_json_anime_names_path,
    list_names_images
)


code = Read.file("tests\\betteranime\\fakes\\fake_full_ba_page.html")
soup = BeautifulSoup(code, "html.parser")
better_anime = FavoritesAnimes(BetterAnimeStrategy, soup)


def read_delete_file(path: str) -> str:
    code = Read.file(path)
    remove(path)
    return code


def test_creation_txt_file_with_list_names():
    expectation_name_file = "name_favorites_betteranime.txt"

    better_anime.create_txt_list_favorites()

    content = read_delete_file(expectation_name_file)

    assert content == list_txt_anime_names


def test_creation_txt_file_with_list_names_thumbs():
    expectation_name_file = "name_url_favorites_betteranime.txt"

    better_anime.create_txt_list_favorites_url()

    content = read_delete_file(expectation_name_file)

    assert content == list_txt_anime_names_url


def test_creation_json_file_with_list_names_thumbs():
    expectation_name_file = "name_url_favorites_betteranime.json"

    better_anime.create_json_list_favorites_url()

    content = read_delete_file(expectation_name_file)

    assert content == list_json_anime_names_url


def test_creation_list_names_download_thumbs():
    better_anime.create_json_list_favorites_local()

    result = listdir("thunbs")
    rmtree("thunbs")

    assert result == list_names_images


def test_creation_json_file_with_list_names_path_thumbs():
    expectation_name_file = "name_local_favorites_betteranime.json"

    content = read_delete_file(expectation_name_file)

    assert content == list_json_anime_names_path
