class A:
    def __init__(self, x) -> None:

        self.attr = x

    @property
    def attr(self):
        print('getter call')
        return self.__attr

    @attr.setter
    def attr(self, value):
        print('setter call')
        assert isinstance(value, str), "---"
        self.__attr = value

    def show(self):
        print(self.__attr)


obj = A(x="12")
obj.show()
# print(obj._A__attr)
