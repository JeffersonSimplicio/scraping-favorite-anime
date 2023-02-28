from os import mkdir
from shutil import rmtree
import asyncio
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

    def list_favorites_name(self) -> list:
        favorites_list = self.__code.find_all(
            'div',
            {"class": "card-vertical-title"}
        )
        names_list = [divName.string for divName in favorites_list]
        return names_list

    def name_thunb(self) -> None:
        favorites_list = self.__code.select('div.card-vertical')
        name_thunb = []
        for anime in favorites_list:
            thunb = anime.select_one('div.card-vertical-img img')['src']
            name = anime.select_one('div.card-vertical-title').string
            name_thunb.append(
                {
                    'name': name,
                    'thunb_url': thunb
                }
            )
        return name_thunb

    async def name_thunb_local(self) -> None:
        favorites_list = self.__code.select('div.card-vertical')
        name_thunb = []

        for anime in favorites_list:

            thunb_url = anime.select_one('div.card-vertical-img img')['src']
            name = anime.select_one('div.card-vertical-title').string

            try:
                mkdir('./thunbs')
            except FileExistsError:
                rmtree('./thunbs')
                mkdir('./thunbs')

            path = await writeImg(thunb_url, name)

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


# Test Zone
if __name__ == '__main__':
    code = readFile('favorites-list-page.html')
    soup = BeautifulSoup(code, "html.parser")

    betterAnime = FavoritesAnimes(soup)

    x = asyncio.run(betterAnime.name_thunb_local())
    print(x)
