"""
# Ohjelmointi - product class excercise
# Tekijä: Irina Kudinova
# Opiskelijanumero: 154058513
"""
#from dis import UNKNOWN


class Product:
    """
    This class defines a simplified product for sale in a store.
    """

    def __init__(self, name, price):
        self.__name = name
        self.__price = price
        self.__sale = 0.00

    def printout(self):

        print(self.__name)
        print(f"  price: {self.__price:.2f}")
        print(f"  sale%: {self.__sale:.2f}")


    def get_price(self):

        if self.__sale > 0:
            return (self.__price -(self.__price * self.__sale/100))
        else:
            return self.__price

    def set_sale(self, percent):

        self.__sale = percent
        return self.__sale


def main():

    test_products = {
        "milk":   1.00,
        "sushi": 12.95,
        "pizza": 4.95,
    }

    for product_name in test_products:
        print("=" * 20)
        print(f"TESTING: {product_name}")
        print("=" * 20)

        prod = Product(product_name, test_products[product_name])

        prod.printout()
        print(f"Normal price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale(0)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale(5)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale(15)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)

        prod.set_sale(75)
        prod.printout()
        print(f"Sale price: {prod.get_price():.2f}")

        print("-" * 20)


if __name__ == "__main__":
    main()
