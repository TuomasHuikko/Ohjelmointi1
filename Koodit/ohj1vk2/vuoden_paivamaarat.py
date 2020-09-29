"""
COMP.CS.100 "vuoden_paivamaarat" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def main():

    main_loop = True

    while main_loop:

        month = 1
        day = 1
        for month in range(1, 13):

            if month == 4 or month == 6 or month == 9 or month == 11:
                for day in range(1, 31):
                    print(f"{day}.{month}.")
                    day += 1
            elif month == 2:
                for day in range(1, 30):
                    print(f"{day}.{month}.")
                    day += 1
            else:
                for day in range(1, 32):
                    print(f"{day}.{month}.")
                    day += 1

        month += 1
        if month > 12:
            main_loop = False





if __name__ == "__main__":
        main()