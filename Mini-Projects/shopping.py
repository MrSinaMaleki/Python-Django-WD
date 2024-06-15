class CashRegister:
    PRODUCTS = (
        {"name": "Pizza", "price": 10.34},
        {"name": "Sandwich", "price": 6.99},
        {"name": "Hamburger", "price": 12.25})

    def __init__(self, name, items_dict):
        self.name = name
        self.items_dict = items_dict
        self.items_dict = {"food": (), "price": 0}


cu_sina = CashRegister("Eli", ("Pizza", "Sandvich", "Hamburger"))
print(cu_sina)