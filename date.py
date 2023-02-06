# Importing modules at the beginning of the program is a good practice

import datetime

date_today = datetime.date.today() # current date
print(date_today)

time_today = datetime.datetime.now()
print(time_today.strftime("%H:%M:%s")) # current time

