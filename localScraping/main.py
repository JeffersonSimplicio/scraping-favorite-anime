from strategy.animeStrategy import AnimeStrategy
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
    def file_favorites(self) -> None:
        self.__anime_strategy.file_favorites(self.__soup)

    def file_favorites_url(self) -> None:
        self.__anime_strategy.file_favorites_url(self.__soup)

    def file_name_thunb(self) -> None:
        self.__anime_strategy.file_name_thunb(self.__soup)

    def file_name_thunb_local(self) -> None:
        self.__anime_strategy.file_name_thunb_local(self.__soup)

    def identifier(self) -> bool:
        return self.__anime_strategy.identifier(self.__soup)


# Test Zone
if __name__ == '__main__':
    from strategy.baStrategy import BetterAnimeStrategy
    from strategy.anihubStrategy import AnihubStrategy
    from readers import readFile

    ba_nf = 'pages/betterAnime/betterAnime-NF.html'
    ba_page = 'pages/betterAnime/betterAnime_page.html'
    ba_body = 'pages/betterAnime/betterAnime_body.html'

    anihub_nf = 'pages/anihub/anihub-NF.html'
    anihub_page = 'pages/anihub/anihub_page.html'
    anihub_body = 'pages/anihub/anihub_body.html'

    code = readFile(anihub_body)
    soup = BeautifulSoup(code, "html.parser")

    anihub = FavoritesAnimes(AnihubStrategy, soup)
    betterAnime = FavoritesAnimes(BetterAnimeStrategy, soup)

    resultAni = anihub.identifier()
    resultBA = betterAnime.identifier()

    print(resultAni)
    print(resultBA)
