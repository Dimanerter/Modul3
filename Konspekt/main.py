from datetime import datetime

now = datetime.now()

formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)

formatted_date_only = now.strftime("%A, %d, %B %Y")
print(formatted_date_only)

formatted_time_only = now.strftime("%I:%M %p")
print(formatted_time_only)

formatted_date_only = now.strftime("%d.%m.%Y")
print(formatted_date_only)