"""
COMP.CS.100 "rubikinkuutio" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def performance_input():
    """Asks the user the time of each rubik's cube performance"""


    performance_list = []
    for number in range(1, 6):
        performance = float(input(f"Enter the time for performance {number}: "))
        performance_list.append(performance)
        number += 1
    return performance_list

def del_min_max(list):
    """
    Deletes the min and max value of a given list
    :param list = a list
    """

    new_list = sorted(list)
    del new_list[-1]
    del new_list[0]

    return new_list

def calc_average(list):
    """Calculates average of a list of numbers"""

    index = 0
    sum_of_list = 0
    for number in range(0, len(list)):
        sum_of_list += list[index]
        index += 1

    average = sum_of_list/len(list)
    return average

def main():

    performance_list = performance_input()
    new_performance_list = del_min_max(performance_list)
    competition_score = calc_average(new_performance_list)
    print(f"The official competition score is {competition_score:.2f} seconds.")


if __name__ == "__main__":
    main()