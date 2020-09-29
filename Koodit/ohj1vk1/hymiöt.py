"""
COMP.CS.100 "hymiöt" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def main():
    mieliala = input("How do you feel? (1-10) ")
    numero = int(mieliala)

    if numero > 0 and numero <11:
        if numero > 7 and numero <10:
            print("A suitable smiley would be :-)")
        elif numero >=4 and numero <=7:
            print("A suitable smiley would be :-|")
        elif numero ==1:
            print("A suitable smiley would be :'(")
        elif numero ==10:
            print("A suitable smiley would be :-D")
        else:
            print("A suitable smiley would be :-(")
    else:
        print("Bad input!")



if __name__ == "__main__":
        main()