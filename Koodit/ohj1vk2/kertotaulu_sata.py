"""
COMP.CS.100 "kertotaulu_sata" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def main():



    toisto_kerrat = 1
    numero = int(input("Choose a number: "))
    lasku = True

    while lasku:


        tulo = (numero * toisto_kerrat)
        print(toisto_kerrat, "*" ,numero, "=", tulo)
        toisto_kerrat += 1

        if tulo > 100:
            lasku = False






if __name__ == "__main__":
        main()