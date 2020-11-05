"""
COMP.CS.100 "auto_luokkana" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

class Car:
    """
    Class Car: Implements a car that moves a certain distance and
    whose gas tank can be filled. The class defines what a car is:
    what information it contains and what operations can be
    carried out for it.
    """

    def __init__(self, tank_size, gas_consumption, gas=0.0, odometer=0.0):
        """
        Constructor, initializes the newly created object.

        :param tank_size: float, the size of this car's tank.
        :param gas_consumption: float, how much gas this car consumes
                   when it drives a 100 kilometers
        """

        self.__tank_volume = tank_size
        self.__consumption = gas_consumption
        self.__gas = gas
        self.__odometer = odometer


    def print_information(self):
        """
        Prints out the situation of the car regarding the gas and odometer.
        """

        print(f"The tank contains {self.__gas:.1f} liters of gas and the odometer"
              f" shows {self.__odometer:.1f} kilometers.")


    def fill(self, gas_to_fill):
        """
        Fills the tank up with the amount specified by gas_to_fill. Gas to fill
            cannot be negative and if it exceeds tank volume it goes to waste.

        :param gas_to_fill: The amount of gas to fill in the tank(liter).
        :type gas_to_fill: float
        """

        if (self.__gas+gas_to_fill) > self.__tank_volume:
            self.__gas = self.__tank_volume
        elif gas_to_fill < 0:
            print("You cannot remove gas from the tank")
        else:
            self.__gas += gas_to_fill


    def drive(self, distance_to_drive):
        """
        Adds the wanted distance to the odometer, "drives the car". Negative
            distance is not tolerated and stops distance when gas runs out.

        :param distance_to_drive: Wanted distance to drive.
        :type distance_to_drive: float
        """

        if distance_to_drive > 10 * self.__gas:
            self.__odometer += 10 * self.__gas
            self.__gas = 0.0
        elif distance_to_drive < 0:
            print("You cannot travel a negative distance")
        if 0 < distance_to_drive < 10 * self.__gas:
            self.__odometer += distance_to_drive
            self.__gas -= distance_to_drive/10


def main():
    tank_size = read_number("How much does the vehicle's gas tank hold?")
    gas_consumption = read_number("How many liters of gas does the car "
                                  "consume per hundred kilometers?")

    car = Car(tank_size, gas_consumption)

    while True:
        car.print_information()

        choice = input("1) Fill 2) Drive 3) Quit\n-> ")

        if choice == "1":
            to_fill = read_number("How many liters of gas to fill up?")
            car.fill(to_fill)

        elif choice == "2":
            distance = read_number("How many kilometers to drive?")
            car.drive(distance)

        elif choice == "3":
            print("Thank you and bye!")
            break


def read_number(prompt, error_message="Incorrect input!"):
    """
    This function is used to read input (float) from the user.

    :param prompt: str, prompt to be used when asking user input.
    :param error_message: str, what error message to print
        if the entered value is not a float.
    """

    while True:
        try:
            return float(input(prompt + " "))

        except ValueError:
            print(error_message)


if __name__ == "__main__":
    main()