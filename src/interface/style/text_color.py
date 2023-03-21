from enum import Enum


class TextColor(Enum):
    DEFAULT = 39
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    LIGHT_GRAY = 37
    GRAY = 90
    LIGHT_RED = 91
    LIGHT_GREEN = 92
    LIGHT_YELLOW = 93
    LIGHT_BLUE = 94
    LIGHT_MAGENTA = 95
    LIGHT_CYAN = 96
    WHITE = 97


if __name__ == '__main__':
    print('Demonstração...')
    print("\033[39mMensagem personalizada, numero = 39\033[0m")
    print("\033[30mMensagem personalizada, numero = 30\033[0m")
    print("\033[31mMensagem personalizada, numero = 31\033[0m")
    print("\033[32mMensagem personalizada, numero = 32\033[0m")
    print("\033[33mMensagem personalizada, numero = 33\033[0m")
    print("\033[34mMensagem personalizada, numero = 34\033[0m")
    print("\033[35mMensagem personalizada, numero = 35\033[0m")
    print("\033[36mMensagem personalizada, numero = 36\033[0m")
    print("\033[37mMensagem personalizada, numero = 37\033[0m")
    print("\033[90mMensagem personalizada, numero = 90\033[0m")
    print("\033[91mMensagem personalizada, numero = 91\033[0m")
    print("\033[92mMensagem personalizada, numero = 92\033[0m")
    print("\033[93mMensagem personalizada, numero = 93\033[0m")
    print("\033[94mMensagem personalizada, numero = 94\033[0m")
    print("\033[95mMensagem personalizada, numero = 95\033[0m")
    print("\033[96mMensagem personalizada, numero = 96\033[0m")
    print("\033[97mMensagem personalizada, numero = 97\033[0m")
