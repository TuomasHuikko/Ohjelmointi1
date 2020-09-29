"""
COMP.CS.100 "listan_indeksointi_a" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def main():

    positive_numbers = []

    print("Give 5 numbers: ")

    for number in range(0, 5):
        number = int(input("Next number: "))

        if number > 0:
            positive_numbers.append(number)

    print("The numbers you entered that were greater than zero were:")
    for number in positive_numbers:
        print(number)




if __name__ == "__main__":
    main()