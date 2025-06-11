import pandas as pd
import requests
import re
#dataplat=pd.read_csv('resseries.csv', index_col=0)
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
def episodesCanal(url):
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    }
    site=requests.get(url, headers=headers)
    saisons=re.findall(r'"displayTemplate":"episodesList","URLPage":"([^"]+)', site.text)
    res=[]
    for lien in saisons:
        lien = lien.replace("\\u002F", "/")
        lien = lien.replace("\\u003A", ":")
        lien = lien.replace("\\u002E", ".")
        apisais=requests.get(lien, headers=headers)
        for h in apisais.json()['episodes']['contents']:
            res.append((str(h['seasonNumber']), str(h['episodeNumber']), h['editorialTitle']))
    return res



print(episodesCanal("https://www.mycanal.fr/series/boardwalk-empire/h/40470406_50889"))

'''
dataepisodes=pd.read_csv('dataepisodes.csv', index_col=0)

eta=0
for i in dataplat.index[:20]:
    print(f"{dataplat.loc[i, 'title']}    {eta}/43")
    if dataplat.loc[i, 'SVOD']=='Canal+' or dataplat.loc[i, 'SVOD']=='MyCanal':
        eta+=1
        try:
            res=episodesCanal(dataplat.loc[i, 'Diffuseur'])
            for j in res:
                dataepisodes = dataepisodes._append(
                {'idSerie': dataplat.loc[i, 'id'],
                'title': dataplat.loc[i, 'title'],
                     'SVOD': 'Canal+/MyCanal',
                     'saison': j[0],
                     'episode':j[1],
                     'ClassifEp': dataplat.loc[i, 'ClassificationSVOD'],},
                    ignore_index=True)

        except Exception as e:
            probdef.append((i, dataplat.loc[i, 'title'], e))


print(probdef)
print(len(probdef))

print(probannee)
print(len(probannee))
dataepisodes.to_csv('dataepisodesTest.csv')
'''

dataplat=pd.read_csv('resseriesvecteur.csv', index_col=0)
dataepisodes=pd.read_csv('resepisodesTestApple.csv', index_col=0)
prob=[]
eta=0
for k in dataplat.index[:186]:
    eta+=1
    print(f"{dataplat.loc[k, 'title']}      {eta} / 186")
    try:
        if dataplat.loc[k, 'id'] in dataepisodes['idSerie'].values and dataplat.loc[k, 'SVOD'] in ('MyCanal', 'Canal+'):
            urlser=dataplat.loc[k, 'Diffuseur']
            res = episodesCanal(urlser)
            for idx,j in dataepisodes[dataepisodes['idSerie']==dataplat.loc[k, 'id']].iterrows():
                for h in res:
                    if h[0]==str(j.saison) and h[1]==str(j.episode):
                        #print(html.unescape(h[2]))
                        dataepisodes.loc[idx, 'titreEP']=h[2]
    except Exception as e:
        prob.append((k))
        print(e)

print(prob)
print(len(prob))
dataepisodes.to_csv('resepisodesTestCanal.csv')