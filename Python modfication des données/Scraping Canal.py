import pandas as pd
import requests
import re
from simplejustwatchapi import *
dataplat=pd.read_csv('resseries.csv', index_col=0)
probdef=[]
proburl=[]

def classifCanal(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    }

    site = requests.get(url, headers=headers)
    print(site.text)
    if site.status_code == 200:
        age=re.search(r'title="Moins de (\d{1,2}) ans"', site.text)
        return '-'+age.group(1)
    else:proburl.append(url)

#print(classifCanal('https://www.mycanal.fr/series/the-big-bang-theory/h/40422267_50889'))

'''
eta = 0
for i in dataplat['Diffuseur']:
    print((dataplat.loc[dataplat['Diffuseur']==i, 'title']).to_string(), '     ', eta, '/ 121')
    if 'canal' in i:
        try:
            dataplat.loc[dataplat['Diffuseur'] == i, 'ClassificationSVOD'] = classifCanal(i)
        except Exception as e:
            probdef.append((i, e))
        eta += 1

print(probdef)
print(len(probdef))

print(proburl)
print(len(proburl))
dataplat.to_csv('dataplatTest.csv')

'''
#-----------------------------------EPISODES------------------------------------
def episodesCanal(idjw):
    seri = details(idjw)
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiMDg4Y2JmOTRjMWVhY2RkN2E3NzZlNTYzYWZmNmMyOCIsIm5iZiI6MTc0NzMxMTgyOS44MzMsInN1YiI6IjY4MjVkY2Q1YWZjOTY2NGQ4NTVhM2E2YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.iy7E3VfMCN5Pxw8jTIBNcTaruLFpfWZlU9PSIAffTWw"
    }
    url = f"https://api.themoviedb.org/3/tv/{seri.tmdb_id}"
    response = requests.get(url, headers=headers)
    data = response.json()
    return data['number_of_episodes'], data['first_air_date']

dataepisodes=pd.read_csv('dataepisodes.csv', index_col=0)

eta=0
probannee=[]
for i in dataplat.index[:20]:
    print(f"{dataplat.loc[i, 'title']}    {eta}/43")
    if dataplat.loc[i, 'SVOD']=='Canal+' or dataplat.loc[i, 'SVOD']=='MyCanal':
        eta+=1
        try:
            res=episodesCanal(dataplat.loc[i, 'idjw'])
            for j in range(1, res[0]+1):
                dataepisodes = dataepisodes._append(
                {'NomSérie': dataplat.loc[i, 'title'],
                     'NumEpisode': j,
                     'SVOD': 'Canal+/MyCanal',
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
dataepisodes.to_csv('dataepisodesTest.csv')