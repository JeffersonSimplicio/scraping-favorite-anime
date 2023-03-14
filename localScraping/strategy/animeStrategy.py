from os import mkdir
from shutil import rmtree
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
from writers import writeTxt, writeJson, writeImg


class AnimeStrategy(ABC):  # Interface
    # Filters
    @abstractmethod
    def __get_cards(cls, code: BeautifulSoup):  # -> ResultSet[Tag]
        raise NotImplementedError

    @abstractmethod
    def __get_names(cls, code: BeautifulSoup):  # -> ResultSet[Tag]
        raise NotImplementedError

    @abstractmethod
    def __get_name(cls, anime: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def __get_thunb(cls, anime: str) -> str:
        raise NotImplementedError

    # Get data from HTML
    @classmethod
    def code(cls, code: BeautifulSoup) -> str:
        return code.prettify()

    @abstractmethod
    def len_favorites(cls, code: BeautifulSoup) -> int:
        raise NotImplementedError

    @classmethod
    def list_favorites_name(
        cls,
        get_names
    ) -> list:
        favorites_list = get_names
        names_list = [divName.string for divName in favorites_list]
        return names_list

    @classmethod
    def list_name_thunb(
        cls,
        get_cards,
        get_name,
        get_thunb
    ) -> list:
        favorites_list = get_cards
        name_thunb = []
        for anime in favorites_list:
            name = get_name(anime)
            thunb_url = get_thunb(anime)
            name_thunb.append(
                {
                    'name': name,
                    'thunb_url': thunb_url
                }
            )
        return name_thunb

    @classmethod
    def list_name_thunb_local(
        cls,
        get_cards,
        get_name,
        get_thunb
    ) -> list:
        print('Por favor, aguarde! Isso pode demorar um pouco...')
        favorites_list = get_cards
        name_thunb = []

        try:
            mkdir('./thunbs')
        except FileExistsError:
            rmtree('./thunbs')
            mkdir('./thunbs')

        for anime in favorites_list:

            name = get_name(anime)
            thunb_url = get_thunb(anime)

            path = writeImg(thunb_url, name)

            name_thunb.append(
                {
                    'name': name,
                    'thunb_url': path
                }
            )

        return name_thunb

    # Create file
    @classmethod
    def file_favorites(
        cls,
        list_favorites_name
    ) -> None:
        writeTxt(list_favorites_name)

    @classmethod
    def file_favorites_url(
        cls,
        list_name_thunb
    ) -> None:
        list_animes = list_name_thunb
        format_list = [
            f'{anime["name"]} - {anime["thunb_url"]}\n'
            for anime in list_animes
        ]
        writeTxt(format_list)

    @classmethod
    def file_name_thunb(
        cls,
        list_name_thunb
    ) -> None:
        writeJson(list_name_thunb)

    @classmethod
    def file_name_thunb_local(
        cls,
        list_name_thunb_local
    ) -> None:
        writeJson(list_name_thunb_local)

    @staticmethod
    def identifier(code: BeautifulSoup) -> bool:
        raise NotImplementedError
