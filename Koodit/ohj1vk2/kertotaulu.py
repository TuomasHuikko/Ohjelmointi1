"""
COMP.CS.100 "kertotaulu" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def main():



    toisto_kerrat = 1
    numero = int(input("Choose a number: "))

    while toisto_kerrat <= 10:


        tulo = (numero * toisto_kerrat)
        print(toisto_kerrat, "*" ,numero, "=", tulo)
        toisto_kerrat += 1





if __name__ == "__main__":
        main()