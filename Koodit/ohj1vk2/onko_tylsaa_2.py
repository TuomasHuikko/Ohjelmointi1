"""
COMP.CS.100 "onko_tylsaa_2" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def main():

    invalid_input = True
    answer = input("Answer Y or N: ")

    while invalid_input:




        if answer == "y":
            invalid_input = False
        elif answer == "Y":
            invalid_input = False
        elif answer == "n":
            invalid_input = False
        elif answer == "N":
            invalid_input = False
        else:
            print("Incorrect entry.")
            answer = input("Please retry: ")


    print("You answered", answer)














if __name__ == "__main__":
        main()