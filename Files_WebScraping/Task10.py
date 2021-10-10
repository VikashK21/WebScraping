
import json

files=open('/home/navgurukul20/Desktop/VIKASH_K/Files_requests_API+WebS/Task5_6.json', 'r')
v3=json.load(files)
dic={}    
def analyse_movies_directors(movies_list,languagelist):
    global s
    for cout in movies_list:   
        for language in languagelist:
            if cout in dic:
                dic3=dic[cout]
                if language in dic[cout]:
                    s=dic[cout][language]
                    s+=1                     
                    dic.update({cout:{language:s}})
                else:
                    dic3[language]=s
                    dic[cout]=dic3
            else:
                dic.update({cout:{language:s}})
for details in v3:
    s=1
    analyse_movies_directors(details['Director'],details['Language'])
print(dic)

