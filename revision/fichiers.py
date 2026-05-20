import json


def get_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)

    return donnees
