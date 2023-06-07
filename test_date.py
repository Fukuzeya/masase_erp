import datetime


today = datetime.datetime.today().date()
count = 1
date_str = str(today)
today = date_str.replace("-","") + str(count)
print(today)
