from enum import Enum
from local_scraping.strategy.anihub_strategy import AnihubStrategy
from local_scraping.strategy.ba_strategy import BetterAnimeStrategy


class Strategys(Enum):
    BetterAnime = BetterAnimeStrategy
    Anihub = AnihubStrategy
