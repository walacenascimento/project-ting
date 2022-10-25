def exists_word(word, instance):
    """Aqui irá sua implementação"""
    occurrences = []
    result = []
    for index in range(instance.__len__()):
        file_sentences = instance.search(index)["linhas_do_arquivo"]
        for index_sentence in range(len(file_sentences)):
            if word.lower() in file_sentences[index_sentence].lower():
                occurrences.append({"linha": index_sentence + 1})
        if len(occurrences) > 0:
            partial_result = {
              "palavra": word,
              "arquivo": instance.search(index)["nome_do_arquivo"],
              "ocorrencias": occurrences,
            }

            result.append(partial_result)

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
