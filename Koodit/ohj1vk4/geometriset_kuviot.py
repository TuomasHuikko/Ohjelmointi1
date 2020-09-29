"""
COMP.CS.100 "geometriset_kuviot" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

from math import pi

def menu():
    """
    This function prints a menu for user to select which
    geometric shape to use in calculations.
    """

    while True:
        answer = input("Enter the pattern's first letter, q stops this (s/r/q): ")
        if answer == "s":
            square_input()
            pass
            # replace this comment and "pass" above with your function calls
            # dealing with square.
        elif answer == "r":
            rectangle_input()
            pass
            # replace this comment and "pass" above with your function calls
            # dealing with rectangle.
        elif answer == "q":
            return
        elif answer == "c":
            circle_input()
            pass
        else:
            print("Incorrect entry, try again!")

        print()  # Empty row for the sake of readability

def square_input():
    """asks the user the needed properties of the square"""


    square_side = float(input("Enter the length of the square's side: "))
    square_validity(square_side)

def square_calculator(square_side):
    """calculates the circumference and area of the square and prints it
    on screen"""

    square_circumference = 4 * square_side
    square_area = square_side ** 2
    print(f"The total circumference is{square_circumference: 0.2f}")
    print(f"The surface area is{square_area: 0.2f}")

def square_validity(square_side):
    """Determines if input is valid"""

    if square_side <= 0:
        square_valid = False
    else:
        square_valid = True

    if square_valid:
        square_calculator(square_side)
    else:
        square_input()

def rectangle_input():
    """asks the user the needed properties of the rectangle"""
    loop = True
    loop_2 = True
    while loop:

        rectangle_side = float(input("Enter the length of the rectangle's side 1: "))
        if rectangle_validity(rectangle_side):
                loop = False
    while loop_2:
        rectangle_side_2 = float(input("Enter the length of the rectangle's side 2: "))
        if rectangle_validity(rectangle_side_2):
                loop_2 = False

    rectangle_calculator(rectangle_side, rectangle_side_2)

def rectangle_validity(rectangle_side):
    """Determines if input is valid"""

    if rectangle_side <= 0:
        rectangle_valid = False
    else:
        rectangle_valid = True

    if rectangle_valid:
         return rectangle_valid

def rectangle_calculator(rectangle_side, rectangle_side_2):
    """calculates the circumference and area of the rectangle and prints it
    on screen"""

    rectangle_circumference = (2 * rectangle_side + 2 * rectangle_side_2)
    rectangle_area = (rectangle_side * rectangle_side_2)
    print(f"The total circumference is{rectangle_circumference: 0.2f}")
    print(f"The surface area is{rectangle_area: 0.2f}")

def circle_input():
    """asks the user the needed properties of the circle(radius)"""

    radius = float(input("Enter the circle's radius: "))
    circle_validity(radius)

def circle_validity(radius):
    """Determines if the input is valid"""

    if radius <= 0:
            circle_valid = False
    else:
            circle_valid = True

    if circle_valid:
            circle_calculator(radius)
    else:
            circle_input()

def circle_calculator(radius):
    """calculates the circumference and area of the circle and prints it
    on screen"""

    circle_circumference = 2 * pi * radius
    circle_area = pi * radius ** 2
    print(f"The total circumference is{circle_circumference: 0.2f}")
    print(f"The surface area is{circle_area: 0.2f}")

def main():
    menu()
    print("Goodbye!")


if __name__ == "__main__":
        main()