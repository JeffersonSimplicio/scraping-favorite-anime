from src.strategy.main import FavoritesAnimes
from src.interface.style.main_style import MainStyle

controls_style = MainStyle()


class Controls:
    def operation(favorite: FavoritesAnimes, selected: int) -> None:
        if selected == 1:
            favorite.create_txt_list_favorites()
        elif selected == 2:
            favorite.create_txt_list_favorites_url()
        elif selected == 3:
            favorite.create_json_list_favorites_url()
        elif selected == 4:
            favorite.create_json_list_favorites_local()
        else:
            print(
                controls_style.fail
                + "Opção inexistente!"
                + controls_style.reset
            )

    def empty_file(total: int) -> bool:
        if total == 0:
            option = ["", "S", "N"]
            text = (
                "Você não possui animes favoritos, "
                + "o arquivo gerado sera vazio\n"
                + "Deseja gerar o arquivo mesmo assim?"
                + "(s/n)(Padrão - Não): "
            )

            while True:
                try:
                    response = str(input(text)).strip().upper()
                    if response == option[0]:
                        print("Foi selecionada a opção padrão - opção N")
                        return False
                    elif response[0] == option[1]:
                        return True
                    elif response[0] == option[2]:
                        return False
                except ValueError: 
                    print(
                        controls_style.alert
                        + "Selecione uma opção valida!"
                        + controls_style.reset
                    )
        return True
