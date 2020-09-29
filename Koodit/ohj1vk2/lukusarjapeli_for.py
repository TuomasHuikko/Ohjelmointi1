"""
COMP.CS.100 "lukusarjapeli_for" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def main():


    numbers = int(input("How many numbers would you like to have? "))


    for main_loop in range(1, numbers +1):

        zip_counter = int(main_loop % 3)
        boing_counter = int(main_loop % 7)
        zip_boing_counter = int((main_loop % 3) + (main_loop % 7))

        if zip_boing_counter == 0:
            print("zip boing")
        elif zip_counter == 0:
            print("zip")
        elif boing_counter == 0:
            print("boing")
        elif zip_boing_counter and zip_counter == 0:
            print("zip boing")
        else:
            print(main_loop)

        main_loop += 1







if __name__ == "__main__":
        main()