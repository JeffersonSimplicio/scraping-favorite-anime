from bs4 import BeautifulSoup
from strategy.anime_strategy import AnimeStrategy


class AnihubStrategy(AnimeStrategy):
    # Default name files
    TYPE_JSON = '.json'
    TYPE_TXT = '.txt'
    DEFAULT_NAME = 'favorites_anihub'

    # Filters
    @classmethod
    def __get_cards(cls, code: BeautifulSoup):  # -> ResultSet[Tag]
        cards_list = code.select('div.animes')
        return cards_list

    @classmethod
    def __get_names(cls, code: BeautifulSoup):  # -> ResultSet[Tag]
        favorites_list = code.select(
            'div.animes a:first-of-type h1.bottom-div'
        )
        return favorites_list

    @staticmethod
    def __get_name(anime: str) -> str:
        name = anime.select_one('a:first-of-type h1.bottom-div').string
        return name

    @staticmethod
    def __get_thunb(anime: str) -> str:
        thunb = anime.select_one('a:first-of-type img')['src']
        return thunb

    # Get data from HTML
    @classmethod
    def code(cls, code: BeautifulSoup) -> str:
        return super().code(code)

    @classmethod
    def len_favorites(cls, code: BeautifulSoup) -> int:
        return len(code.select('div.animes'))

    @classmethod
    def list_favorites_name(cls, code: BeautifulSoup) -> list:
        return super().list_favorites_name(cls.__get_names(code))

    @classmethod
    def list_name_thunb(cls, code: BeautifulSoup) -> list:
        return super().list_name_thunb(
            cls.__get_cards(code),
            cls.__get_name,
            cls.__get_thunb
        )

    @classmethod
    def list_name_thunb_local(cls, code: BeautifulSoup) -> list:
        return super().list_name_thunb_local(
            cls.__get_cards(code),
            cls.__get_name,
            cls.__get_thunb
        )

    # Create file
    @classmethod
    def create_txt_list_favorites(cls, code: BeautifulSoup) -> None:
        super().create_txt_list_favorites(
            cls.list_favorites_name(code),
            f'name_{cls.DEFAULT_NAME}{cls.TYPE_TXT}'
        )

    @classmethod
    def create_txt_list_favorites_url(cls, code: BeautifulSoup) -> None:
        return super().create_txt_list_favorites_url(
            cls.list_name_thunb(code),
            f'name_url_{cls.DEFAULT_NAME}{cls.TYPE_TXT}'
        )

    @classmethod
    def create_json_list_favorites_url(cls, code: BeautifulSoup) -> None:
        return super().create_json_list_favorites_url(
            cls.list_name_thunb(code),
            f'name_url_{cls.DEFAULT_NAME}{cls.TYPE_JSON}'
        )

    @classmethod
    def create_json_list_favorites_local(cls, code: BeautifulSoup) -> None:
        return super().create_json_list_favorites_local(
            cls.list_name_thunb_local(code),
            f'name_local_{cls.DEFAULT_NAME}{cls.TYPE_JSON}'
        )

    @staticmethod
    def identifier(code: BeautifulSoup) -> bool:
        if (code.select_one('h1.cover-photo')):
            return True
        elif (code.select_one('div.grid4.t-center')):
            return True
        elif (code.select_one('div.grid4.grid5')):
            return True
        return False
