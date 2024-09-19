from datetime import datetime 

now = datetime.now()

# Использование isoweekday() для получения дня недели

day_of_week = now.isoweekday()

print(f"Сьогодні: {day_of_week}")
