########Recipe 1: Creating datetime Objects
from datetime import datetime

dt1 = datetime.now()
print(f'Apporach #1: {dt1}')

print(f'Year: {dt1.year}')
print(f'Month: {dt1.month}')
print(f'Day: {dt1.day}')
print(f'Hours: {dt1.hour}')
print(f'Minutes: {dt1.minute}')
print(f'Seconds: {dt1.second}')
print(f'Microseconds: {dt1.microsecond}')
print(f'Timezone: {dt1.tzinfo}')


dt2 = datetime(year=2027, month=12, day=1)
print(f'Approach #2 : {dt2}')

print(f'Year: {dt2.year}')
print(f'Month: {dt2.month}')
print(f'Day: {dt2.day}')
print(f'Hours: {dt2.hour}')
print(f'Minutes: {dt2.minute}')
print(f'Seconds: {dt2.second}')
print(f'Microseconds: {dt2.microsecond}')
print(f'Timezone: {dt2.tzinfo}')


print(f'Date: {dt1.date()}')
print(f'Type: {type(dt1.date())}')

######## Recipe 2: Crating timedelta objects

from datetime import timedelta

td1  = timedelta(days=5)
print(f'Time difference: {td1}')

td2 = timedelta(days=3)
print(f'Time difference: {td2}')

print(f'Addition: {td1} + {td2} = {td1 + td2}')
print(f'Substraction: {td1} - {td2} = {td1 - td2}')
print(f'Multiplication: {td1} * 2.5 = {td1 * 2.5}')

td3 = timedelta(hours=50, minutes=59, seconds=60)
print(f'Time difference: {td3}')
print(f'Total seconds in 2 days, 3:00:00: {td3.total_seconds()}')


#########Recipe 3: Operations on datetime objects

from datetime import date, datetime, timedelta

date_today = date.today()
print(f"Today's Date: {date_today}")

date_5days_later = date_today + timedelta(days=5)
print(f'Date 5 days later: {date_5days_later}')

date_5days_ago = date_today - timedelta(days=5)
print(f'Date 5 days ago: {date_5days_ago}')

print(date_5days_later > date_5days_ago)
print(date_5days_later < date_5days_ago)
print(date_5days_later > date_today > date_5days_ago)

current_timestamp = datetime.now()
time_now = current_timestamp.time()
print(f'Time now: {time_now}')

time_5minutes_later = (current_timestamp + timedelta(minutes=5)).time()
print(f'Time 5 minutes later: {time_5minutes_later}')

time_5minutes_ago = (current_timestamp - timedelta(minutes=5)).time()
print(f'Time 5 minutes ago: {time_5minutes_ago}')

print(time_5minutes_later > time_5minutes_ago)
print(time_5minutes_later < time_5minutes_ago)
print(time_5minutes_later > time_now > time_5minutes_ago)