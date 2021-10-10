
import json

file_12p=open("/home/navgurukul20/Desktop/VIKASH_K/Files_requests_API+WebS/Task13.json", 'r')
task_12p1=json.load(file_12p)
ls=[]
for z in task_12p1:
    nls=[]
    for y in z['Cast']:
        nls.append(y['Id'])
    ls.append(nls)

#################Task14 p2: The above one is also connected.

file_13=open("/home/navgurukul20/Desktop/VIKASH_K/Files_requests_API+WebS/Task13.json", 'r')
task_14=json.load(file_13)

for dic in task_14:
    cast_list=[]
    castlist=dic['Cast']
    print()
    for cast in range(len(dic['Cast'])-1):
        s=0
        dic2=castlist[cast]
        dic3=castlist[cast+1]
        for ids in ls:
            if dic3['Id'] in ids and dic2['Id'] in ids:
                s+=1
        frequent_co={'imdb_id':dic3['Id'], 'Name':dic3['Name'], 'num_movie':s}
        cast_list.append({dic2['Id']:{'Name':dic2['Name'], 'Frequent_co_actors':[frequent_co]}})
        print()
    dic.update({"Cast":cast_list})  
    print(dic)  
file_14=open("/home/navgurukul20/Desktop/VIKASH_K/Files_requests_API+WebS/Task14.json", "w")
json.dump(task_14, file_14, indent=4)
file_14.close()

