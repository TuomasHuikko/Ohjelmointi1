"""
COMP.CS.100 "montako_löytyy" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def input_to_list(number_of_integers):
    """
    Adds the values added by the user to a list and returns it
    :param(number_of_integers) = the number of integers the user wants to add
    """

    number_list = []
    print("Enter" ,number_of_integers, "numbers:")
    for number in range(0, number_of_integers):
        number_list.append(int(input()))

    return number_list

def main():

    number_of_integers = int(input("How many numbers do you want to process: "))
    list_of_numbers = input_to_list(number_of_integers)
    searched_number = int(input("Enter the number to be searched: "))
    count_searched_number = list_of_numbers.count(searched_number)

    if count_searched_number == 0:
        print(f"{searched_number} is not among the numbers you have entered.")

    else:
        print(f"{searched_number} shows up {count_searched_number} "
        f"times among the numbers you have entered.")




if __name__ == "__main__":
        main()