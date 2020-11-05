"""
COMP.CS.100 "tuote_luokka" tehtävä.
Tekijä: Tuomas Huikko
Opiskelijanumero: H291873
"""

class Product:
    """
    This class defines a simplified product for sale in a store.
    """
    def __init__(self, name, price, sale_percentage=0.00):
        """
        Initializes the product with starting values/parameters name and price.

        :param name: Name of the product.
        :type name: str
        :param price: Price of the product.
        :type price: float
        """

        self.__name = name
        self.__price = price
        self.__sale = sale_percentage

    def get_price(self):
        """
        Returns the price of product after sale. If there is no sale returns
            original value instead.

        :return: Price of product.
        :rtype: float
        """

        return (1-(self.__sale/100))*self.__price

    def set_sale_percentage(self, sale_percentage):
        """
        Sets a new sale percentage for the product.

        :param sale_percentage: Sale percentage of product.
        :type sale_percentage: float
        :return: Price after sale.
        :rtype: float
        """

        self.__sale = sale_percentage

    def printout(self):
        """
        Prints out the name, price and sale percentage of a product.
        """

        print(self.__name)
        print(f"  price: {self.__price:.2f}")
        print(f"  sale%: {self.__sale:.2f}")


def main():
    ################################################################
    #                                                              #
    #  You can use the main-function to test your Product class.   #
    #  The automatic tests will not use the main you submitted.    #
    #                                                              #
    #  Voit käyttää main-funktiota Product-luokkasi testaamiseen.  #
    #  Automaattiset testit eivät käytä palauttamaasi mainia.      #
    #                                                              #
    ################################################################

    test_products = {
        "milk":   1.00,
        "sushi": 12.95,
    }

    for product_name in test_products:
        print("=" * 20)
        print(f"TESTING: {product_name}")
        print("=" * 20)

        prod = Product(product_name, test_products[product_name])

        prod.printout()
        print(f"Normal price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(10.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale_percentage(25.0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)


if __name__ == "__main__":
    main()