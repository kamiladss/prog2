import datetime
cur_date=datetime.datetime.now()

yest=cur_date-datetime.timedelta(days=1)
tom=cur_date+datetime.timedelta(days=1)
print(yest)
print(cur_date)
print(tom)