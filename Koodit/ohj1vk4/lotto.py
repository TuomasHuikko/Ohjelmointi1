"""
COMP.CS.100 "lotto" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

from math import factorial

def probability_counter(total_balls, drawn_balls):
    """
    Calculates the probability of winning in a lottery with
    given amount of total balls and the amount of balls drawn.
    Uses the equation n!/((n-p)!*p!) where n=total_balls and
    p=drawn_balls
     """

    number_of_possibilities = int(factorial(total_balls)/(factorial
    (total_balls - drawn_balls) * factorial(drawn_balls)))
    probability = (f"The probability of guessing all {drawn_balls} balls"
                   f" correctly is 1/{number_of_possibilities}")

    return probability

def invalid_input(total_balls, drawn_balls):
    """Determines if the given integers(number of balls) are valid"""

    validity = True
    if total_balls <= 0 or drawn_balls <= 0:
        print("The number of balls must be a positive number.")
        validity = False
    elif drawn_balls > total_balls:
        print("At most the total number of balls can be drawn.")
        validity = False

    return validity







def main():

    total_balls = int(input("Enter the total number of lottery balls: "))
    drawn_balls = int(input("Enter the number of the drawn balls: "))

    if invalid_input(total_balls, drawn_balls) != False:

        print(probability_counter(total_balls, drawn_balls))



if __name__ == "__main__":
        main()