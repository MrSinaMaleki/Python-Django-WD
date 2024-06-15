def safe(callback):
    def _(*args, **kwargs):
        while True:
            try:
                res = callback(*args, **kwargs)
            except (Exception, KeyboardInterrupt) as e:
                print(e)
                continue

            return res

    return _


class Shape:
    def __init__(self, name, color):
        assert self.validator_str(name), "Name can't contain a number!"
        self.name = name
        assert self.validator_str(color), "Color can't contain a number!"
        self.color = color

    @staticmethod
    def validator_str(input_value):
        if input_value.isalpha() and len(input_value) < 100:
            return True

    @staticmethod
    def validator_float(input_value):
        if float(input_value) > 0:
            return True

    def display_name(self):
        return f"The name of this shape is {self.name}"

    def display_color(self):
        return f"The color of this shape is {self.color}"


# @safe
# def get_shape():
#     name_input = input("name: ")
#     color_input = input("color: ")
#     my_shape = Shape(name=name_input, color=color_input)
#     return my_shape
#
#
# get_shape()

class Rectangle(Shape):
    def __init__(self, name, color, length, width):
        super().__init__(name=name, color=color)

        assert self.validator_float(length), "Negative length is not allowed! \n please try again! "
        self.length = float(length)

        assert self.validator_float(width), "Negative width is not allowed! \n please try again!"
        self.width = float(width)

    def perimeter(self):
        return f"perimeter: {2 * (self.length + self.width)}"

    def area(self):
        return f"area: {self.length * self.width}"


# @safe
# def get_rec_shape():
#     # name_input = input("name: ")
#     name_input = "Rec"
#     # color_input = input("color: ")
#     color_input = "Blue"
#     # length_input = input("length: ")
#     length_input = 12
#     # width_input = input("width: ")
#     width_input = 2
#     my_rec = Rectangle(name=name_input, color=color_input, length=length_input, width=width_input)
#
#     print(my_rec.perimeter(), my_rec.area(), sep="\n")
#     return my_rec
#
#
# get_rec_shape()

class Triangle(Shape):
    def __init__(self, name, color, a, b, c, height):
        super().__init__(name=name, color=color)

        assert self.validator_float(a), "Negative number is not allowed!(a) \n please try again! "
        self.a = float(a)
        assert self.validator_float(b), "Negative number is not allowed!(b) \n please try again!"
        self.b = float(b)
        assert self.validator_float(c), "Negative number is not allowed!(c) \n please try again!"
        self.c = float(c)
        assert self.tri_validator(a=self.a, b=self.b,
                                  c=self.c), "These numbers can't form a triangle \n please try again!"

        assert self.validator_float(height), "Negative number is not allowed!(c) \n please try again!"
        self.height = float(height)

    @staticmethod
    def tri_validator(a, b, c):
        if (a < b + c) and (b < a + c) and (c < a + b):
            return True

    def perimeter(self):
        return f"perimeter: {self.a + self.b + self.c}"

    def area(self):
        # https://khoshamoz.ir/index.php/post5453
        s = (self.a + self.b + self.c) / 2
        return f"area: {pow((s * ((s - self.a) + (s - self.b) + (s - self.c))), .5)}"


@safe
def get_tri_shape():
    name_input = input("name: ")
    # name_input = "Rec"

    color_input = input("color: ")
    # color_input = "Blue"

    a_input = input("a: ")
    # a_input = 3

    b_input = input("b: ")
    # b_input = 4

    c_input = input("c: ")
    # c_input = 5

    height_input = input("height: ")
    # height_input = 12

    my_tri = Triangle(name=name_input, color=color_input, a=a_input, b=b_input, c=c_input, height=height_input)

    print(my_tri.perimeter(), my_tri.area(), sep="\n")
    return my_tri


get_tri_shape()
