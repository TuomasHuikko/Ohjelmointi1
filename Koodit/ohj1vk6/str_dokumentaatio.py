"""
COMP.CS.100 "str_dokumentaatio" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def capitalize_initial_letters(name):
    """
    Muuntaa annetun merkkijonon muotoon, jossa sanojen ensimmäiset kirjaimet
    ovat isolla ja muut pienellä, erottimena toimii välilyönti.
    Esim. "drIVING cAR" = "Driving Car"

    :param name: Merkkijono, joka muunnetaan esimerkin muotoon
    :type name: str
    :return: Uusi muunnettu nimi esimerkin muodossa ks. esimerkki
    :rtype: str
    """

    new_name = name.title()
    return new_name

def main():

    print(capitalize_initial_letters("drIVING cAR"))

if __name__ == "__main__":
    main()
