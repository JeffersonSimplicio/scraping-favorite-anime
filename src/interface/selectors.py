from bs4 import BeautifulSoup
from src.utils.readers import Read
from src.utils.web_site_identifier import web_site_identifier
from src.utils.create_list_options import create_list_options
from src.strategy.list_stratege import Strategys
from src.interface.console import Console
from src.interface.style.main_style import MainStyle

selectors_style = MainStyle()


class Selectors:
    DELAY_TIME = 1

    @classmethod
    def file(cls) -> str:
        DEFAULT_PATH = "favorites-list-page.html"
        text = (
            "Qual arquivo deseja utilizar?"
            + selectors_style.default_value
            + f"({DEFAULT_PATH}) "
            + selectors_style.reset
        )
        while True:
            try:
                path_file = str(input(text)).strip()
                path = DEFAULT_PATH if path_file == "" else path_file
                if path_file == DEFAULT_PATH:
                    Console.self_destruct_message(
                        "Foi selecionado o arquivo padrão ", cls.DELAY_TIME
                    )
                code = Read.file(path)
                return code
            except FileNotFoundError:
                print(
                    selectors_style.fail
                    + "Arquivo não encontrado"
                    + selectors_style.reset
                )

    @classmethod
    def filter(cls, soup: BeautifulSoup):
        try:
            filter = web_site_identifier(soup)
            return filter
        except ValueError:
            option = create_list_options()
            print(
                selectors_style.fail
                + "Não foi possível identificar a qual site pertence o código"
                + selectors_style.reset
            )

            while True:
                try:
                    print("Filtros disponíveis:")
                    for i, web in enumerate(Strategys):
                        print(f"{i + 1} - {web.name}")

                    selected = str(input(
                        "\nQual opção escolhida(Padrão - 1): "
                    )).strip()

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
                    Console.alert("Selecione uma opção valida!")

    @classmethod
    def options(cls) -> None:
        option = ["", "1", "2", "3", "4"]
        text = """Opções disponíveis:
1 - Lista de nomes(txt)
2 - Lista com nome e URL da thumb(txt)
3 - Lista com nome e URL da thumb(json)
4 - Lista com nome e path da thumb(download da thumb)(json)

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
                Console.alert("Selecione uma opção valida!")

    @classmethod
    def willContinue(cls) -> bool:
        option = ["", "S", "N"]
        text = (
            "Deseja gerar uma nova lista, "
            + "baseado no mesmo site?(S/N) - Padrão N"
        )
        while True:
            try:
                selected = str(input(text)).strip().upper()
                if selected in option:
                    if selected == option[0]:
                        Console.self_destruct_message(
                            "Foi selecionada a opção padrão - opção N",
                            cls.DELAY_TIME,
                        )
                        Console.clear()
                        return False
                    else:
                        Console.clear()
                        return selected == option[1]
                Console.clear()
                raise ValueError
            except ValueError:
                Console.alert("Selecione uma opção valida!")
