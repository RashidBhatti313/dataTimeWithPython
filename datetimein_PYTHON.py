import datetime
n = datetime.datetime.now()
print("current date and time")
print(n.strftime("%Y-%m-%d %H:%M:%S"))


import calendar
y = int(input("Input the year: "))
m = int(input("Input the month: "))
print(calendar.month(y, m))
