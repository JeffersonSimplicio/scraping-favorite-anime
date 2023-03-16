from strategy.anime_strategy import AnimeStrategy
from bs4 import BeautifulSoup


class FavoritesAnimes():
    def __init__(
        self,
        anime_strategy: AnimeStrategy,
        soup: BeautifulSoup
    ) -> None:
        self.__anime_strategy = anime_strategy
        self.__soup = soup

    # Get data from HTML
    def code(self) -> str:
        return self.__anime_strategy.code(self.__soup)

    def len_favorites(self) -> int:
        return self.__anime_strategy.len_favorites(self.__soup)

    def list_favorites_name(self) -> list:
        return self.__anime_strategy.list_favorites_name(self.__soup)

    def list_name_thunb(self) -> list:
        return self.__anime_strategy.list_name_thunb(self.__soup)

    def list_name_thunb_local(self) -> list:
        return self.__anime_strategy.list_name_thunb_local(self.__soup)

    # Create file
    def create_txt_list_favorites(self) -> None:
        self.__anime_strategy.create_txt_list_favorites(self.__soup)

    def create_txt_list_favorites_url(self) -> None:
        self.__anime_strategy.create_txt_list_favorites_url(self.__soup)

    def create_json_list_favorites_url(self) -> None:
        self.__anime_strategy.create_json_list_favorites_url(self.__soup)

    def create_json_list_favorites_local(self) -> None:
        self.__anime_strategy.create_json_list_favorites_local(self.__soup)

    def identifier(self) -> bool:
        return self.__anime_strategy.identifier(self.__soup)
