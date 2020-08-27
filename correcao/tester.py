import argparse
import os
import numpy as np
import pandas as pd

from importlib import import_module
from gabarito import read_and_tokenize as correct_read_and_tokenizer
from gabarito import bayes_theorem as correct_bayes_theorem


def main(path_answers, texts_path):
    correct_texts = correct_read_and_tokenizer(texts_path=texts_path)

    files = [file for file in os.listdir(path_answers) if file not in ['__init__.py', '__pycache__']]

    text_indices = np.arange(5).tolist()
    words = ['pandemic', 'populist', 'coronavirus']
    index = pd.MultiIndex.from_product([text_indices, words], names=['text', 'word'])

    own_entry = pd.DataFrame(index=index, columns=[f.split('.')[0] + '_correct' for f in files])
    same_entry = pd.DataFrame(index=index, columns=[f.split('.')[0] + '_correct' for f in files])

    for file in files:
        name = file.split('.')[0]

        module_object = import_module('agrupado.%s' % name, package='agrupado')
        read_and_tokenize = getattr(module_object, 'read_and_tokenize')
        bayes_theorem = getattr(module_object, 'bayes_theorem')

        student_texts = read_and_tokenize(texts_path)

        for word in words:
            for text_index in text_indices:
                own_entry.loc[(text_index, word)][name + '_correct'] = \
                    round(bayes_theorem(student_texts, a=word, b=text_index), 6) == \
                    round(correct_bayes_theorem(student_texts, a=word, b=text_index), 6)

                same_entry.loc[(text_index, word)][name + '_correct'] = \
                    round(bayes_theorem(correct_texts, a=word, b=text_index), 6) == \
                    round(correct_bayes_theorem(correct_texts, a=word, b=text_index), 6)

    print(own_entry)
    print(same_entry)

    # exporta para csv, para facilitar a visualização (caso não caiba no console)
    # own_entry.to_csv('propria_entrada.csv', index=True)
    # same_entry.to_csv('mesma_entrada.csv', index=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Código utilizado para testar as diversas implementações dos alunos.'
    )

    parser.add_argument(
        '--texts-path', action='store', required=True,
        help='Caminho para onde os .txts estão armazenados.'
    )

    args = parser.parse_args()
    main(path_answers='agrupado', texts_path=args.texts_path)
