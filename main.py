from shop_module import Shop, Discount


store = Shop("ElectroShop", "Electronics")
print(store.shop_name)
print(store.store_type)
store.describe_shop()
store.open_shop()

print()


store1 = Shop("BookWorld", "Books")
store2 = Shop("StyleHub", "Clothing")
store3 = Shop("FreshMart", "Groceries")

store1.describe_shop()
store2.describe_shop()
store3.describe_shop()

print()


print(f"Default number of units in store: {store.number_of_units}")
store.number_of_units = 20
print(f"Updated number of units: {store.number_of_units}")

print()


store.set_number_of_units(35)
print(f"Number of units after setting: {store.number_of_units}")

store.increment_number_of_units(5)
print(f"Number of units after incrementing: {store.number_of_units}")

print()


store_discount = Discount("FashionSale", "Clothing", ["Jeans", "T-Shirts", "Sneakers"])
store_discount.get_discounts_products()
