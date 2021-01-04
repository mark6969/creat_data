import random
from datetime import datetime , timedelta
time_up = "2020-06-01"
time_to = "2020-11-30"
time_up = datetime.strptime(time_up, "%Y-%m-%d")
time_to = datetime.strptime(time_to, "%Y-%m-%d")
def creat_data(date):
    all_date = list()
    date = datetime.strftime(time_up, "%Y-%m-%d")
    date = date.replace("-", "")
    code1 = random.randint(0,1)
    code2 = "%05d" % (random.randint(0,100))
    if code1 == 0:
            code1 = ""
    else:
        code1 = code2  
    last_code = "G10101" + str(random.randint(0,1))
    all_date.append(date)
    all_date.append(code1)
    all_date.append(code2)
    all_date.append(last_code)
    all_date = ",".join(all_date)
    return all_date
while time_to >= time_up:
    num = random.randint(20,50)
    all_date = list()
    for i in range(num):
        a = creat_data(time_up)
        all_date.append(a)
    all_date = "\n".join(all_date)
    file_name = "data/mipList_{}_ok.txt".format(a[0:8])
    f=open(file_name, "w")
    f.writelines(all_date)
    time_up = time_up + timedelta(days = 1)