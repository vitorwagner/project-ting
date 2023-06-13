import sys
# https://stackoverflow.com/a/5899544
# https://www.w3schools.com/python/ref_string_splitlines.asp


def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        print('Formato inválido', file=sys.stderr)
    try:
        with open(path_file, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
