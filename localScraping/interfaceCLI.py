from bs4 import BeautifulSoup
from readers import readFile
from main import FavoritesAnimes


def select_file():
    path_file = str(
        input("Qual arquivo deseja utilizar?(favorites-list-page.html) ")
    ).strip()
    path = 'favorites-list-page.html' if path_file == '' else path_file
    code = readFile(path)
    return code


def interface():
    code = select_file()
    soup = BeautifulSoup(code, "html.parser")
    betterAnime = FavoritesAnimes(soup)
    print(f'Você possui {betterAnime.len_favorites()} animes favoritos')


interface()
