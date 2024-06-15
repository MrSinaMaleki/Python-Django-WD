import time

# print(time.time())  # number
# print(time.ctime())  # real date in str
# print(time.gmtime().tm_mday)  # time.struct that you can do methods on
# print(time.mktime(time.gmtime()))  # gets the date instance and transform it to seconds

YEAR_MONTH = {
    1: "Jan",
    2: "Feb",
    3: "Mar",
    4: "Apr",
    5: "May",
    6: "June",
    7: "Jul",
    8: "Aug",
    9: "Sep",
    10: "Oct",
    11: "Nov",
    12: "Dec",
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12

}


# https://www.geeksforgeeks.org/python-time-module/
class BirthDay:
    def __init__(self, hour, day, mount, year):

        assert self.year_validator(year=year), \
            "Please enter a valid year! (It should be a positive number, and not in the past!)"
        self.year = year

        assert self.month_validator(month=mount), \
            "Please enter a valid month! (It should be between 1 and 12 / It should be a positive number)"
        self.month = int(mount)

        assert self.day_validator(day=day), \
            "Please enter a valid day! (It should be between 0 and 31 / It should be a positive number)"
        self.day = int(day)

        assert self.hour_validator(hour=hour), \
            "Please enter a valid hour! (It should be between 0 and 24/ It should be a positive number)"
        self.hour = int(hour)

        assert self.master_validater(), "You can't be born in the future:)"

    @staticmethod
    def present_obj():
        return time.gmtime()  # time.struct that you can do methods on

    @staticmethod
    def present_in_seconds():
        return time.time()  # number

    # What's the difference between this and assert?!
    @staticmethod
    def year_validator(year):
        if year.isnumeric() and 0 < int(year):
            return True

    @staticmethod
    def month_validator(month):
        if month.isnumeric() and (0 < int(month) <= 12):
            return True

    @staticmethod
    def day_validator(day):
        if day.isnumeric() and (0 < int(day) <= 31):
            return True

    @staticmethod
    def hour_validator(hour):
        if hour.isnumeric() and (0 <= int(hour) <= 24):
            return True

    def user_input_time_to_seconds(self, flag):
        time_in_seconds = time.strptime(
            f"{self.day} {YEAR_MONTH[self.month]} {self.year if flag else self.present_obj().tm_year} {self.hour if flag else self.present_obj().tm_hour}:00:00",
            "%d %b %Y %H:%M:%S")
        return time.mktime(time_in_seconds)  # number

    def master_validater(self):
        if self.user_input_time_to_seconds(flag=True) < self.present_in_seconds():
            return True

    def age(self):
        test_v = time.ctime(self.present_in_seconds() - self.user_input_time_to_seconds(flag=True))
        # print(test_v)
        date_list = test_v.split(" ")
        # https://www.bahesab.ir/time/age/ wrong
        # https://www.calculator.net/age-calculator.html
        print(
            f"you are: {(int(date_list[-1])) - 1970} years, {YEAR_MONTH[date_list[1]] - 1} mounts ,{int(date_list[-3]) - 3} days and {int((date_list[3])[:2])} hours old.")

    def days_to_bd(self):
        days = int((self.user_input_time_to_seconds(flag=False) - self.present_in_seconds()) / 86400)
        hours = int((self.user_input_time_to_seconds(flag=True) - self.present_in_seconds()) / 3600)

        if days < 0 and hours < 0:
            print(f"{days + 365} days and {days + 24} hours remains to your birthday :)")
        else:
            print(f"{days} days and {days} hours remains to your birthday :)")


year_input = input("Please enter year of birth. ")
month_input = input("Please enter month of birth. ")
day_input = input("Please enter day of birth. ")
hour_input = input("Please enter hour of birth. ")
# year_input = "2003"
# month_input = "2"
# day_input = "2"
# hour_input = "1"

my_bd = BirthDay(year=year_input, mount=month_input, day=day_input, hour=hour_input)
my_bd.age()
my_bd.days_to_bd()
