class Oop:
    items_list = []

    def __new__(cls, *args, **kwargs):
        cls.items_list.append(args)
        cls.items_list.append(kwargs)
        return super().__new__(cls)


test = Oop("sina", {"last_name": "Maleki"})
print(test.items_list)
print(type(test))
