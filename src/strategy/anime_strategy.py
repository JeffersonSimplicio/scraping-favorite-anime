from os import mkdir
from shutil import rmtree
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
from src.utils.writers import Write
from src.utils.image_name_generator import image_name_generator


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
    def __get_thumb(cls, anime: str) -> str:
        raise NotImplementedError

    # Get data from HTML
    @staticmethod
    def code(code: BeautifulSoup) -> str:
        return code.prettify()

    @staticmethod
    def len_favorites(cards) -> int:
        return len(cards)

    @staticmethod
    def list_favorites_name(get_names) -> list:
        favorites_list = get_names
        names_list = [divName.string for divName in favorites_list]
        return names_list

    @staticmethod
    def list_name_thumb(get_cards, get_name, get_thumb) -> list:
        favorites_list = get_cards
        name_thumb = []
        for anime in favorites_list:
            name = get_name(anime)
            thumb_url = get_thumb(anime)
            name_thumb.append({"name": name, "thumb_url": thumb_url})
        return name_thumb

    # Create file
    @staticmethod
    def create_txt_list_favorites(
        list_favorites_name, name_file: str = ""
    ) -> None:
        if name_file != "":
            return Write.txt(list_favorites_name, name_file)
        Write.txt(list_favorites_name)

    @staticmethod
    def create_txt_list_favorites_url(
        list_name_thumb, name_file: str = ""
    ) -> None:
        list_animes = list_name_thumb
        format_list = [
            f'{anime["name"]} - {anime["thumb_url"]}\n'
            for anime in list_animes
        ]
        if name_file != "":
            return Write.txt(format_list, name_file)
        Write.txt(format_list)

    @staticmethod
    def create_json_list_favorites_url(
        list_name_thumb, name_file: str = ""
    ) -> None:
        if name_file != "":
            return Write.json(list_name_thumb, name_file)
        Write.json(list_name_thumb)

    @staticmethod
    def create_json_list_favorites_local(
        list_name_thumb, name_file: str = "", extension: str = "jpg"
    ) -> None:
        print("Por favor, aguarde! Isso pode demorar um pouco...")

        try:
            mkdir("./thumbs")
        except FileExistsError:
            rmtree("./thumbs")
            mkdir("./thumbs")

        name_thumb = []

        for anime in list_name_thumb:
            image_name = image_name_generator(anime["name"])
            Write.img(anime["thumb_url"], image_name, extension)
            name_thumb.append(
                {
                    "name": anime["name"],
                    "thumb_url": f"/thumbs/{image_name}.{extension}",
                }
            )

        if name_file != "":
            return Write.json(name_thumb, name_file)
        Write.json(name_thumb)

    @abstractmethod
    def identifier(code: BeautifulSoup) -> bool:
        raise NotImplementedError
