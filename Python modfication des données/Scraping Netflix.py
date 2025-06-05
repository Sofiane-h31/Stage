import pandas as pd
import numpy as np
import requests
import re
from simplejustwatchapi import *

'''
#-------------------------------------------------------------- Séries Films -------------------------------------------

#dataplat=pd.read_csv('platfilms.csv', index_col=0)
#dataplat['ClassificationSVOD']=None

probdef = []


def classifnetflix(url):
    url = url[:24] + 'fr/' + url[24:]
    serie = False  # Modifier pour les films

    headers = {
        'Accept-Encoding': 'identity'
    }

    site = requests.get(url, headers=headers)

    html = site.text
    print(html)
    if site.status_code == 200:
        age = re.search(r'"contentRating":"([^"]+)"', html)
        if age:
            if serie == True:
                episodes = re.findall(r'"episodeNum":([^,]*)', html)
                episodes = [(i, age.group(1)) for i in range(1, len(episodes) + 1)]
                return age.group(1), episodes
            else:
                return age.group(1)
        else:
            print("Problème d'âge :", url)
            probdef.append(url)

print(classifnetflix('https://www.netflix.com/title/70143836'))


proburl = []
eta = 0
for i in dataplat['Diffuseur']:
    print((dataplat.loc[dataplat['Diffuseur']==i, 'title']).to_string(), '     ', eta, '/ 332')
    if 'netflix' in i:
        try:
            dataplat.loc[dataplat['Diffuseur'] == i, 'ClassificationSVOD'] = classifnetflix(i)
        except Exception as e:
            probdef.append((i, e))
        eta += 1

print(probdef)
print(len(probdef))

print(probdef)
print(len(probdef))
dataplat.to_csv('dataplatfilms.csv')

'''
#--------------------------------------------------------------- Épisodes ----------------------------------------------


dataplat=pd.read_csv('resseries.csv', index_col=0)
dataepisodes=pd.read_csv('dataepisodes.csv', index_col=0)
'''

probdef=[]
probannee=[]


def episodesNetflix(idjw):
        seri=details(idjw)
        headers={
            "accept": "application/json",
            "Authorization": f"Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiMDg4Y2JmOTRjMWVhY2RkN2E3NzZlNTYzYWZmNmMyOCIsIm5iZiI6MTc0NzMxMTgyOS44MzMsInN1YiI6IjY4MjVkY2Q1YWZjOTY2NGQ4NTVhM2E2YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.iy7E3VfMCN5Pxw8jTIBNcTaruLFpfWZlU9PSIAffTWw"
        }
        url=f"https://api.themoviedb.org/3/tv/{seri.tmdb_id}"
        response=requests.get(url, headers=headers)
        data=response.json()
        return data['number_of_episodes'], data['first_air_date']



#print(episodesNetflix('ts4'))
eta=0
for i in dataplat.index[:186]:
    print(f"{dataplat.loc[i, 'title']}    {eta}/43")
    if dataplat.loc[i, 'SVOD']=='Netflix':
        eta+=1
        try:
            res=episodesNetflix(dataplat.loc[i, 'idjw'])
            for j in range(1, res[0]+1):
                dataepisodes = dataepisodes._append(
                {'NomSérie': dataplat.loc[i, 'title'],
                     'NumEpisode': j,
                     'SVOD': 'Netflix',
                     'ClassifEpisode': dataplat.loc[i, 'ClassificationSVOD'],},
                    ignore_index=True)
            if str(dataplat.loc[i, 'releaseYear'])[:4] not in res[1]:
                probannee.append((i, dataplat.loc[i, 'releaseYear'], res[1]))
        except Exception as e:
            probdef.append((i, dataplat.loc[i, 'title'], e))


print(probdef)
print(len(probdef))

print(probannee)
print(len(probannee))
dataepisodes.to_csv('dataepisodesTest.csv', index=False)



#Ajout manuel
'''
ligne=pd.DataFrame([{'NomSérie': 'The Simpsons',
         'NumEpisode': 1,
         'SVOD': 'Disney+',
         'ClassifEpisode': '12+' }])
for j in range(2, 849):
    ligne=ligne._append({'NomSérie': 'The Simpsons' ,
         'NumEpisode': j,
         'SVOD': 'Disney+',
         'ClassifEpisode': '12+' }, ignore_index=True)

ligne.to_csv('dataepisodesCasadelpapel.csv', index=False)



