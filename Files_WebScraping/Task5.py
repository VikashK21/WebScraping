import json

file2point0=open('./Files_requests_API+WebS/Task4.json', 'r')

loading=json.load(file2point0)

def analyse_movies_language(movies_list):
    hr=movies_list['Runtime']//60
    min=movies_list['Runtime']%60
    movies_list['Runtime']={'hours':hr, 'minutes':min}
for details in loading:
    analyse_movies_language(details)
    
file2point1=open('./Files_requests_API+WebS/Task5_6.json', 'w')
f=open('./Files_requests_API+WebS/copy_5_6.json', 'r')
f2=json.load(f)
json.dump(f2, file2point1, indent=4)    

