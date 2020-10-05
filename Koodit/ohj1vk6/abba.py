"""
COMP.CS.100 "abba" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def count_abbas(word):
    """
    Laskee kuinka monta kertaa "abba" esiintyy annetussa sanassa.
    :param word: Annettu sana.
    :type word: str
    :return: Kuinka monta kertaa "abba" esiintyy sanassa.
    :rtype: int
    """

    index = 0
    abba_counter = 0
    for text in range(0, len(word)):
        character = word[index]

        if character == "a":
            possible_abba = word[index:index+4]
            if possible_abba == "abba":
                abba_counter += 1


        index += 1

    return abba_counter


def main():

    print(count_abbas("abbabbabba"))
    print(count_abbas("barbapapa"))
    print(count_abbas("aba"))

if __name__ == "__main__":
    main()