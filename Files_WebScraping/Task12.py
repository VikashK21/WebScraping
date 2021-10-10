

import requests, json
from bs4 import BeautifulSoup
import random, time

rsleep=random.randint(1, 3)
file_=open("/home/navgurukul20/Desktop/VIKASH_K/Files_requests_API+WebS/Task1.json", 'r')
file_task1=json.load(file_)

dic=[]
for movedic in file_task1:
    time.sleep(rsleep)
    url=requests.get(movedic['Url']+"fullcredits?ref_=tt_cl_sm#cast")
    soup=BeautifulSoup(url.text, "html.parser")
    movie_=soup.find_all('table', class_="cast_list")
    s=1
    ss=soup.findAll("table",class_="cast_list")
    for i in ss:
        p=(i.findAll("a"))
        s=0
        for j in p:
            lisitms=(str(j)).split("/")
            if len(lisitms)==5:
                dic.append({'Name':(lisitms[-2]).strip('  ">\n<'), 'Id':lisitms[-3]})

    print(dic)    
anfile=open("/home/navgurukul20/Desktop/VIKASH_K/Files_requests_API+WebS/Task12.json", 'w')
json.dump(dic, anfile, indent=4)
anfile.close()
   
