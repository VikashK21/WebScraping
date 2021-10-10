import json
from pprint import pprint
def group_by_year():
    jfile=open('/home/navgurukul20/Desktop/VIKASH_K/Files_requests_API+WebS/Task1.json', 'r')
    imdbmovies=json.load(jfile)
    moviesdic={}
    for movies in imdbmovies:
        listdic=[]
        for same in imdbmovies:
            if movies['Year']==same['Year']:
                listdic.append(same)
        moviesdic.update({int(movies['Year']):listdic})
    jfile1=open('/home/navgurukul20/Desktop/VIKASH_K/Files_requests_API+WebS/Task2.json', 'w')
    json.dump(moviesdic, jfile1, indent=4)
    jfile.close()
    return moviesdic

pprint(group_by_year())
        







