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
    occurrences = exists_word(word, instance)

    for index in range(instance.__len__()):
        for data in occurrences:
            sentences = data["ocorrencias"]
            if data["arquivo"] == instance.search(index)["nome_do_arquivo"]:
                for sentence in sentences:
                    inst_data = instance.search(index)["linhas_do_arquivo"]
                    sentence_txt = inst_data[sentence["linha"] - 1]
                    sentence["conteudo"] = sentence_txt

    return occurrences
