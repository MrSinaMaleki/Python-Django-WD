import datetime


class Person:
    ids_list = list()

    def __init__(self, name, id_num, fathers_name, birth_date):
        self.__name = name

        self.__id_num = None
        self.set_id_num(value=id_num)

        self.__fathers_name = fathers_name
        self.__birth_date = birth_date
        self.age = self.cal_age(birth_date)

    @staticmethod
    def cal_age(value):
        birth_date_obj = datetime.datetime.strptime(value, "%Y-%m-%d").date()
        delta = datetime.date.today() - birth_date_obj
        age = delta.days // 365
        return age

    @classmethod
    def validate_id(cls, value):
        if value in cls.ids_list:
            return False
        else:
            cls.ids_list.append(value)
            return True

    @property
    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    @property
    def get_id_num(self):
        return self.__id_num

    def set_id_num(self, value):
        assert self.validate_id(value), "Tekrari!"
        self.__id_num = value

    @property
    def get_fathers_name(self):
        return self.__fathers_name

    def set_fathers_name(self, value):
        self.__fathers_name = value

    @property
    def get_birth_date(self):
        return self.__birth_date

    def set_birth_date(self, value):
        self.__birth_date = value


class Emp(Person):
    emp_ids = list()

    def __init__(self, name, id_num, fathers_name, birth_date, salary, emp_id):
        super().__init__(name, id_num, fathers_name, birth_date)

        self.__salary = None
        self.set_salary(value=salary)

        self.__emp_id = None
        self.set_emp_id(value=emp_id)

    @property
    def get_salary(self):
        return self.__salary

    def set_salary(self, value):
        if value < 0 and isinstance(value, (int, float)):
            raise "salary is no valid!!"
        else:
            self.__salary = value

    @property
    def get_emp_id(self):
        return self.__emp_id

    def set_emp_id(self, value):
        if value in self.emp_ids:
            raise "emp_id Tekrari!"
        else:
            self.emp_ids.append(value)
            self.__emp_id = value
            return True


class Lecture:
    def __init__(self, name, lec_id, start):
        self.__name = name
        self.__lec_id = lec_id
        self.__start = start

    @property
    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    @property
    def get_lec_id(self):
        return self.__lec_id

    def set_lec_id(self, value):
        self.__lec_id = value

    @property
    def get_start(self):
        return self.__start

    def set_start(self, value):
        self.__start = value


first_class = Lecture("Math", 12, "1:00")
second_class = Lecture("Science", 13, "2:00")


class Teacher(Emp):
    def __init__(self, name, id_num, fathers_name, birth_date, salary, emp_id, *classes_list):
        super().__init__(name, id_num, fathers_name, birth_date, salary, emp_id)
        self.classes_list = classes_list


first_teach = Teacher("Reza", 12, "Ali", "1990-04-15", 1200, 10, first_class, second_class)
second_teach = Teacher("Amir", 15, "Hassan", "1910-04-15", 1200, 100, first_class, second_class)

print(first_teach)
