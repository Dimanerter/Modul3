from datetime import datetime 

seventh_day_2019 = datetime(year = 2019, month=1, day=7, hour=14)
seventh_day_2020 = datetime(year = 2020, month=1, day=7, hour=14)

difference = seventh_day_2020 - seventh_day_2019
print(difference)
print(difference.total_seconds())
