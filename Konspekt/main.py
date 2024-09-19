from datetime import datetime

date_string = "2023.03.14"

datetime_object = datetime.strptime(date_string, "%Y.%m.%d")
print(datetime_object)

