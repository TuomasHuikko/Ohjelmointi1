"""
COMP.CS.100 "kolmio" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""
from math import sqrt

def area(first_side, second_side, third_side):
    """calculates triangle area with given lenghts of sides"""

    perimeter = float((first_side + second_side + third_side)/2)
    area = sqrt(perimeter* (perimeter - first_side)*
             (perimeter - second_side)*(perimeter - third_side))

    return area

def main():

    first_side = float(input("Enter the length of the first side: "))
    second_side = float(input("Enter the length of the second side: "))
    third_side = float(input("Enter the length of the third side: "))


    print(f"The triangle's area is "
          f"{area(first_side, second_side, third_side):.1f}")


if __name__ == "__main__":
    main()
