from bs4 import BeautifulSoup
from src.utils.readers import Read
from src.utils.web_site_identifier import web_site_identifier
from src.strategy.list_stratege import Strategys
from src.interface.console import Console


class Selectors:
    DELAY_TIME = 1

    @classmethod
    def file(cls) -> str:
        DEFAULT_PATH = "favorites-list-page.html"
        text = f"Qual arquivo deseja utilizar?({DEFAULT_PATH}) "
        while True:
            try:
                path_file = str(input(text)).strip()
                path = DEFAULT_PATH if path_file == "" else path_file
                if path_file == DEFAULT_PATH:
                    Console.self_destruct_message(
                        "Foi selecionado o arquivo padrão", cls.DELAY_TIME
                    )
                code = Read.file(path)
                return code
            except FileNotFoundError:
                print("Arquivo não encontrado")

    @classmethod
    def filter(cls, soup: BeautifulSoup):
        try:
            filter = web_site_identifier(soup)
            return filter
        except ValueError:
            option = ["", "BetterAnime", "Anihub", "AnimeFire"]
            text = """Filtros disponíveis:
1 - BetterAnime
2 - Anihub
3 - AnimeFire

Qual opção escolhida(Padrão - 1): """

            print("Não foi possível identificar a qual site pertence o código")

            while True:
                try:
                    selected = str(input(text)).strip()
                    if selected in option:
                        if selected == option[0]:
                            Console.self_destruct_message(
                                "Foi selecionada a opção padrão - opção 1",
                                cls.DELAY_TIME,
                            )
                            return Strategys.BetterAnime.value
                        filter = Strategys[option[int(selected)]].value
                        Console.clear()
                        return filter
                except ValueError:
                    print("Selecione uma opção valida!")

    @classmethod
    def options(cls) -> None:
        option = ["", "1", "2", "3", "4"]
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
                            "Foi selecionada a opção padrão - opção 2",
                            cls.DELAY_TIME,
                        )
                        return 2
                    Console.clear()
                    return int(selected)
                Console.clear()
                raise ValueError
            except ValueError:
                print("Selecione uma opção valida!")
