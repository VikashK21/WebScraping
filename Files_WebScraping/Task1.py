from os import PRIO_PGRP
import requests, json

from bs4 import BeautifulSoup
from pprint import pprint

movie=requests.get('https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in')
soup=BeautifulSoup(movie.text, 'html.parser')
def scrape_top_list():
    
    ss=soup.find("tbody",class_="lister-list")
    trs=ss.find_all('tr')
    global TheMoviesList
    TheMoviesList=[]
    for tr in trs:
        lism=0
        p_n_y=tr.find('td', class_="titleColumn").get_text()
        lism=p_n_y.strip().split("\n")
        lism.extend([tr.find('td', class_="ratingColumn imdbRating").strong.get_text(),'https://www.imdb.com/'+(tr.find('td', class_="titleColumn").a['href'])])
        tp=int(lism[0][:-1])
        ty=int(lism[2][1:-1])
        trating=float(lism[3])
        dic={'Position':tp, 'Name':lism[1].strip( ), 'Year':ty, 'Rating':trating, 'Url':lism[-1]}
        TheMoviesList.append(dic)
    jfile=open('/home/navgurukul20/Desktop/VIKASH_K/Files_requests_API+WebS/Task1.json', 'w')
    json.dump(TheMoviesList, jfile, indent=4)
    jfile.close()
    return TheMoviesList
pprint(scrape_top_list())




