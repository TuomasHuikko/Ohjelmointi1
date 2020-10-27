"""
COMP.CS.100 "pistekirjanpito_b" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def main():

    file_name = input("Enter the name of the score file: ")

    try:
        score_file = open(file_name, mode="r")
    except OSError:
        print("There was an error in reading the file.")
        return

    for file_line in score_file:
        file_line = list(file_line.split())
        index = 0
        for string in range(0, len(file_line)):
            if file_line[index] == " ":
                del file_line[index]
            elif len(file_line) < 2:
                print("There was an erroneous line in the file:")
                print(file_line[0])
                return
            elif not file_line[-1].isdigit():
                print("There was an erroneous score in the file:")
                print(file_line[-1])
                return
            index += 1


    game_scores = {}

    for file_line in score_file:
        file_line = file_line.split()

        if file_line[0] in game_scores:
            game_scores[file_line[0]] += int(file_line[1])

        else:
            game_scores[file_line[0]] = file_line[1]
        game_scores[file_line[0]] = int(game_scores[file_line[0]])

    print("Contestant score:")

    for player in sorted(game_scores):
        print(player, game_scores[player])


if __name__ == "__main__":
    main()