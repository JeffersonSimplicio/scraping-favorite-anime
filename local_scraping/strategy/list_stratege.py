from enum import Enum
from strategy.anihub_strategy import AnihubStrategy
from strategy.ba_strategy import BetterAnimeStrategy


class Strategys(Enum):
    BetterAnime = BetterAnimeStrategy
    Anihub = AnihubStrategy
