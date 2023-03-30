import os
from time import sleep
from src.interface.style.main_style import MainStyle

console_style = MainStyle()


class Console:
    @staticmethod
    def total_favorites(total: int) -> None:
        if total == 0:
            print("Você não possui nenhum anime na lista de favoritos")
        elif total == 1:
            print("Você possui 1 anime na lista de favoritos")
        else:
            print(f"Você possui {total} animes favoritos")

    @staticmethod
    def clear(seconds: int = 0) -> None:
        sleep(seconds)
        os.system("cls" if os.name == "nt" else "clear")

    @classmethod
    def self_destruct_message(cls, msg: str, seconds: int):
        print(msg)
        cls.clear(seconds)

    @staticmethod
    def alert(cls, msg: str, seconds: int = -1) -> None:
        print(console_style.alert + msg + console_style.reset)
        if seconds > 0:
            cls.clear(seconds)
