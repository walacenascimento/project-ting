import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if not path_file.endswith(".txt"):
        return sys.stderr.write("Formato inválido\n")
    try:
        with open(path_file) as file:
            text = file.read()
            text_list = text.split("\n")

        return text_list
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
