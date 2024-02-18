import datetime
cur_date=datetime.datetime.now()
days= int(input())
new=cur_date-datetime.timedelta(days=days)
print(cur_date)
print(new)