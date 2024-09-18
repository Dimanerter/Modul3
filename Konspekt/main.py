from datetime import datetime

now = datetime.now()

timestamp = datetime.timestamp(now)

print(timestamp)

timestamp = 1617183600
dt_object = datetime.fromtimestamp(timestamp)
print(dt_object)



