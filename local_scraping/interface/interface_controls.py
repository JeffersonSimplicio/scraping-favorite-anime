from utils.readers import read_file
from utils.web_site_identifier import web_site_identifier
from strategy.main import FavoritesAnimes
from strategy.ba_strategy import BetterAnimeStrategy
from strategy.anihub_strategy import AnihubStrategy


def select_file():
    text = "Qual arquivo deseja utilizar?(favorites-list-page.html) "
    while True:
        try:
            path_file = str(input(text)).strip()
            path = 'favorites-list-page.html' if path_file == '' else path_file
            code = read_file(path)
            return code
        except FileNotFoundError:
            print('Arquivo não encontrado')


def select_filter(soup):
    try:
        filter = web_site_identifier(soup)
        return filter
    except ValueError:
        option = ['', '1', '2']
        text = '''1 - BetterAnime
2 - Anihub

Qual opção escolhida(Padrão - 1): '''
        print('Não foi possível identificar a qual site pertence o código')

        while True:
            try:
                selected = str(input(text)).strip()
                if selected in option:
                    if selected == option[0]:
                        print('Foi selecionada a opção padrão - opção 1')
                        return BetterAnimeStrategy
                    elif selected == option[1]:
                        return BetterAnimeStrategy
                    elif selected == option[2]:
                        return AnihubStrategy
                raise ValueError
            except ValueError:
                print("Selecione uma opção valida!")


def select_option():
    option = ['', '1', '2', '3', '4']
    text = """1 - Lista de nomes(txt)
2 - Lista com nome e URL da thunb(txt)
3 - Lista com nome e URL da thunb(json)
4 - Lista com nome e path da thumb(download da thunb)(json)

Qual opção escolhida(Padrão - 2): """

    while True:
        try:
            selected = str(input(text)).strip()
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
