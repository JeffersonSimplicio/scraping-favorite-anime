from enum import Enum
from strategy.anihub_strategy import AnihubStrategy
from strategy.ba_strategy import BetterAnimeStrategy
from strategy.af_strategy import AnimeFireStrategy


class Strategys(Enum):
    BetterAnime = BetterAnimeStrategy
    Anihub = AnihubStrategy
    AnimeFire = AnimeFireStrategy
