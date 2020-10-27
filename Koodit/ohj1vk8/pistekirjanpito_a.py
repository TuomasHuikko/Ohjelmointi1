"""
COMP.CS.100 "pistekirjanpito_a" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def main():

    file_name = input("Enter the name of the score file: ")
    score_file = open(file_name, mode="r")

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