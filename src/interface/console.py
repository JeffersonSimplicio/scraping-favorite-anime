class Console():
    @staticmethod
    def total_favorites(total: int) -> None:
        if (total == 0):
            print('Você não possui nenhum anime na lista de favoritos')
        elif (total == 1):
            print('Você possui 1 anime na lista de favoritos')
        else:
            print(f'Você possui {total} animes favoritos')
