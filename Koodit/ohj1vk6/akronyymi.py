"""
COMP.CS.100 "akronyymi" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def create_an_acronym(name):
    """
    Muuttaa annetun nimen akronyymiksi eli lyhenteeksi esimerkki:
    "central intelligence agency" = "CIA"

    :param name: Annettu nimi esimerkin muodossa
    :type name: str
    :return: Akronyymi eli lyhenne annetusta nimestä ks. esimerkki.
    :rtype: str
    """

    names = name.split(" ")
    total_name_number = len(names)
    final_name = ""
    for index in range(0, total_name_number):
        name_part = names[index]
        new_name_part = name_part[0]
        new_name_part = new_name_part.upper()
        final_name += new_name_part

    return final_name

def main():

    print(create_an_acronym("central intelligence agency"))


if __name__ == "__main__":
    main()