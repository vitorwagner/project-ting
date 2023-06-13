# https://realpython.com/python-enumerate/#using-pythons-enumerate
# https://stackoverflow.com/a/319435


def exists_word(word, instance):
    output = list()
    for i in range(0, len(instance)):
        occurences = list()
        for line_index, line\
                in enumerate(instance.search(i)['linhas_do_arquivo']):
            if word.casefold() in line.casefold():
                occurences.append({'linha': line_index + 1})
        if occurences:
            output.append({
                'palavra': word,
                'arquivo': instance.search(i)['nome_do_arquivo'],
                'ocorrencias': occurences,
            })

    return output


def search_by_word(word, instance):
    output = list()
    for i in range(0, len(instance)):
        occurences = list()
        for line_index, line\
                in enumerate(instance.search(i)['linhas_do_arquivo']):
            if word.casefold() in line.casefold():
                occurences.append({'linha': line_index + 1,
                                   'conteudo': line})
        if occurences:
            output.append({
                'palavra': word,
                'arquivo': instance.search(i)['nome_do_arquivo'],
                'ocorrencias': occurences,
            })

    return output
