from datetime import datetime 

now = datetime.now()

# Конвертация в формат ISO 8601
iso_format = now.isoformat()
print(iso_format)

iso_date_string = "2023-03-14T12:39:29.992996"

# Конвертация из ISO формата
date_from_iso = datetime.fromisoformat(iso_date_string)
print(date_from_iso)