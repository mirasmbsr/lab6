from datetime import datetime, date, time, timedelta

date1 = date.today()
date = date1 - timedelta(days=+1)
date2 = date1 - timedelta(days=-1)
print(date2,date,date1)