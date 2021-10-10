import json

files=open('/home/navgurukul20/Desktop/VIKASH_K/Files_requests_API+WebS/Task5_6.json', 'r')
v3=json.load(files)
dic={}    
def analyse_movies_directors(movies_list):
    global s
    for cout in movies_list:
    
        if cout in dic:
            s=dic[cout]
            s+=1
            dic.update({cout:s})
        else:
            dic.update({cout:s})

for details in v3:
    s=1
    analyse_movies_directors(details['Director'])
print(dic)