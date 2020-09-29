"""
COMP.CS.100 "arvosanojen_korvaus" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def convert_grades(list_of_integers):
    """
    Converts every integer that is > 0 and < 6 to 6 in list
    :param list_of_integers = a list of integers
    """

    index = 0
    for number in range(0, len(list_of_integers)):
        if list_of_integers[index] != 0:
            del list_of_integers[index]
            list_of_integers.insert(index, 6)
        index += 1

def main():

    grades = []
    convert_grades(grades)
    print(grades)  # Should print [0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0]


if __name__ == "__main__":
    main()
