import json, requests
from bs4 import BeautifulSoup
op=open('/home/navgurukul20/Desktop/VIKASH_K/Files_requests_API+WebS/Task1.json', 'r')
movie_=json.load(op)
movie_list=[]
for us_url in movie_:
    movie_request=requests.get(us_url['Url']+'?ref_=hm_rvi_tt_t_1')
    soup=BeautifulSoup(movie_request.text, 'html.parser')   
    dirctr=soup.find('div', class_="ipc-metadata-list-item__content-container").text
    dirctr2=soup.find('a', class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link").text
    director = [dirctr2, dirctr[len(dirctr2): ]]
    if len(director[-1])==0:
        director.pop()
    # print(director)    
    bio=soup.find('span', class_="GenresAndPlot__TextContainerBreakpointXL-cum89p-2 gCtawA").text
    # print(bio)    
    try:
        navrasa=soup.findAll('div', class_="ipc-chip-list GenresAndPlot__GenresChipList-cum89p-4 gtBDBL")      
    finally:
        generic = []
        for i in navrasa:
            p=(i.findAll("a"))
            for i in p:
                generic.append(i.text)
        # print(generic)
    ru=soup.find('div',class_="TitleBlock__TitleMetaDataContainer-sc-1nlhx7j-2 hWHMKr")
    for i in ru:
        p1=(i.findAll("li"))
        for k in p1:
            pass            
    duration=k.text.split()
    try:
        rtime=(int(duration[0].strip('h'))*60 + int(duration[-1].strip('min')))
        # print(rtime)
    except:
        pass
        # print(rtime)
        # rtime=(int(duration.strip('h'))*60)    
    lan=soup.find('ul', class_="ipc-metadata-list ipc-metadata-list--dividers-all ipc-metadata-list--base").text
    try:
        pr=(lan.split())
        # print(pr[6])
        # print()
    except:
        pass
        # print(lan)    
    lan=soup.find('ul', class_="ipc-metadata-list ipc-metadata-list--dividers-all ipc-metadata-list--base")
    detail=[]
    for ik in lan:
        p2=(ik.findAll('li'))
        for ki in p2:
            detail.append(ki.text)
    # print(detail)
    try:
        country=detail[1]
    except:
        country='India'
    finally:
        if len(detail[2:-1])>3:
            language=detail[2:5]
        else:
            language=detail[2:-1]    
    image=soup.find('img', class_="ipc-image")    
    Url=str(image).split()
    for v in Url:
        if v[0:4]=="src=":
            Url1=v.strip('src="')
            break
    movie_list.append({'Name':us_url['Name'], 'Director':director, 'Country':country, 'Language':language, 'Poster_image_Url':Url1, 'Bio':bio, 'Runtime':rtime, 'Genre':generic, })     
    # print(movie_list)   
task4=open('/home/navgurukul20/Desktop/VIKASH_K/Files_requests_API+WebS/Task4.json', 'w')
json.dump(movie_list, task4, indent=4)  

