import os


class Inventory:
    products = list()

    def __init__(self, products_list):

        self.products_list = products_list
        for p in products_list:
            self.products.append(
                {"name": p.name, "price": p.price, "quantity": p.quantity if p.quantity > 0 else "Not available"})

    @staticmethod
    def add_product(name, price, quantity):
        Product(name=name, price=price, quantity=quantity)

    @staticmethod
    def update_product(name, price):
        for p in Inventory.products:
            if p.get("name") == name:
                p["price"] = price
                return f"The {name} has been added successfully updated to {price}"
            else:
                return "Couldn't find the product!!!"

    @staticmethod
    def delete_product(name):
        invent_len = len(Inventory.products)
        if invent_len > 0:
            for p in range(invent_len):
                if Inventory.products[p]['name'] == name:
                    del Inventory.products[p]
                    return f"The {name} has been added successfully been deleted"
                else:
                    return "Couldn't find the product"
        else:
            return "You don't have any products!"

    @classmethod
    def read_inventory(cls):
        for p in cls.products:
            return f"name : {p.get('name')} quantity : {p.get('quantity')}, price : {p.get('price')}$"

    @classmethod
    def sell(cls, name):
        for p in cls.products:
            if p.get("name") == name:
                new_q = p["quantity"] - 1
                p["quantity"] = new_q if new_q > 0 else "Not available"
                return f"The {name} has been added successfully sold."
            else:
                return "Couldn't find the product!!!"

    @staticmethod
    def update_quantity_product(name, quantity):
        for p in Inventory.products:
            if p.get("name") == name:
                p["quantity"] = quantity
                return f"The {name} has been added successfully updated to {quantity} quantity"
            else:
                return "Couldn't find the product!!!"

    @classmethod
    def show_info(cls, name):
        if len(cls.products) > 0:
            for p in cls.products:
                if name == p.get("name"):
                    return f"name : {p.get('name')} quantity : {p.get('quantity')}, price : {p.get('price')}$"
                else:
                    return "Couldn't find the item. "
        else:
            return "No products to search in!"

    @staticmethod
    def clear():
        os.system('cls' if os.name.lower() == 'nt' else 'clear')


class Product:
    all_products_created = []

    def __init__(self, name, price, quantity):
        self.name = name

        assert self.validate(price), "Please enter a valid price. "
        self._price = price

        assert self.validate(quantity), "Please enter a valid price. "
        self._quantity = quantity

        self.__class__.all_products_created.append(self)

    @classmethod
    def from_string(cls, input_name, input_price, input_quantity):
        return cls(name=input_name, price=input_price, quantity=input_quantity)

    @classmethod
    def from_file(cls):
        # file = open("test.txt", "r")
        pass

    @staticmethod
    def validate(input_price):
        if str(input_price).isnumeric() and int(input_price) >= 0:
            return True

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        assert self.validate(input_price=new_price), "Please enter a valid price. "
        self._price = new_price

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, new_value):
        assert self.validate(input_price=new_value), "Please enter a valid quantity. "
        self._quantity = new_value

    # def sell(self):
    #     self.quantity -= 1

    def restock(self, new_q):
        self.quantity = new_q

    def display_info(self):
        return f"name:{self.name} quantity:{self.quantity}, price:{self.price}"


# pro_num1 = Product(name="Phone", price=200, quantity=2)
# pro_num2 = Product(name="Laptop", price=1200, quantity=0)
# pro_num3 = Product(name="earphones", price=270, quantity=5)
# pro_num4 = Product(name="MacBook", price=2400, quantity=1)
# pro_num1.quantity = 5

# my_inventory.add_product()

# print(my_inventory.products[0][1].name)


# name_input = input("Please enter the name of the product. ")
# price_input = int(input("Please enter the price of the product. "))
# quantity_input = int(input("Please enter the quantity of the product. "))
# Inventory.add_product(name=name_input, price=price_input, quantity=quantity_input)


# my_inventory = Inventory(products_list=Product.all_products_created)
# my_inventory.update_product(name="Phone", price=250)
# my_inventory.delete_product(name="earphones")
# print(my_inventory.products)


file = open(file="test.txt", mode="r")
content = file.readlines()
content_str = ""
for word in content:
    content_str += word
content_list = content_str.split(" ")
str_list = list(filter(None, content_list))
# print(str_list)
# print(len(content_list))
if len(str_list):
    i = 0
    while i < len(str_list):
        # print(f"Item created{i / 3}")
        Product(name=str_list[i][5:], price=int(str_list[i + 1][6:]), quantity=int(str_list[i + 2][9:]))
        i += 1
        # print(i)
        i += 1
        # print(i)
        i += 1
        # print(i)
Inventory(products_list=Product.all_products_created)


def menu(user_inp):
    if user_inp == '0':
        file = open("test.txt", "w")
        for p in Inventory.products:
            for k, v in p.items():
                file.writelines(f"{k}:{v} ")
        file.close()
        print(Inventory.products)
        exit()

    if user_inp == "1":
        name_input = input("Please enter the name of the product. ")
        price_input = int(input("Please enter the price of the product. "))
        quantity_input = int(input("Please enter the quantity of the product. "))
        # my_product = Product(name=name_input, price=price_input, quantity=quantity_input)
        Product.all_products_created = []
        Product(name=name_input, price=price_input, quantity=quantity_input)
        Inventory(products_list=Product.all_products_created)
        Inventory.clear()
        print(f"The {name_input} has been added successfully")

    if user_inp == "2":
        name_input = input("Please enter the name of the product you want to update. ")
        price_input = int(input("Please enter the price of the product you want to update. "))
        Inventory.clear()
        print(Inventory.update_product(name=name_input, price=price_input))

    if user_inp == "3":
        name_input = input("Please enter the name of the product you want to delete. ")
        Inventory.clear()
        print(Inventory.delete_product(name=name_input))

    if user_inp == "4":
        Inventory.clear()
        # Inventory(products_list=Product.all_products_created)
        # print(Inventory.read_inventory())
        print(Inventory.products)

    if user_inp == "5":
        name_input = input("Please enter the name of the product you want to buy. ")
        Inventory.sell(name=name_input)

    if user_inp == "6":
        name_input = input("Please enter the name of the product you want to update. ")
        quantity_input = int(input("Please enter the price of the product you want to update. "))
        Inventory.clear()
        print(Inventory.update_quantity_product(name=name_input, quantity=quantity_input))

    if user_inp == "7":
        name_input = input("Please enter the name of the product you want to see info of. ")
        print(Inventory.show_info(name=name_input))


while True:
    user_input = input("""Please select one of the options.                
    0-> exit
    1-> add a product
    2-> modify a product
    3-> delete a product
    4-> Show all of the products
    5-> Sell
    6-> Change the quantity of a product
    7-> Show info
    """)
    menu(user_input)
