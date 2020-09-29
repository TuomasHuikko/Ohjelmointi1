"""
COMP.CS.100 "onko_tylsaa_3" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def main():


    read_words = True

    while read_words:

        bored_input = str(input("Bored? (y/n) "))
        if bored_input == "y":
            read_words = False
            print("Well, let's stop this, then.")
            break

        invalid_input = True

        while invalid_input:

            if bored_input == "y":
                invalid_input = False
                print("Well, let's stop this, then.")
                read_words = False
            elif bored_input == "n":
                invalid_input = False
            else:
                print("Incorrect entry.")
                bored_input = input("Please retry: ")










if __name__ == "__main__":
        main()