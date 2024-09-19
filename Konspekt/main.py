from datetime import datetime 

now = datetime.now()

iso_calendar = now.isocalendar()
print(f'ISO year : {iso_calendar[0]}, ISO Week: {iso_calendar[1]}, ISO week day: {iso_calendar[2]}')

