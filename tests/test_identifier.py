from bs4 import BeautifulSoup
from src.utils.readers import Read
from src.strategy.ba_strategy import BetterAnimeStrategy
from src.strategy.anihub_strategy import AnihubStrategy
from src.strategy.af_strategy import AnimeFireStrategy


code_ba = Read.file("tests\\betteranime\\fakes\\fake_full_ba_page.html")
code_anihub = Read.file("tests\\anihub\\fakes\\fake_full_anihub_page.html")
code_af = Read.file(
    "tests\\animeFire\\fakes\\fake_full_animefire_page.html"
)

soup_ba = BeautifulSoup(code_ba, "html.parser")
soup_anihub = BeautifulSoup(code_anihub, "html.parser")
soup_af = BeautifulSoup(code_af, "html.parser")


def test_returns_true_when_supported():
    result_ba = BetterAnimeStrategy.identifier(soup_ba)
    result_anihub = AnihubStrategy.identifier(soup_anihub)
    result_af = AnimeFireStrategy.identifier(soup_af)

    assert result_ba is True
    assert result_anihub is True
    assert result_af is True


def test_returns_true_when_not_supported():
    result_ba_one = BetterAnimeStrategy.identifier(soup_anihub)
    result_ba_two = BetterAnimeStrategy.identifier(soup_af)

    result_anihub_one = AnihubStrategy.identifier(soup_af)
    result_anihub_two = AnihubStrategy.identifier(soup_ba)

    result_af_one = AnimeFireStrategy.identifier(soup_ba)
    result_af_two = AnimeFireStrategy.identifier(soup_anihub)

    assert result_ba_one is False
    assert result_ba_two is False
    assert result_anihub_one is False
    assert result_anihub_two is False
    assert result_af_one is False
    assert result_af_two is False