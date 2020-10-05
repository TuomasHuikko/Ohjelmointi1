"""
COMP.CS.100 "nimet" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def reverse_name(name):
    """
    Kääntää annetun nimen muodosta "Sukunimi, Etunimi" muotoon
    "Etunimi Sukunimi".

    :param name: Annettu nimi muodossa "Sukunimi, Etunimi"
    :type name: str
    :return: Nimi muodossa "Etunimi Sukunimi"
    :rtype: str
    """
    
    name.strip()
    names = name.split(",")
    first_name = names[-1]
    first_name = first_name.strip()
    surname = names[0]
    surname = surname.strip()
    new_name = first_name + " " + surname
    new_name = new_name.strip()

    return new_name

def main():

    print(reverse_name("Techie, Teddy"))
    print(reverse_name("Scumble,    Arnold"))
    print(reverse_name("Fortunato,Frank"))
    print(reverse_name("von Grünbaumberger, Herbert"))

if __name__ == "__main__":
    main()