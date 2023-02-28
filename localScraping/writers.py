def writeTxt(names: list, nameFile: str = 'FavoritesAnimes.txt') -> None:
    with open(nameFile, 'w') as file:
        for name in names:
            file.write(f'{name}\n')
    print('Escrita concluída')
