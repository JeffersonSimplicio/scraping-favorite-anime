import json
import requests


def writeTxt(names: list, nameFile: str = 'FavoritesAnimes.txt') -> None:
    with open(nameFile, 'w') as file:
        for name in names:
            file.write(f'{name}\n')
    print('Escrita concluída')


def writeJson(names_thunbs: list, nameFile: str = 'FavoritesAnimes.json'):
    with open(nameFile, 'w') as file:
        json_to_write = json.dumps(names_thunbs)
        file.write(json_to_write)
    print('Escrita concluída')


def writeImg(image_url: str, name: str) -> None:
    path = name.strip().lower()
    path = path.replace(" ", "_").replace(":", "_").replace("/", "_")
    img_data = requests.get(image_url).content

    with open(
        f'thunbs/{path}.jpg',
        'wb'
    ) as handler:
        handler.write(img_data)

    return f'thunbs/{path}.jpg'
