"""
COMP.CS.100 "tulitikkupeli" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def main():

    print("Game of sticks")
    main_loop = True
    player_1_loop = True
    player_2_loop = True
    stick_number = 21

    while main_loop:


        while player_1_loop:

            player_1_input = int(
                input("Player 1 enter how many sticks to remove: "))

            if player_1_input >= 1 and player_1_input <= 3:
                stick_number -= player_1_input

                if stick_number <= 0:
                    main_loop = False
                    player_2_loop = False
                    print("Player 1 lost the game!")
                    break

                print(f"There are {stick_number} sticks left")
                break
            else:
                print("Must remove between 1-3 sticks!")
                continue

        while player_2_loop:

            player_2_input = int(
                input("Player 2 enter how many sticks to remove: "))

            if player_2_input >= 1 and player_2_input <= 3:
                stick_number  -= player_2_input

                if stick_number <= 0:
                    main_loop = False
                    print("Player 2 lost the game!")
                    break

                print(f"There are {stick_number} sticks left")
                break
            else:
                print("Must remove between 1-3 sticks!")
                continue


if __name__ == "__main__":
        main()
