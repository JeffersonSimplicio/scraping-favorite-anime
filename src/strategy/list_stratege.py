from enum import Enum
from src.strategy.anihub_strategy import AnihubStrategy
from src.strategy.ba_strategy import BetterAnimeStrategy
from src.strategy.af_strategy import AnimeFireStrategy


class Strategys(Enum):
    BetterAnime = BetterAnimeStrategy
    Anihub = AnihubStrategy
    AnimeFire = AnimeFireStrategy
