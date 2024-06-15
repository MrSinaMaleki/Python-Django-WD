class Backpack:

    def __init__(self):

        self._items = []

    @property
    def items(self):
        print("Calling the getter")
        return self._items

    @items.setter
    def items(self, new_value):
        print("Calling the setter")
        self._items = new_value if isinstance(new_value, list) else print("The backpack doesn't have enough capacity.")


my_back_pack = Backpack()
print(my_back_pack.items)

my_back_pack.items = ["Pen", "books"]
print(my_back_pack.items)
