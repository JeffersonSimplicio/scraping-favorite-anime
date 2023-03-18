import json
import requests


class Write():
    def txt(
        animes_list: list,
        name_file: str = 'FavoritesAnimes.txt'
    ) -> None:
        with open(name_file, 'w', encoding="utf-8") as file:
            for anime in animes_list:
                file.write(f'{anime}\n')
        print('Escrita concluída')

    def json(
        names_thunbs: list,
        name_file: str = 'FavoritesAnimes.json'
    ) -> None:
        with open(name_file, 'w', encoding="utf-8") as file:
            json_to_write = json.dumps(names_thunbs)
            file.write(json_to_write)
        print('Escrita concluída')

    def img(
        image_url: str,
        name: str,
        extension: str = 'jpg'
    ) -> None:
        img_data = requests.get(image_url).content
        with open(
            f'thunbs/{name}.{extension}',
            'wb'
        ) as handler:
            handler.write(img_data)
