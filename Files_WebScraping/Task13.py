import requests, json
from bs4 import BeautifulSoup
import random, time

rsleep=random.randint(1, 3)
file_=open("/home/navgurukul20/Desktop/VIKASH_K/Files_requests_API+WebS/Task1.json", 'r')
file_2=open("/home/navgurukul20/Desktop/VIKASH_K/Files_requests_API+WebS/Task4.json", 'r')
file_task1=json.load(file_)
file_task4=json.load(file_2)

s=0
for movedic in file_task1:
    dic=[]
    time.sleep(rsleep)
    url=requests.get(movedic['Url']+"fullcredits?ref_=tt_cl_sm#cast")
    soup=BeautifulSoup(url.text, "html.parser")
    ss=soup.findAll("table",class_="cast_list")
    for i in ss:
        p=(i.findAll("a"))
        for j in p:
            lisitms=(str(j)).split("/")
            if len(lisitms)==5:
                dic.append({'Name':(lisitms[-2]).strip('  ">\n<'), 'Id':lisitms[-3]})
    (file_task4[s]).update({"Cast":dic})
    print(file_task4[s])  
    s+=1
anfile=open("/home/navgurukul20/Desktop/VIKASH_K/Files_requests_API+WebS/Task13.json", 'w')
json.dump(file_task4, anfile, indent=4)
anfile.close()

