"""
COMP.CS.100 "vaihtorahat" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

def main():


    purchase_input = input("Purchase price: ")
    purchase = int(purchase_input)
    paid_input = input("Paid amount of money: ")
    paid = int(paid_input)

    change = (paid-purchase)
    change10 = (change//10)
    change10_left = (change % 10)
    change5 = (change10_left//5)
    change5_left = (change10_left % 5)
    change2 = (change5_left//2)
    change2_left = (change5_left % 2)
    change1 = (change2_left//1)


    if change > 0:
        print("Offer change:")
    if change10 > 0 and paid > purchase:
        print(change10, "ten-euro notes")
    if change5 > 0 and paid > purchase:
        print(change5, "five-euro notes")
    if change2 > 0 and paid > purchase:
        print(change2, "two-euro coins")
    if change1 > 0 and paid > purchase:
        print(change1, "one-euro coins")
    if purchase >= paid and purchase != 0 and paid != 0:
        print("No change")
    if purchase == 0 and paid == 0:
        print("")



if __name__ == "__main__":
        main()