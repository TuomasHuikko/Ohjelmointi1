"""
COMP.CS.100 "onko_tylsaa_1" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def main():

    read_words = True

    while read_words:
        bored_input = input("Bored? (y/n) ")
        read_words = bored_input != "y"

    print("Well, let's stop this, then.")


if __name__ == "__main__":
        main()

