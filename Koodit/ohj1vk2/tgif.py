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
        friday_counter = -2
        for month in range(1, 13):

            if month == 4 or month == 6 or month == 9 or month == 11:
                for day in range(1, 31):
                    day += 1
                    friday_counter += 1
                    fridays = (friday_counter % 7)

                    if fridays == 0:
                        print(f"{day}.{month}.")
            elif month == 2:
                for day in range(1, 29):
                    friday_counter += 1
                    day += 1
                    fridays = (friday_counter % 7)

                    if fridays == 0:
                        print(f"{day}.{month}.")

            else:

                for day in range(1, 32):
                    friday_counter += 1
                    day += 1
                    fridays = (friday_counter % 7)

                    if month == 7 and day == 32:
                        print(f"1.8.")
                    else:
                        if fridays == 0:
                            print(f"{day}.{month}.")





        month += 1
        if month > 12:
            main_loop = False




if __name__ == "__main__":
        main()