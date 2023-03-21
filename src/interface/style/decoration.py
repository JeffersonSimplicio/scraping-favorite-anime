from enum import Enum


class Decoration(Enum):
    NORMAL = 0
    BOLD = 1
    DIM = 2
    ITALIC = 3
    UNDERLINE = 4
    BLINK = 5
    REVERSE = 7
    HIDDEN = 8
    TACHADO = 9


if __name__ == '__main__':
    print('Demonstração...')
    print("\033[1mMensagem personalizada, numero = 0\033[0m")
    print("\033[2mMensagem personalizada, numero = 1\033[0m")
    print("\033[3mMensagem personalizada, numero = 2\033[0m")
    print("\033[0mMensagem personalizada, numero = 3\033[0m")
    print("\033[4mMensagem personalizada, numero = 4\033[0m")
    print("\033[5mMensagem personalizada, numero = 5\033[0m")
    print("\033[7mMensagem personalizada, numero = 7\033[0m")
    print("\033[8mMensagem personalizada, numero = 8\033[0m")
    print("\033[9mMensagem personalizada, numero = 9\033[0m")
