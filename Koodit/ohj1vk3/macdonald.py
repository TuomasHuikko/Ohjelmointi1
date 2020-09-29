"""
COMP.CS.100 "macdonald" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def print_verse(animal, sound):
    """prints the verse"""

    """param: animal, animal of choice"""
    """param: sound, sound the animal makes"""
    print("Old MACDONALD had a farm")
    print("E-I-E-I-O")
    print(f"And on his farm he had a {animal}")
    print("E-I-E-I-O")
    print(f"With a {sound} {sound} here")
    print(f"And a {sound} {sound} there")
    print(f"Here a {sound}, there a {sound}")
    print(f"Everywhere a {sound} {sound}")
    print("Old MacDonald had a farm")
    print("E-I-E-I-O")
    print()

def main():

    print_verse("cow", "moo")
    print_verse("pig", "oink")
    print_verse("duck", "quack")
    print_verse("horse", "neigh")
    print_verse("lamb", "baa")


if __name__ == "__main__":
    main()
