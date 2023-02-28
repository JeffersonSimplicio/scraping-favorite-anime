import json


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
