import datetime
date = datetime.date.now()
micro = date.replace(microsecond=0)
print(micro)