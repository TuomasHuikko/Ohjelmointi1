"""
COMP.CS.100 "hintalista" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.70, "grasshopper": 13.25,
    "sushi": 19.90, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def main():

    while True:
        product = str(input("Enter product name: "))
        product = product.strip()

        if product == "":
            print("Bye!")
            break
        elif product in PRICES:
            print(f"The price of {product} is{PRICES[product]: .2f} e")
            continue
        elif product not in PRICES:
            print(f"Error: {product} is unknown.")
            continue

if __name__ == "__main__":
    main()