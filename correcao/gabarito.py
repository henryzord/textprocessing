import argparse  # talvez seja necessário instalar essa biblioteca: conda install argparse
import os
from nltk.tokenize import RegexpTokenizer  # talvez seja necessário instalar essa biblioteca: conda install nltk
from collections import Counter


def read_and_tokenize(texts_path: str) -> list:
    """
    Carrega os textos .txt para a memória. Separa cada texto em uma lista de listas, onde cada sublista é uma lista de
    palavras, e cada super-lista um texto.

    As palavras nas sublistas já estão em caixa baixa, e já tiveram a pontuação removida.

    :type texts_path: str
    :param texts_path: Caminho para onde os os textos estão.
    :rtype: list
    :return: Uma lista de listas.
    """

    filenames = sorted(os.listdir(texts_path))

    texts = []

    for filename in filenames:
        with open(os.path.join(texts_path, filename), 'r') as fileobj:
            texts += [''.join(fileobj.readlines())]

    rg = RegexpTokenizer(r'\w+')

    tokenized = []

    for text in texts:
        text = text.lower()
        text = rg.tokenize(text)
        tokenized += [text]

    return tokenized


def bayes_theorem(texts: list, a: str, b: int = None):
    """
    Implementa o Teorema de Bayes:

    P(A|B) = P(B|A)P(A)/P(B)

    :param texts: uma lista de listas, onde cada sublista é uma lista de
    palavras, e cada super-lista um texto.
    :param a: A palavra a qual quer-se verificar a probabilidade de ocorrer.
    :param b: Opcional - Se não for provido, retornará P(A); do contrário, retorna P(A|B)
    :return: P(A) se b = None, P(A|B) se b não for None
    """

    """
    Faz uma contagem de palavras: dicionário para cada texto. Cada chave do dicionário é uma palavra, e cada valor
    o número de vezes que a palavra aconteceu naquele texto.
    """
    counts = list(map(Counter, texts))

    count_a = 0
    n_words = 0

    for count in counts:
        n_words += sum([v for k, v in count.items()])
        count_a += count[a]
    pa = count_a / n_words

    if b is None:
        return pa
    else:
        # probabilidade de uma palavra (qualquer uma) pertencer ao texto B
        pb = sum([v for k, v in counts[b].items()]) / sum([sum([v for k, v in count.items()]) for count in counts])

        # probabilidade do texto B conter palavras = A dada todas as contagens da palavra A em todos os textos
        pb_a = counts[b][a] / count_a

        # retorna probabilidade da palavra A ocorrer no texto B
        return (pb_a * pa) / pb


def main(texts_path):
    """
    Função principal.

    :type texts_path: str
    :param texts_path: Caminho para onde os os textos estão.
    """

    texts = read_and_tokenize(texts_path)

    words = ['coronavirus', 'populist', 'pandemic']

    for word in words:
        for i in range(5):
            print('P(%s | text=%d):\t' % (word, i), round(bayes_theorem(texts, a=word, b=i), 6))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Gabarito do trabalho final de Programação em Python.'
    )

    parser.add_argument(
        '--texts-path', action='store', required=True,
        help='Caminho para onde os .txts estão armazenados.'
    )

    args = parser.parse_args()
    main(texts_path=args.texts_path)
