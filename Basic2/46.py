import datetime

weekdays = {1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday",
            7: "Sunday"}

td=datetime.date.today()

day=td.isoweekday()

print("Today is :{}".format(weekdays[day]))