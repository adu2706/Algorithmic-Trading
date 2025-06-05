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
