import time
from datetime import datetime as dt

hostpATH=r"C:\Windows\System32\drivers\etc\hosts"
host_temps="hosts"
redirect="127.0.0.1"
web_list=["www.facebook.com","facebook.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8)< dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,15):
        print("Working Hours")
        with open(host_temps,'r+') as file:
            content=file.read()
            for wb in web_list:
                if wb in content:
                    pass
                else:
                    file.write(redirect+" "+wb+"\n")
    else:
        with open(host_temps,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in web_list):
                    file.write(line)
            file.truncate()
        print("Fun Hours......")

    time.sleep(5)
