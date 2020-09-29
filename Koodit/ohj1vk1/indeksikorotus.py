"""
COMP.CS.100 "indeksikorotus" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

opintotuki = input("Enter the amount of the study benefits: ")
opintotuki1 = float(opintotuki)
indeksikorotus = 1.0117
opintotuki_lopullinen = (opintotuki1 * indeksikorotus)
opintotuki_lopullinen2 = (opintotuki_lopullinen * indeksikorotus)

print("If the index raise is 1.17 percent, the study benefit,")
print("after a raise, would be", opintotuki_lopullinen, "euros")
print("and if there was another index raise, the study")
print("benefits would be as much as", opintotuki_lopullinen2, "euros")
