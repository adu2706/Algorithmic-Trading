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


######Recipe 4: Modifiying datetime objects

from datetime import datetime

dt1 = datetime.now()
print(dt1)

dt2 = dt1.replace(year=2003, month=6, day=27)
print(f'A timestamp from 27th June 2003: {dt2}')

dt3 = datetime(year=2003,
               month=6,
               day=27,
               hour=dt1.hour,
               minute=dt1.minute,
               second=dt1.second,
               microsecond=dt1.microsecond,
               tzinfo=dt1.tzinfo)
print(f'A timestamp from 27th June 2003: {dt3}')

print(dt2 == dt3)


###### Recipe 6: Creating a datetime object from a string

from datetime import datetime

now_str = '04-06-2025 23:19:53 +05:30'
now = datetime.strptime(now_str, "%d-%m-%Y %H:%M:%S %z")
print(now)
print(type(now))

##### now = datetime.strptime(now_str, "%d-%m-%Y")  ####error you have to write "%H:%M:%S %z" (hour minute and timezone also ) format is wrong here

####### The datetime Object and time zones

from datetime import datetime

now_tz_naive = datetime.now()    # timezone naive datetime object
print(now_tz_naive)

print(now_tz_naive.tzinfo)

now_tz_aware = datetime.now().astimezone() #Timezone aware datetime object
print(now_tz_aware)
print(now_tz_aware.tzinfo)

new_tz_aware = now_tz_naive.replace(tzinfo=now_tz_aware.tzinfo)
print(new_tz_aware)
print(new_tz_aware.tzinfo)

new_tz_navie = new_tz_aware.replace(tzinfo=None)
print(new_tz_navie)
print(new_tz_navie.tzinfo)


######Recipe 8 : Creating a Pandas.Dataframe object

from datetime import datetime
import pandas

time_series_data = [
    {
        'date' : datetime(2003, 11, 13, 0, 0),
        'open' : 71.8075,
        'high' : 71.845,
        'low' : 71.7775,
        'close' : 71.7925,
        'volume' : 219512
    },
    {
        'date' : datetime(2003, 11, 13, 0, 20),
        'open' : 71.8075,
        'high' : 71.845,
        'low' : 71.7775,
        'close' : 71.7925,
        'volume' : 219512
    },
    {
        'date' : datetime(2003, 11, 13, 0, 30),
        'open' : 71.8075,
        'high' : 71.845,
        'low' : 71.7775,
        'close' : 71.7925,
        'volume' : 219512
    },
    {
        'date' : datetime(2003, 11, 13, 1, 0),
        'open' : 71.8075,
        'high' : 71.845,
        'low' : 71.7775,
        'close' : 71.7925,
        'volume' : 219512
    },
    {
        'date' : datetime(2003, 11, 13, 1, 10),
        'open' : 71.8077,
        'high' : 71.8459,
        'low' : 71.77715,
        'close' : 71.79235,
        'volume' : 119582
    },
    {
        'date' : datetime(2003, 11, 13, 1, 20),
        'open' : 71.8072,
        'high' : 71.8458,
        'low' : 71.7745,
        'close' : 71.725,
        'volume' : 229532
    },
    {
        'date' : datetime(2003, 11, 13, 1, 30),
        'open' : 71.805,
        'high' : 71.85,
        'low' : 71.7735,
        'close' : 71.7125,
        'volume' : 819912
    },
    {
        'date' : datetime(2003, 11, 13, 2, 0),
        'open' : 71.8175,
        'high' : 71.8995,
        'low' : 71.75,
        'close' : 71.225,
        'volume' : 239512
    },
    {
        'date' : datetime(2003, 11, 13, 2, 10),
        'open' : 71.5,
        'high' : 71.8115,
        'low' : 71.9775,
        'close' : 71.79925,
        'volume' : 119512
    },
    {
        'date' : datetime(2003, 11, 13, 2, 20),
        'open' : 71.4775,
        'high' : 71.695,
        'low' : 71.6795,
        'close' : 71.725,
        'volume' : 129512
    }
]


df = pandas.DataFrame(time_series_data)
print(df)

print(df.columns.tolist())

print(pandas.DataFrame(time_series_data,
                       columns = ['close', 'date', 'open', 'high', 'low', 'volume']))

####### print(pandas.DataFrame(time_series_data, index=range(10,20))) #changing indexing from 0-9 to 10-19

df.rename(columns={'date': 'timestamp'}, inplace = True)
print(df)

print(df.reindex(columns=[
    'volume',
    'close',
    'timestamp',
    'high',
    'open',
    'low'
]))

print(df[::-1])

print(df['close'])

print(df.iloc[0])

print(df.iloc[:2, :2])

print(df.iloc[:, 4])


#######Recipe 10: Dataframe Manipulation: applying, sorting, iteration and concatenating

import pandas

print(df)

df['timestamp'] = df['timestamp'].apply(
    lambda x: x.strftime("%d-%m-%Y %H:%M:%S")
)

print(df)

print(df.sort_values(by='close', ascending = True))

print(df.sort_values(by='open', ascending=False))

for i,row in df.iterrows():
    avg = (row['open'] + row['close'] + row['high'] + row['low'])/4
    print(f'INDEX: {i} | Average: {avg}')

for value in df.iloc[0]:
    print(value)


df_new = pandas.DataFrame([
    {
        'timestamp' : datetime(2000, 6, 27, 1, 0),
        'open' : 72.8072,
        'high' : 72.8458,
        'low' : 72.7745,
        'close' : 72.725,
        'volume' : 389292
    },
    {
        'timestamp' : datetime(2000, 6, 27, 1, 30),
        'open' : 72.805,
        'high' : 72.85,
        'low' : 72.7735,
        'close' : 72.7225,
        'volume' : 1012093
    },
    {
        'timestamp' : datetime(2000, 6, 27, 2, 0),
        'open' : 72.8175,
        'high' : 72.8995,
        'low' : 72.75,
        'close' : 72.225,
        'volume' : 183280
    },
    {
        'timestamp' : datetime(2000, 6, 27, 2, 30),
        'open' : 72.5,
        'high' : 72.8065,
        'low' : 72.9775,
        'close' : 72.79925,
        'volume' : 823838
    },
    {
        'timestamp' : datetime(2000, 6, 27, 3, 0),
        'open' : 72.4775,
        'high' : 72.695,
        'low' : 72.672395,
        'close' : 72.7335,
        'volume' : 292992
    }
])

print(df_new)

print(pandas.concat([df, df_new]).reset_index(drop=True))
