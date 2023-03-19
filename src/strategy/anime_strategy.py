from os import mkdir
from shutil import rmtree
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
from utils.writers import Write
from utils.image_name_generator import image_name_generator


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
    def len_favorites(cls, cards) -> int:
        return len(cards)

    @classmethod
    def list_favorites_name(cls, get_names) -> list:
        favorites_list = get_names
        names_list = [divName.string for divName in favorites_list]
        return names_list

    @classmethod
    def list_name_thunb(cls, get_cards, get_name, get_thunb) -> list:
        favorites_list = get_cards
        name_thunb = []
        for anime in favorites_list:
            name = get_name(anime)
            thunb_url = get_thunb(anime)
            name_thunb.append({"name": name, "thunb_url": thunb_url})
        return name_thunb

    # Create file
    @classmethod
    def create_txt_list_favorites(
        cls, list_favorites_name, name_file: str = ""
    ) -> None:
        if name_file != "":
            return Write.txt(list_favorites_name, name_file)
        Write.txt(list_favorites_name)

    @classmethod
    def create_txt_list_favorites_url(
        cls, list_name_thunb, name_file: str = ""
    ) -> None:
        list_animes = list_name_thunb
        format_list = [
            f'{anime["name"]} - {anime["thunb_url"]}\n'
            for anime in list_animes
        ]
        if name_file != "":
            return Write.txt(format_list, name_file)
        Write.txt(format_list)

    @classmethod
    def create_json_list_favorites_url(
        cls, list_name_thunb, name_file: str = ""
    ) -> None:
        if name_file != "":
            return Write.json(list_name_thunb, name_file)
        Write.json(list_name_thunb)

    @classmethod
    def create_json_list_favorites_local(
        cls, list_name_thunb, name_file: str = "", extension: str = "jpg"
    ) -> None:
        print("Por favor, aguarde! Isso pode demorar um pouco...")

        try:
            mkdir("./thunbs")
        except FileExistsError:
            rmtree("./thunbs")
            mkdir("./thunbs")

        name_thunb = []

        for anime in list_name_thunb:
            image_name = image_name_generator(anime["name"])
            Write.img(anime["thunb_url"], image_name, extension)
            name_thunb.append(
                {
                    "name": anime["name"],
                    "thunb_url": f"/thunbs/{image_name}.{extension}",
                }
            )

        if name_file != "":
            return Write.json(name_thunb, name_file)
        Write.json(name_thunb)

    @staticmethod
    def identifier(code: BeautifulSoup) -> bool:
        raise NotImplementedError
