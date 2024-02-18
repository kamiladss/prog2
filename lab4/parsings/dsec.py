import datetime
import math
date1 = input("Enter the first date (YYYY-MM-DD HH:MM:SS): ")
date2 = input("Enter the second date (same as first type): ")
dif=datetime.datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")-datetime.datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
print(dif.total_seconds())