from bs4 import BeautifulSoup
from readers import readFile
from main import FavoritesAnimes
from strategy.baStrategy import BetterAnimeStrategy


def select_file():
    text = "Qual arquivo deseja utilizar?(favorites-list-page.html) "
    while True:
        try:
            path_file = str(input(text)).strip()
            path = 'favorites-list-page.html' if path_file == '' else path_file
            code = readFile(path)
            return code
        except FileNotFoundError:
            print('Arquivo não encontrado')


def select_option():
    option = ['', '1', '2', '3', '4']
    text = """1 - Lista de nomes(txt)
2 - Lista com nome e URL da thunb(txt)
3 - Lista com nome e URL da thunb(json)
4 - Lista com nome e path da thumb(download da thunb)(json)

Qual opção escolhida(Padrão - 2): """

    while True:
        try:
            selected = str(input(text))
            if selected in option:
                if selected == option[0]:
                    print('Foi selecionada a opção padrão - opção 2')
                    return 2
                return int(selected)
            raise ValueError
        except ValueError:
            print("Selecione uma opção valida!")


def operation(favorite: FavoritesAnimes, selected: int):
    if selected == 1:
        favorite.file_favorites()
    elif selected == 2:
        favorite.file_favorites_url()
    elif selected == 3:
        favorite.file_name_thunb()
    elif selected == 4:
        favorite.file_name_thunb_local()
    else:
        print('Opção inexistente!')


def interface():
    code = select_file()
    soup = BeautifulSoup(code, "html.parser")
    betterAnime = FavoritesAnimes(BetterAnimeStrategy, soup)
    print(f'Você possui {betterAnime.len_favorites()} animes favoritos')
    selected = select_option()
    operation(betterAnime, selected)


interface()
