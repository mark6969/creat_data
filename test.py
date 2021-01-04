import random
from datetime import datetime
time_up = "2020-06-01"
time_to = "2020-11-30"
time_up = datetime.strptime(time_up, "%Y-%m-%d")
time_to = datetime.strptime(time_to, "%Y-%m-%d")
s = datetime.strftime(time_up, "%Y-%m-%d")
if time_to > time_up:
    print("1")
print(time_up)
print(s)