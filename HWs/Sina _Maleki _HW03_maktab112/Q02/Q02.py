# # Sina Maleki - Python 112 - Group Number 1 -CW3
# # ////////////////////////// Q number 2 //////////////////////////
import os

carts = [
    # {
    #     "name": "Sina",
    #     "products": [
    #         {
    #             "product_name": "laptop",
    #             "price": 1000,
    #             "quantity": 1
    #         }, {
    #             "product_name": "phone",
    #             "price": 450,
    #             "quantity": 2
    #         }
    #     ],
    #     "final_price": 1900
    # }, {
    #     "product_name": "reza",
    #     "products": [],
    #     "final_price": 0
    # }
]


def clear():
    if os.name == 'posix':
        os.system('clear')
    # else screen will be cleared for windows
    else:
        os.system('cls')


def menu():
    print("Please select one of the options.")
    print(" 1)Show all cart.")
    print(" 2)add a product to your card.")
    print(" 3)Deleting a product from your card.")
    print(" 0)exit")


def add_product():
    user_name = input("Please enter your name. ")
    p_name = input("Please enter the name of your product. ")
    p_price = int(input("Please enter the price of your product. "))
    p_quantity = int(input("Please enter your product's quantity. "))

    for cart in carts:
        if cart.get("name") == user_name:
            print("I know you!")
            cart["products"].append({
                "product_name": p_name,
                "price": p_price,
                "quantity": p_quantity
            }, )
            cart["final_price"] += p_price * p_quantity
            print(f"Here is your cart: ")
            print(cart)
            break

    else:
        carts.append({
            "name": user_name, "products": [
                {
                    "product_name": p_name,
                    "price": p_price,
                    "quantity": p_quantity
                }
            ],
            "final_price": p_price * p_quantity

        })
        print(carts[-1])


def del_product(user_name, product_name):
    for cart in carts:
        if cart.get("name") == user_name:
            for product in cart["products"]:
                if product["product_name"] == product_name:
                    cart["products"].remove(product)
                    cart["final_price"] -= product["price"] * product["quantity"]
                    print(f"{product_name} is deleted from you cart. ")
                    return
            print(f"I could not find {product_name} in your card. ")
            return
            # Why not break ?!
    print(f"{user_name} doesn't exist!")


flag = True
while flag:
    menu()
    menu_input = input()
    if menu_input == "1":
        clear()
        # print("There aren't any carts" if len(carts) < 1 else print(f"Here is all of the carts: \n {carts}"))
        if len(carts) < 1:
            print("There are not any carts")
        else:
            print(f"Here is all of the carts: \n {carts}")

    elif menu_input == "2":
        try:
            add_product()

        except ValueError:
            print("Value Error! Try again.")

        except TypeError:
            print("Type error")

    elif menu_input == "3":
        user_name = str(input("Please enter your name. "))
        product_name = str(input("Please enter your product's name. "))
        del_product(user_name=user_name, product_name=product_name)

    elif menu_input == "0":
        flag = False
        clear()
        print("Bye Bye :)")
