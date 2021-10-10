
import json

file_14=open("/home/navgurukul20/Desktop/VIKASH_K/Files_requests_API+WebS/Task14.json", "r")
task_15=json.load(file_14)
def analyse_actors(movies_list):
    list_cast=[]
    for cast in movies_list:
        for i in cast:
            if (cast[i]['Frequent_co_actors'][0]['num_movie'])>1:
                print(cast)
                list_cast.append(cast)
                # print(movies_list)
    return list_cast
for get_movie_list_details in task_15:
    x=analyse_actors(get_movie_list_details['Cast'])
    get_movie_list_details['Cast']=x
file_15=open('/home/navgurukul20/Desktop/VIKASH_K/Files_requests_API+WebS/Task15.json', 'w')
json.dump(task_15, file_15, indent=4)