import requests
import re
import pandas as pd
import numpy as np
from simplejustwatchapi import *
'''

dataplat=pd.read_csv('resseries.csv', index_col=0)
probdef=[]
proburl = []

def classifdisney(url):
    site=requests.get(url, allow_redirects=True)
    #print(site.url)
    url=site.url[:26]+'/fr-fr/'+site.url[27:]
    site=requests.get(url)
    try:
        if site.status_code==200:
            #print(site.text)
            age=re.search(r'Classification.*id="(\d+\+)"', site.text)
        return age.group(1)
    except Exception as e:
        proburl.append((url,e))


print(classifdisney("https://disneyplus.bn5x.net/c/1206980/705874/9358?u=https%3A%2F%2Fwww.disneyplus.com%2Fmovies%2Fthe-happening%2F2V6FKeZRE593&subId3=justappsvod"))

eta = 0
for i in dataplat['Diffuseur']:
    print((dataplat.loc[dataplat['Diffuseur']==i, 'title']).to_string(), '     ', eta, '/ 425')
    if 'disney' in i:
        try:
            dataplat.loc[dataplat['Diffuseur'] == i, 'ClassificationSVOD'] = classifdisney(i)
        except Exception as e:
            probdef.append((i, e))
        eta += 1

print(probdef)
print(len(probdef))

print(proburl)
print(len(proburl))
dataplat.to_csv('dataplatfilms.csv')
'''


#--------------------------------------------Episodes----------------------------------
probannee=[]
probdef=[]
dataplat=pd.read_csv('resseries.csv', index_col=0)
dataepisodes=pd.read_csv('dataepisodes.csv')
def episodesDisney(idjw):
    seri = details(idjw)
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiMDg4Y2JmOTRjMWVhY2RkN2E3NzZlNTYzYWZmNmMyOCIsIm5iZiI6MTc0NzMxMTgyOS44MzMsInN1YiI6IjY4MjVkY2Q1YWZjOTY2NGQ4NTVhM2E2YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.iy7E3VfMCN5Pxw8jTIBNcTaruLFpfWZlU9PSIAffTWw"
    }
    url = f"https://api.themoviedb.org/3/tv/{seri.tmdb_id}"
    response = requests.get(url, headers=headers)
    data = response.json()
    return data['number_of_episodes'], data['first_air_date']


eta=0
for i in dataplat.index[:186]:
    print(f"{dataplat.loc[i, 'title']}    {eta}/26")
    if dataplat.loc[i, 'SVOD']=='Disney+':
        eta+=1
        try:
            res=episodesDisney(dataplat.loc[i, 'idjw'])
            if str(dataplat.loc[i, 'releaseYear'])[:4] not in res[1]:
                probannee.append((i, dataplat.loc[i, 'releaseYear'], res[1]))
            print(res[0])
            for j in range(1, res[0]+1):
                dataepisodes = dataepisodes._append(
                {'NomSérie': dataplat.loc[i, 'title'],
                     'NumEpisode': j,
                     'SVOD': 'Disney+',
                     'ClassifEpisode': dataplat.loc[i, 'ClassificationSVOD']},
                    ignore_index=True)

        except Exception as e:
            probdef.append((i, dataplat.loc[i, 'title'], e))

print(probdef)
print(len(probdef))

print(probannee)
print(len(probannee))
dataepisodes.to_csv('dataepisodesTest.csv', index=False)