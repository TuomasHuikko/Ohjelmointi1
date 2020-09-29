"""
COMP.CS.100 "kivi_paperi_sakset" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def main():

    rpsplayer1 = input("Player 1, enter your choice (R/P/S): ")
    rpsplayer2 = input("Player 2, enter your choice (R/P/S): ")
    rps = str(rpsplayer1)
    rps2 = str(rpsplayer2)
    rock = "R"
    paper = "P"
    scissors = "S"

    if rps == rock and rps2 == scissors \
    or rps == scissors and rps2 == paper \
    or rps == paper and rps2 == rock:
        print("Player 1 won!")

    elif rps2 == rock and rps == scissors \
        or rps2 == scissors and rps == paper \
        or rps2 == paper and rps == rock:
            print("Player 2 won!")
    elif rps == rock and rps2 == rock \
        or rps == scissors and rps2 == scissors \
        or rps == paper and rps2 == paper:
            print("It's a tie!")
    else:
        print("Bad input!")


if __name__ == "__main__":
        main()