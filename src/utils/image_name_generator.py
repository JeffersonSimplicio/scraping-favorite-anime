def image_name_generator(name: str) -> str:
    chars = '.,!?'
    path = name.strip().lower()
    path = path.replace(" ", "_").replace(":", "_").replace("/", "_")
    path = path.translate(str.maketrans('', '', chars))  # remove caracteres
    return path
