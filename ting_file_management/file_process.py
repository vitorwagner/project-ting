import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for i in range(0, len(instance)):
        if instance.search(i)['nome_do_arquivo'] == path_file:
            return None

    lines = txt_importer(path_file)
    output = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(lines),
        'linhas_do_arquivo': lines,
    }

    instance.enqueue(output)
    print(output, file=sys.stdout)


def remove(instance):
    try:
        removed = instance.dequeue()['nome_do_arquivo']
    except IndexError:
        print('Não há elementos', file=sys.stdout)
    else:
        print(f'Arquivo {removed} removido com sucesso', file=sys.stdout)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
