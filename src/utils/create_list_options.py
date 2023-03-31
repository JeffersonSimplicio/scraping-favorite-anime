from src.strategy.list_stratege import Strategys


def to_string(n):
    return str(n)


def create_list_options():
    result = list(map(to_string, range(1, len(Strategys) + 1)))

    result.insert(0, "")

    return result
