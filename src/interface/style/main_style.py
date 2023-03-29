from src.interface.style.background_color import BackgroundColor
from src.interface.style.text_color import TextColor
from src.interface.style.decoration import Decoration


class MainStyle:
    def __init__(self) -> None:
        self.__reset = "\033[0m"
        self.__success = f"\033[{TextColor.GREEN.value}m"
        self.__fail = f"\033[{TextColor.RED.value}m"
        self.__alert = "\033[{};{};{};{}m".format(
            Decoration.BOLD.value,
            Decoration.ITALIC.value,
            TextColor.RED.value,
            BackgroundColor.YELLOW.value,
        )

    @staticmethod
    def __unalterable_message():
        raise AttributeError("This attribute cannot be changed.")

    @staticmethod
    def __undeletable_message():
        raise AttributeError("This attribute cannot be deleted.")

    # Reset
    @property
    def reset(self):
        return self.__reset

    @reset.setter
    def reset(self):
        self.__unalterable_message()

    @reset.deleter
    def reset(self):
        self.__undeletable_message()

    # Success
    @property
    def success(self):
        return self.__success

    @success.setter
    def success(self):
        self.__unalterable_message()

    @success.deleter
    def success(self):
        self.__undeletable_message()

    # Fail
    @property
    def fail(self):
        return self.__fail

    @fail.setter
    def fail(self):
        self.__unalterable_message()

    @fail.deleter
    def fail(self):
        self.__undeletable_message()

    # Alert
    @property
    def alert(self):
        return self.__alert

    @alert.setter
    def alert(self):
        self.__unalterable_message()

    @alert.deleter
    def alert(self):
        self.__undeletable_message()
