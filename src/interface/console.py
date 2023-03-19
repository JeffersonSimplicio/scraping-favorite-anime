import os
from time import sleep


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
