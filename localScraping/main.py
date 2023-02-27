from bs4 import BeautifulSoup


class FavoritesAnimes:
    def __init__(self, code: BeautifulSoup):
        self.__code = code

    def code(self):
        return self.__code.prettify()

    def len_favorites(self) -> int:
        return len(self.__code.find_all('article'))
