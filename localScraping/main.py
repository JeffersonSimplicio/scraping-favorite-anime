from bs4 import BeautifulSoup
from readers import readFile
from writers import writeTxt


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

    def file_favorites(self) -> None:
        writeTxt(self.list_favorites_name())

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


# Test Zone
if __name__ == '__main__':
    code = readFile('favorites-list-page.html')
    soup = BeautifulSoup(code, "html.parser")

    betterAnime = FavoritesAnimes(soup)

    x = betterAnime.name_thunb()

    for i in x:
        print(i)
