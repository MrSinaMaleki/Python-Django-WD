import jdatetime
from hijri_converter import Gregorian
import os

YEAR_MONTH = {
    1: "January",
    2: "Feb",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

# Lookout for FEB!!!
MONTH_DAY = {
    "January": 31,
    "Feb": 29,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 31,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31

}


# print(MONTH_DAY[YEAR_MONTH[9]])

class Date:
    def __init__(self, year, month, day):
        assert self.year_validation(year_input=year), \
            f"Please enter a valid year! {year} should be positive and it should be a number. "

        assert self.month_validation(month_input=month), \
            f"Please enter a valid month! {month} should be positive and it should be a number between 12 and 1.  "

        assert self.day_validation(day_input=day), \
            f"Please enter a valid day! {day} should be positive and it should be a number. "

        assert self.is_valid_date(day, month), \
            f"{YEAR_MONTH[int(month)]} only has {MONTH_DAY[YEAR_MONTH[int(month)]]} days! But you entered {day} days."

        self.year = int(year)
        self.month = int(month)
        self.day = int(day)

    @classmethod
    def from_string(cls, user_input_date):
        date_list = user_input_date.split("-")
        return cls(day=date_list[0], month=date_list[1], year=date_list[2])

    @staticmethod
    def year_validation(year_input):
        if year_input.isnumeric() and int(year_input) > 0:
            return True

    @staticmethod
    def month_validation(month_input):
        if month_input.isnumeric() and (12 >= int(month_input) > 0):
            return True

    @staticmethod
    def day_validation(day_input):
        if day_input.isnumeric() and (31 >= int(day_input) > 0):
            return True

    @staticmethod
    def is_valid_date(day, month):
        if (MONTH_DAY[YEAR_MONTH[int(month)]]) >= int(day):
            return True

    def to_shamsi(self):
        # https://pypi.org/project/jdatetime/
        jalili_date = jdatetime.datetime.fromgregorian(day=self.day, month=self.month, year=self.year)
        return str(jalili_date)[:10]

    def to_ghamari(self):
        # https://pypi.org/project/hijri-converter/
        gregorian_date = Gregorian(self.year, self.month, self.day).to_hijri()
        return gregorian_date

    def __str__(self):
        return f"({user_date.day}th of {YEAR_MONTH[user_date.month]}, {user_date.year})"


def safe(callback):
    def _(*args, **kwargs):
        while True:
            try:
                res = callback(*args, **kwargs)
            except (Exception, KeyboardInterrupt) as e:
                print(f"Error: Try again !\n")
                print(e)
                continue

            return res

    return _


@safe
def get_date_object():
    date_input = input("Please enter a date in the following format (dd-mm-year). ")
    return Date.from_string(user_input_date=date_input)


user_date = get_date_object()

print("Your date was successfully validated!",
      f"({user_date.day}th of {YEAR_MONTH[user_date.month]}, {user_date.year})")


def clear():
    os.system('cls' if os.name.lower() == 'nt' else 'clear')


def menu(user_inp):
    if user_inp == '0':
        exit()
    elif user_inp == '1':
        clear()
        print("Here is the date in Shamsi: ")
        return user_date.to_shamsi()
    elif user_inp == '2':
        clear()
        return user_date.to_ghamari()
    elif user_inp == "3":
        clear()
        return user_date


while True:
    user_input = input("""Please select one of the options.                
    0-> exit.
    1-> Show date in Shamsi.
    2-> Show date in Ghamari.
    3-> Show the date again.
    """)
    print(menu(user_input))
