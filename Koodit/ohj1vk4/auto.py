"""
COMP.CS.100 "auto" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""
from math import sqrt


def menu():
    """
    This is a text-based menu. You should ONLY TOUCH TODOs inside the menu.
    TODOs in the menu call functions that you have implemented and take care
    of the return values of the function calls.
    """

    tank_size = read_number("How much does the vehicle's gas tank hold? ")
    gas = tank_size  # Tank is full when we start
    gas_consumption = read_number("How many liters of gas does the car " +
                                  "consume per hundred kilometers? ")
    x = 0.0  # Current X coordinate of the car
    y = 0.0  # Current Y coordinate of the car

    while True:
        print("Coordinates x={:.1f}, y={:.1f}, "
              "the tank contains {:.1f} liters of gas.".format(x, y, gas))

        choice = input("1) Fill 2) Drive 3) Quit\n-> ")

        if choice == "1":
            to_fill = read_number("How many liters of gas to fill up? ")
            gas = fill(tank_size, to_fill, gas)

        elif choice == "2":
            new_x = read_number("x: ")
            new_y = read_number("y: ")
            gas, x, y = drive(x ,y, new_x, new_y, gas, gas_consumption)

        elif choice == "3":
            break

    print("Thank you and bye!")


def fill(tank_size, to_fill, gas):
    """
    This function has three parameters which are all FLOATs:
      (1) the size of the tank
      (2) the amount of gas that is requested to be filled in
      (3) the amount of gas in the tank currently

    The parameters have to be in this order.
    The function returns one FLOAT that is the amount of gas in the
    tank AFTER the filling up.

    The function does not print anything and does not ask for any
    input.
    """

    if to_fill < 0:
        print("You cannot remove gas from the tank")
    elif gas + to_fill >= tank_size:
        gas = tank_size
    else:
        gas = gas + to_fill

    return gas

def drive(x ,y, destination_x, destination_y, gas, consumption):
    """
    This function has six parameters. They are all floats.
      (1) The current x coordinate
      (2) The current y coordinate
      (3) The destination x coordinate
      (4) The destination y coordinate
      (5) The amount of gas in the tank currently
      (6) The consumption of gas per 100 km of the car

    The parameters have to be in this order.
    The function returns three floats:
      (1) The amount of gas in the tank AFTER the driving
      (2) The reached (new) x coordinate
      (3) The reached (new) y coordinate

    The return values have to be in this order.
    The function does not print anything and does not ask for any
    input.
    """

    # It might be useful to make one or two assisting functions
    # to help the implementation of this function.
    distance = calc_distance(x, y, destination_x, destination_y)
    gas_consumption = calc_gas_consumption(distance, consumption)

    if gas_consumption <= gas:
        gas = gas - gas_consumption
        new_x = destination_x
        new_y = destination_y
    else:
        ratio = gas / gas_consumption
        new_x = x + (ratio * (destination_x - x))
        new_y = y + (ratio * (destination_y - y))
        gas = 0
    return gas, new_x, new_y

      # Implement your own functions here. You are required to
      # implement at least two functions that take at least
      # one parameter and return at least one value.  The
      # functions have to be used somewhere in the program.

def calc_distance(x, y, destination_x, destination_y):
    """
    Calculates distance between two given points in 2d plane with parameters:
    x - x-coordinate of the first point
    y - y-coordinate of the first point
    destination_x - x-coordinate of the second point
    destination_y - y-coordinate of the second point
    """

    distance = sqrt((destination_x - x) ** 2 + (destination_y - y) ** 2) 
    return distance

def calc_gas_consumption(distance, consumption):
    """
    Calculates gas consumption for given distance
    with parameters:
    distance - Distance to drive
    consumption - Gas consumption per 100 kilometers
    """

    gas_consumption = consumption * distance * 0.01
    return gas_consumption


def read_number(prompt, error_message="Incorrect input!"):
    """
    DO NOT TOUCH THIS FUNCTION.
    This function reads input from the user.
    Also, don't worry if you don't understand it.
    """

    try:
        return float(input(prompt))

    except ValueError:
        print(error_message)
        return read_number(prompt, error_message)


def main():
    menu()


if __name__ == "__main__":
    main()