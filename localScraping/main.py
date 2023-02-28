from os import mkdir
from shutil import rmtree
from bs4 import BeautifulSoup
from readers import readFile
from writers import writeTxt, writeJson, writeImg


class FavoritesAnimes:
    def __init__(self, code: BeautifulSoup):
        self.__code = code

    def code(self):
        return self.__code.prettify()

    def len_favorites(self) -> int:
        return len(self.__code.find_all('article'))

    def __get_cards(self):
        cards_list = self.__code.select('div.card-vertical')
        return cards_list

    @staticmethod
    def __get_name(anime):
        name = anime.select_one('div.card-vertical-title').string
        return name

    @staticmethod
    def __get_thunb(anime):
        thunb = anime.select_one('div.card-vertical-img img')['src']
        return thunb

    def list_favorites_name(self) -> list:
        favorites_list = self.__code.find_all(
            'div',
            {"class": "card-vertical-title"}
        )
        names_list = [divName.string for divName in favorites_list]
        return names_list

    def name_thunb(self) -> None:
        favorites_list = self.__get_cards()
        name_thunb = []
        for anime in favorites_list:
            thunb_url = self.__get_thunb(anime)
            name = self.__get_name(anime)
            name_thunb.append(
                {
                    'name': name,
                    'thunb_url': thunb_url
                }
            )
        return name_thunb

    def __name_thunb_local(self) -> None:
        print('Por favor, aguarde! Isso pode demorar um pouco...')
        favorites_list = self.__get_cards()
        name_thunb = []

        try:
            mkdir('./thunbs')
        except FileExistsError:
            rmtree('./thunbs')
            mkdir('./thunbs')

        for anime in favorites_list:

            thunb_url = self.__get_thunb(anime)
            name = self.__get_name(anime)

            path = writeImg(thunb_url, name)

            name_thunb.append(
                {
                    'name': name,
                    'thunb_url': path
                }
            )

        return name_thunb

    def file_favorites(self) -> None:
        writeTxt(self.list_favorites_name())

    def file_name_thunb(self) -> None:
        writeJson(self.name_thunb())

    def file_name_thunb_local(self) -> None:
        writeJson(self.__name_thunb_local())


# Test Zone
if __name__ == '__main__':
    code = readFile('favorites-list-page.html')
    soup = BeautifulSoup(code, "html.parser")

    betterAnime = FavoritesAnimes(soup)

    betterAnime.file_name_thunb_local()
