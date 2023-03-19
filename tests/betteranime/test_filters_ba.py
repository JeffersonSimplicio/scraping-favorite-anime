from bs4 import BeautifulSoup
from src.utils.readers import Read
from src.strategy.main import FavoritesAnimes
from src.strategy.ba_strategy import BetterAnimeStrategy


code = Read.file("tests\\betteranime\\fakes\\fake_full_ba_page.html") 
soup = BeautifulSoup(code, "html.parser")
better_anime = FavoritesAnimes(BetterAnimeStrategy, soup)


def test_returns_to_total_number_of_favorites():
    total = better_anime.len_favorites()

    assert total == 5


# def test_name_all_unreturned_animes():
#     expectation = ["Anime1", "Anime2", "Anime3", "Anime4", "Anime5"]

#     list = better_anime.list_favorites_name()

#     assert list == expectation


# def test_returns_list_name_url():
#     expectation = [
#         {
#             "name": "Anime1",
#             "thunb_url": "https://betteranime.com/anime1-img.jpg",
#         },
#         {
#             "name": "Anime2",
#             "thunb_url": "https://betteranime.com/anime2-img.jpg",
#         },
#         {
#             "name": "Anime3",
#             "thunb_url": "https://betteranime.com/anime3-img.jpg",
#         },
#         {
#             "name": "Anime4",
#             "thunb_url": "https://betteranime.com/anime4-img.jpg",
#         },
#         {
#             "name": "Anime5",
#             "thunb_url": "https://betteranime.com/anime5-img.jpg",
#         },
#     ]

#     list = better_anime.list_name_thunb()

#     assert list == expectation
