from datetime import datetime

napoleon_burns_moscow = datetime(year=1812, month=9, day=14)

current_date = datetime.now()

days_since = current_date.toordinal() - napoleon_burns_moscow.toordinal()

print(days_since)



