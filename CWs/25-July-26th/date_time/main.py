from datetime import datetime, timedelta
from pytz import timezone
from pprint import pprint


class DateManipulator:
    @staticmethod
    def get_current_time():
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def calculate_difference(t1, t2):
        date1 = datetime.strptime(t1, '%Y-%m-%d %H:%M:%S')
        date2 = datetime.strptime(t2, '%Y-%m-%d %H:%M:%S')
        return abs(date2 - date1)

    @staticmethod
    def time_converter(t1):
        date1 = datetime.strptime(t1, '%Y-%m-%d')
        return date1

    @staticmethod
    def time_localizer(zone):
        str_time = datetime.now(timezone('UTC'))
        result = str_time.astimezone(timezone(zone))
        return result

    @staticmethod
    def time_traveler(days, date):
        date_obj = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        result = date_obj + timedelta(days=days)
        return result

    @staticmethod
    def get_weeks(year):
        weeks = []
        day_of_week = datetime(year, 1, 1).weekday()
        date_obj = datetime(year, 1, 1)
        if day_of_week == 0:
            while date_obj.year <= year:
                week = (date_obj.strftime('%Y-%m-%d'), (date_obj+timedelta(days=7)).strftime('%Y-%m-%d'))
                date_obj = date_obj + timedelta(days=7)
                weeks.append(week)

        elif day_of_week > 0:
            date_obj = datetime(year, 1, 1) + timedelta(days=7-day_of_week)
            while date_obj.year <= year:
                week = (date_obj.strftime('%Y-%m-%d'), (date_obj + timedelta(days=7)).strftime('%Y-%m-%d'))
                date_obj = date_obj + timedelta(days=7)
                weeks.append(week)

        return weeks

    @staticmethod
    def compare_dates(date1, date2):
        list_date = [date1, date2]
        return {'past': min(list_date).strftime('%Y-%m-%d'), 'future': max(list_date).strftime('%Y-%m-%d')}


# print(datetime.now().weekday())

obj = DateManipulator()
# print(obj.calculate_difference('2024-06-02 06:00:00', '2024-06-01 06:00:00'))
# print(obj.time_converter('2024-06-02'))
# print(obj.time_localizer('Asia/Tehran'))
# print(obj.time_traveler(-12, '2024-06-02 15:26:30'))
# print(datetime(2024, 1, 8).weekday())
# pprint(obj.get_weeks(2023))
print(obj.compare_dates(datetime(2025, 1, 1), datetime(2020, 2, 1)))
# my_list = [datetime(2023, 1, 1), datetime(2020, 2, 1)]
# print(max(my_list))
