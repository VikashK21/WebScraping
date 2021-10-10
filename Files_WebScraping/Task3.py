import json
def group_by_decade():
    jfile1=open('/home/navgurukul20/Desktop/VIKASH_K/Files_requests_API+WebS/Task2.json', 'r')
    moviesyear=json.load(jfile1)
    moviesperiod={}
    for yrs in moviesyear:
        moviedetails=[]
        # print(moviedetails)
        yrs1=(int(yrs))//10*10
        # print(yrs1)
        for period in range(yrs1, yrs1+10):
            if str(period) in moviesyear:
                moviedetails.extend(moviesyear[(str(period))])
                # print(moviesyear[(str(period))])
        moviesperiod.update({(str(yrs1)+" - "+str(yrs1+9)):moviedetails})
    jfile2=open('/home/navgurukul20/Desktop/VIKASH_K/Files_requests_API+WebS/Task3.json', 'w')
    json.dump(moviesperiod, jfile2, indent=4)      
    jfile2.close()
    return moviesperiod
print(group_by_decade())






