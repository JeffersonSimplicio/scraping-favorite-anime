import json
import requests


class Write:
    @staticmethod
    def txt(animes_list: list, name_file: str = "FavoritesAnimes.txt") -> None:
        with open(name_file, "w", encoding="utf-8") as file:
            for anime in animes_list:
                no_space_anime = anime.strip()
                file.write(f"{no_space_anime}\n")
        print("Escrita concluída")

    @staticmethod
    def json(
        names_thumbs: list, name_file: str = "FavoritesAnimes.json"
    ) -> None:
        with open(name_file, "w", encoding="utf-8") as file:
            json_to_write = json.dumps(names_thumbs)
            file.write(json_to_write)
        print("Escrita concluída")

    @staticmethod
    def img(image_url: str, name: str, extension: str = "jpg") -> None:
        img_data = requests.get(image_url).content
        with open(f"thumbs/{name}.{extension}", "wb") as handler:
            handler.write(img_data)
