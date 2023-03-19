from bs4 import BeautifulSoup
from src.strategy.anime_strategy import AnimeStrategy


class AnimeFireStrategy(AnimeStrategy):
    # Default name files
    TYPE_JSON = ".json"
    TYPE_TXT = ".txt"
    DEFAULT_NAME = "favorites_animefire"

    # Filters
    @classmethod
    def __get_cards(cls, code: BeautifulSoup):  # -> ResultSet[Tag]
        cards_list = code.select("article.card.cardUltimosEps")
        return cards_list

    @classmethod
    def __get_names(cls, code: BeautifulSoup):  # -> ResultSet[Tag]
        favorites_list = code.select("h3.animeTitle")
        return favorites_list

    @staticmethod
    def __get_name(anime: str) -> str:
        name = anime.select_one("h3.animeTitle").string
        return name

    @staticmethod
    def __get_thunb(anime: str) -> str:
        thunb = anime.select_one(
            "img.card-img-top.imgAnimes.transitioning_src"
        )["src"]
        return thunb

    # Get data from HTML
    @classmethod
    def code(cls, code: BeautifulSoup) -> str:
        return super().code(code)

    @classmethod
    def len_favorites(cls, code: BeautifulSoup) -> int:
        return super().len_favorites(cls.__get_cards(code))

    @classmethod
    def list_favorites_name(cls, code: BeautifulSoup) -> list:
        return super().list_favorites_name(cls.__get_names(code))

    @classmethod
    def list_name_thunb(cls, code: BeautifulSoup) -> list:
        return super().list_name_thunb(
            cls.__get_cards(code), cls.__get_name, cls.__get_thunb
        )

    # Create file
    @classmethod
    def create_txt_list_favorites(cls, code: BeautifulSoup) -> None:
        super().create_txt_list_favorites(
            cls.list_favorites_name(code),
            f"name_{cls.DEFAULT_NAME}{cls.TYPE_TXT}",
        )

    @classmethod
    def create_txt_list_favorites_url(cls, code: BeautifulSoup) -> None:
        return super().create_txt_list_favorites_url(
            cls.list_name_thunb(code),
            f"name_url_{cls.DEFAULT_NAME}{cls.TYPE_TXT}",
        )

    @classmethod
    def create_json_list_favorites_url(cls, code: BeautifulSoup) -> None:
        return super().create_json_list_favorites_url(
            cls.list_name_thunb(code),
            f"name_url_{cls.DEFAULT_NAME}{cls.TYPE_JSON}",
        )

    @classmethod
    def create_json_list_favorites_local(cls, code: BeautifulSoup) -> None:
        return super().create_json_list_favorites_local(
            cls.list_name_thunb(code),
            f"name_local_{cls.DEFAULT_NAME}{cls.TYPE_JSON}",
            "webp",
        )

    @staticmethod
    def identifier(code: BeautifulSoup) -> bool:
        if code.select_one("div.row.ml-1.mr-1"):
            return True
        elif code.select_one("div#body-content"):
            return True
        elif code.select_one("div.container.mt-5"):
            return True
        return False
