from bs4 import BeautifulSoup
from src.utils.readers import Read
from src.strategy.main import FavoritesAnimes
from src.strategy.af_strategy import AnimeFireStrategy
from expectation_results_animefire import (
    amount_anime,
    list_txt_anime_names,
    array_animes_names_thumbs
)


code = Read.file("tests\\animeFire\\fakes\\fake_full_animefire_page.html")
soup = BeautifulSoup(code, "html.parser")
animefire = FavoritesAnimes(AnimeFireStrategy, soup)


def test_returns_to_total_number_of_favorites():
    total = animefire.len_favorites()

    assert total == amount_anime


def test_name_all_unreturned_animes():
    list = animefire.list_favorites_name()

    assert list == list_txt_anime_names.split()


def test_returns_list_name_url():
    list = animefire.list_name_thumb()

    assert list == array_animes_names_thumbs
