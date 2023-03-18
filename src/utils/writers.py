import json
import requests


def write_txt(
        animes_list: list,
        name_file: str = 'FavoritesAnimes.txt'
) -> None:
    with open(name_file, 'w', encoding="utf-8") as file:
        for anime in animes_list:
            file.write(f'{anime}\n')
    print('Escrita concluída')


def write_json(names_thunbs: list, name_file: str = 'FavoritesAnimes.json'):
    with open(name_file, 'w', encoding="utf-8") as file:
        json_to_write = json.dumps(names_thunbs)
        file.write(json_to_write)
    print('Escrita concluída')


def write_img(image_url: str, name: str, extension: str = 'jpg') -> None:
    chars = '.,!?'
    path = name.strip().lower()
    path = path.replace(" ", "_").replace(":", "_").replace("/", "_")
    path = path.translate(str.maketrans('', '', chars))
    img_data = requests.get(image_url).content

    with open(
        f'thunbs/{path}.{extension}',
        'wb',
    ) as handler:
        handler.write(img_data)

    return f'thunbs/{path}.{extension}'
