from enum import Enum


class BackgroundColor(Enum):
    DEFAULT = 49
    BLACK = 40
    RED = 41
    GREEN = 42
    YELLOW = 43
    BLUE = 44
    MAGENTA = 45
    CYAN = 46
    LIGHT_GRAY = 47
    GRAY = 100
    LIGHT_RED = 101
    LIGHT_GREEN = 102
    LIGHT_YELLOW = 103
    LIGHT_BLUE = 104
    LIGHT_MAGENTA = 105
    LIGHT_CYAN = 106
    WHITE = 107


if __name__ == "__main__":
    print("Demonstração...")
    print("\033[49mMensagem personalizada, numero = 49\033[0m")
    print("\033[40mMensagem personalizada, numero = 40\033[0m")
    print("\033[41mMensagem personalizada, numero = 41\033[0m")
    print("\033[42mMensagem personalizada, numero = 42\033[0m")
    print("\033[43mMensagem personalizada, numero = 43\033[0m")
    print("\033[44mMensagem personalizada, numero = 44\033[0m")
    print("\033[45mMensagem personalizada, numero = 45\033[0m")
    print("\033[46mMensagem personalizada, numero = 46\033[0m")
    print("\033[47mMensagem personalizada, numero = 47\033[0m")
    print("\033[100mMensagem personalizada, numero = 100\033[0m")
    print("\033[101mMensagem personalizada, numero = 101\033[0m")
    print("\033[102mMensagem personalizada, numero = 102\033[0m")
    print("\033[103mMensagem personalizada, numero = 103\033[0m")
    print("\033[104mMensagem personalizada, numero = 104\033[0m")
    print("\033[105mMensagem personalizada, numero = 105\033[0m")
    print("\033[106mMensagem personalizada, numero = 106\033[0m")
    print("\033[107mMensagem personalizada, numero = 107\033[0m")
