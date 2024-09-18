import datetime

date_part = datetime.date(2023, 12,14)
time_part = datetime.time(12,30,15)

combined_datetime = datetime.datetime.combine(date_part, time_part)

print(combined_datetime)