class Shop:
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = 0

    def describe_shop(self):
        print(f"Shop name: {self.shop_name}")
        print(f"Store type: {self.store_type}")

    def open_shop(self):
        print(f"The online shop '{self.shop_name}' is now open!")

    def set_number_of_units(self, number):
        self.number_of_units = number

    def increment_number_of_units(self, amount):
        self.number_of_units += amount


class Discount(Shop):
    def __init__(self, shop_name, store_type, discount_products=None):
        super().__init__(shop_name, store_type)
        if discount_products is None:
            discount_products = []
        self.discount_products = discount_products

    def get_discounts_products(self):
        print("Discounted products:")
        for product in self.discount_products:
            print(f" - {product}")
