def readFile(path: str) -> str:
    data = open(path, 'r')
    code = data.read()
    data.close()
    return code
