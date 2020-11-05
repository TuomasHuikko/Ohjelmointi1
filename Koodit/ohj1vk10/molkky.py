"""
COMP.CS.100 "mölkky" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

class Player:
    """
    Defines the player of the game "mölkky", with attributes: name and points.
    """

    def __init__(self, name, points=0, number_of_throws=0, points_above_0=0):
        """
        Initializes the class Player with attributes name, points, number
            of throws and points that are above zero.

        :param name: Name of the player.
        :type name: str
        :param points: Points/score of the player.
        :type points: int
        :param number_of_throws: Number of throws the player has thrown.
        :type number_of_throws: int
        :param points_above_0: Players points that are above 0.
        :type points_above_0: int
        """

        self.__name = name
        self.__points = points
        self.__throws = number_of_throws
        self.__above_0 = points_above_0


    def get_name(self):
        """
        Returns the name of the player to use in the main function.
        :return: Name of player.
        :rtype: str
        """

        return self.__name


    def add_points(self, points_to_add):
        """
        Adds points_to_add to the players score. Also examines if the players
            score is more than 50 which results in penalty points (-> 25 p).
            Prints a warning if the players points exceed 39 and are lower
            than 50.

        :param points_to_add: The points to add in the players score.
        :type points_to_add: int
        """

        if points_to_add > 0:
            self.__points += points_to_add
            self.__above_0 += 1
        self.__throws += 1

        if self.__points > 50:
            self.__points = 25
            print(f"{self.__name} gets penalty points!")
        elif 40 <= self.__points <= 49:
            print(f"{self.__name} needs only {50-self.__points} points. "
                  f"It's better to avoid knocking down the pins "
                  f"with higher points.")

    def get_points(self):
        """
        Returns the score/point situation of the player.
        :return: Score of player.
        :rtype: int
        """

        return self.__points

    def has_won(self):
        """
        Returns true if the players points are equal to 50 and false if not.

        :return: If players points are =50 or not.
        :rtype: bool
        """

        if self.__points == 50:
            return True
        else:
            return False

    def calc_average(self):
        """
        Returns the average score per throw from the players' throws.

        :return: The average of all throws.
        :rtype: float
        """

        return self.__points/self.__throws

    def hit_percentage(self):
        """
        Calculates the hit percentage of the player.

        :return: Hit percentage.
        :rtype: float
        """

        if self.__above_0 == 0:
            return 0.0
        else:
            return (self.__above_0/self.__throws) * 100



def main():
    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!

    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:

        # if throw is an even number
        if throw % 2 == 0:
            in_turn = player1

        # else throw is an odd number
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))

        in_turn.add_points(pts)

        if pts > in_turn.calc_average():
            if not in_turn.get_points() == 25:
                print(f"Cheers {in_turn.get_name()}!")

        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(f"{player1.get_name()}: {player1.get_points()} p, "
              f"hit percentage {player1.hit_percentage():.1f}")
        print(f"{player2.get_name()}: {player2.get_points()} p, "
              f"hit percentage {player2.hit_percentage():.1f}")
        print("")

        throw += 1


if __name__ == "__main__":
    main()
