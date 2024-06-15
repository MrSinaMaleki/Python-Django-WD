import uuid
import random


class Library:
    def __init__(self, name, location, opening_hours):
        self.name = name
        self.location = location
        self.opening_hours = opening_hours

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        assert isinstance(new_name, str), "It should be a STR"
        self._name = new_name

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, new_location):
        assert isinstance(new_location, str), "It should be a STR"
        self._location = new_location

    @property
    def opening_hours(self):
        return self._opening_hours

    @opening_hours.setter
    def opening_hours(self, new_opening_hours):
        assert new_opening_hours.isnumeric(), "It should be a number"
        self._opening_hours = new_opening_hours


test = Library("IranCentralLib", "Tehran", "2")


# print(test._Library__name)
class Author:
    def __init__(self, name):
        self.name = name


auther_1 = Author("Amir")

auther_2 = Author("Reza")


class Category:
    list_of_categories = []
    ids = []

    def __init__(self, name):

        random_int = random.randint(1000, 9999)
        while random_int in self.ids:
            random_int = random.randint(1000, 9999)
        else:
            self.ids.append(random_int)
            self.name = name
            self.id = random_int

        # print(random_int)

        if name in self.list_of_categories:
            raise Exception("Tekrari")
        else:
            self.list_of_categories.append(name)
            self.category = name


cat1 = Category("si_fi")
cat2 = Category("Action")


class Book:
    all_books_dict = {}

    def __init__(self, name, page_count, price, category, authors):
        self.name = name
        self.page_count = page_count
        self.uniq_id = uuid.uuid1()
        self._price = price
        self._category = category
        # list_of_authors = ""
        # for item in authors:
        #     list_of_authors += f"{item.name}-"
        # print(list_of_authors)
        #
        # self.writers = list_of_authors
        self.authors = authors

        if self.name in self.__class__.all_books_dict.keys():
            _ = self.__class__.all_books_dict.get(name)
            _.append(self)

            self.__class__.all_books_dict.update({self.name: _})
        else:
            self.__class__.all_books_dict.update({self.name: [self]})

        print(self.__class__.all_books_dict)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        print("setter")
        self._price = self.price

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_price):
        pass


my_book = Book("b1", 100, 200, cat1, [auther_1, auther_2])
my_book5 = Book("b1", 100, 200, cat2, [auther_1])

my_book2 = Book("b2", 100, 200, cat2, [auther_1])
my_book3 = Book("b3", 100, 200, cat1, [auther_1])


# print(Book.all_books["b1"])


class Shelves:
    pages = 0
    shelf_number = 0

    def __init__(self):
        # https://realpython.com/inherit-python-list/
        # super().__init__(item for item in books)
        self.max_capacity = 200
        self.__class__.shelf_number += 1

    def add_book(self, *args):
        for book in args:
            self.pages += book.page_count
            if self.pages <= self.max_capacity:
                print(f"{self.shelf_number} -> {book._category.id}")
            else:
                raise Exception("You have Exceeded the max_capacity")

    def __len__(self):
        return self.pages


shelf1 = Shelves()
shelf1.add_book(my_book, my_book2)
print(len(shelf1))


class Librarian:
    def __init__(self):
        pass

    @classmethod
    def search_for_books(cls, input_name):
        book_instance_dict = Book.all_books_dict[input_name]
        # _ = list()
        # # name, page_count, price, category, authors
        # for book in Book.all_books_list:

        return f"*** name:{book_instance_dict.name} - page-count:{book_instance_dict.page_count} - price:{book_instance_dict.price} category:{book_instance_dict.category.name}({book_instance_dict.category.id}), authors:{[author.name for author in book_instance_dict.authors]})***"

    def retrieve_a_book(self):
        pass

    @staticmethod
    def add_category(name_of_cat):
        my_cat = Category(name_of_cat)
        return my_cat

    def book_replacement(self):
        pass


Librarian.add_category("action")
Librarian.add_category("test")
print(Librarian.search_for_books("b1"))
