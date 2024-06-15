class ShoppingCart:
    items_list = []

    def __init__(self, name):
        self.name = name
        ShoppingCart.items_list.append({"name": name, "cart": []})

    def add_item(self, name, count):
        for i in range(count):
            self.items_list[0]["cart"].append(f"{name}")

    def remove_items(self, name):
        self.items_list[0]["cart"].remove(name)


my_shopping_cart = ShoppingCart(name='Sina')
my_shopping_cart.add_item("Jeans", 3)
my_shopping_cart.add_item("Sweatshirt", 1)
print(my_shopping_cart.items_list)

my_shopping_cart.remove_items("Jeans")
print(my_shopping_cart.items_list)

