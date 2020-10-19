"""
COMP.CS.100 "tanssipelit_1" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.70, "grasshopper": 13.25,
    "sushi": 19.90, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def payload(key):
    """
    Returns the value of key in dict: dict[key].

    :param key: Name of key in dict.
    :type key: str
    :return: Value of said key in dict.
    :rtype: float
    """

    return PRICES[key]

def main():

    for price in sorted(PRICES, key=payload):
        print(f"{price} {PRICES[price]:.2f}")

if __name__ == "__main__":
    main()
