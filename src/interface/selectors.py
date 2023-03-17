from bs4 import BeautifulSoup
from utils.readers import read_file
from utils.web_site_identifier import web_site_identifier
from strategy.ba_strategy import BetterAnimeStrategy
from strategy.anihub_strategy import AnihubStrategy
from interface.console import Console


class Selectors():
    @staticmethod
    def file() -> str:
        DEFAULT_PATH = 'favorites-list-page.html'
        text = f"Qual arquivo deseja utilizar?({DEFAULT_PATH}) "
        while True:
            try:
                path_file = str(input(text)).strip()
                path = DEFAULT_PATH if path_file == '' else path_file
                Console.clear()
                code = read_file(path)
                return code
            except FileNotFoundError:
                print('Arquivo não encontrado')

    @staticmethod
    def filter(soup: BeautifulSoup):
        try:
            filter = web_site_identifier(soup)
            return filter
        except ValueError:
            option = ['', '1', '2']
            text = '''Filtros disponíveis:
1 - BetterAnime
2 - Anihub

Qual opção escolhida(Padrão - 1): '''

            print('Não foi possível identificar a qual site pertence o código')

            while True:
                try:
                    selected = str(input(text)).strip()
                    if selected in option:
                        if selected == option[0]:
                            Console.self_destruct_message(
                                'Foi selecionada a opção padrão - opção 1', 1
                            )
                            return BetterAnimeStrategy
                        elif selected == option[1]:
                            Console.clear()
                            return BetterAnimeStrategy
                        elif selected == option[2]:
                            Console.clear()
                            return AnihubStrategy
                    Console.clear()
                    raise ValueError
                except ValueError:
                    print("Selecione uma opção valida!")

    @staticmethod
    def options() -> None:
        option = ['', '1', '2', '3', '4']
        text = """Opções disponíveis:
1 - Lista de nomes(txt)
2 - Lista com nome e URL da thunb(txt)
3 - Lista com nome e URL da thunb(json)
4 - Lista com nome e path da thumb(download da thunb)(json)

Qual opção escolhida?(Padrão - 2) """

        while True:
            try:
                selected = str(input(text)).strip()
                if selected in option:
                    if selected == option[0]:
                        Console.self_destruct_message(
                                'Foi selecionada a opção padrão - opção 2', 1
                            )
                        return 2
                    Console.clear()
                    return int(selected)
                Console.clear()
                raise ValueError
            except ValueError:
                print("Selecione uma opção valida!")