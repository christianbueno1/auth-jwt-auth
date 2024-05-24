from datetime import datetime, timedelta, timezone

# now = datetime.utcnow()

# use timezone-aware datetime objects, and always use UTC, assing timezone to now2
now = datetime.now(timezone.utc)
delta15min = timedelta(minutes=15)
expire = now + delta15min
print(f"now: {now}\ndelta15min: {delta15min}\nexpire: {expire}")
# print(f"now2: {now2}")