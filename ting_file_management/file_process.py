import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    text_list = txt_importer(path_file)

    for index in range(instance.__len__()):
        if path_file == instance.search(index)["nome_do_arquivo"]:
            return None

    result = {
      "nome_do_arquivo": path_file,
      "qtd_linhas": len(text_list),
      "linhas_do_arquivo": text_list
    }

    instance.enqueue(result)

    return print(result)


def remove(instance):
    """Aqui irá sua implementação"""
    if not instance.__len__():
        print("Não há elementos")
    else:
        file = instance.dequeue()
        path_file = file["nome_do_arquivo"]
        return print(f"Arquivo {path_file} removido com sucesso")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        return print(instance.search(position))
    except IndexError:
        return sys.stderr.write("Posição inválida")
