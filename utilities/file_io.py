def read_file(file_name: str) -> str:
    with open(file_name, "r", encoding="utf-8") as fp:
        return fp.read()
