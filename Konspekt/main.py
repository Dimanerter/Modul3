from datetime import datetime, timezone, timedelta

utc_time = datetime.now(timezone.utc)

eastern_time = utc_time.astimezone(timezone(timedelta(hours=-5)))
print(eastern_time)