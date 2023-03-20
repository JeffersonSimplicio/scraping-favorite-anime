from bs4 import BeautifulSoup
from src.utils.readers import Read
from src.strategy.main import FavoritesAnimes
from src.strategy.ba_strategy import BetterAnimeStrategy
from expectation_results import (
    amount_anime,
    list_txt_anime_names,
    array_animes_names_thumbs
)


code = Read.file("tests\\betteranime\\fakes\\fake_full_ba_page.html")
soup = BeautifulSoup(code, "html.parser")
better_anime = FavoritesAnimes(BetterAnimeStrategy, soup)


def test_returns_to_total_number_of_favorites():
    total = better_anime.len_favorites()

    assert total == amount_anime


def test_name_all_unreturned_animes():
    list = better_anime.list_favorites_name()

    assert list == list_txt_anime_names.split()


def test_returns_list_name_url():
    list = better_anime.list_name_thunb()

    assert list == array_animes_names_thumbs
