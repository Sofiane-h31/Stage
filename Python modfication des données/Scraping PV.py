import requests
import re
import html
import pandas as pd

'''
probdef = []
proburl = []



def ttsaisons(url):
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
    }

    site=requests.get(url, headers=headers)
    if site.status_code==200:
        if 'fr' in url:
            saisons=re.findall(r'"seasonLink":"(/-/fr/detail/\w+/ref=atv_dp_season_select_s\d+)"', site.text)
        else:
            saisons = re.findall(r'"seasonLink":"(/detail/\w+/ref=atv_dp_season_select_s\d+)"', site.text)
            for i in range(len(saisons)):
                saisons[i]="/-/fr"+saisons[i]
        for i in range(len(saisons)):
            saisons[i]='https://www.primevideo.com'+saisons[i]
        return saisons


def classifPV(url):
    serie=True
    if 'app' in url:
        url=url+'&language=fr-FR'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
    }
    if serie==True:
        saisons=ttsaisons(url)
        classifep = []
        classifsais=[]
        numep=0
        try:
            #print(saisons)
            for saison in saisons:
                site=requests.get(saison, headers=headers)
                #print(site.text)
                if site.status_code==200:
                    ages=re.findall(r'aria-label="Ce contenu est classé ([^"]+)"' ,site.text)
                    if ages==[]:
                        ages.append('Tous Publics')
                    titres=re.findall(r'<span class="Z7ThIH"> - </span><span class="P1uAb6">([^<]+)<', site.text)
                    #print(ages)
                    for k in range(len(titres)):
                        titres[k]=html.unescape(titres[k])
                    #print(titres)
                    for i in range(1,len(ages)):
                        numep+=1
                        classifep.append((numep,ages[i]))
                    #print(classifep)
                    #print(ages)
                    classifsais.append(ages[0])
            return max(classifsais),classifep
        except Exception as e:
            proburl.append((url, e))
    else:
        try:
            site=requests.get(url, headers=headers)
            age = re.search(r'aria-label="Ce contenu est classé ([^"]+)"', site.text)
            return age.group(1)
        except Exception as e:
            proburl.append((url, e))
print(classifPV('https://app.primevideo.com/detail?gti=amzn1.dv.gti.24b8776e-16e0-e3e3-67e8-b144e97d7728'))


  #Series ou films
dataplat=pd.read_csv('dataplatfilms.csv', index_col=0)
eta = 1

for i in dataplat['Diffuseur']:
    print((dataplat.loc[dataplat['Diffuseur']==i, 'title']).to_string(), '     ', eta, '/ 637')
    if 'primevideo' in i:
        try:
            dataplat.loc[dataplat['Diffuseur'] == i, 'ClassificationSVOD'] = classifPV(i)
        except Exception as e:
            probdef.append((i, e))
        eta += 1



print(probdef)
print(len(probdef))

print(proburl)
print(len(proburl))
dataplat.to_csv('dataplatfilms.csv')

#-------------------------- Épisodes ----------------------------

#print(classifPV('https://www.primevideo.com/-/fr/detail/0IQX4B70WS4VB5JSB4GBTCACON'))
dataepisode=pd.DataFrame(columns=['NomSérie', 'NumEpisode', 'SVOD', 'ClassifEpisode'])


dataplat=pd.read_csv('resseries.csv', index_col=0)
eta = 1
lig=0
for i in dataplat['Diffuseur'][0:100]:
    print((dataplat.loc[dataplat['Diffuseur']==i, 'title']).to_string(), '     ', eta, '/ 639')
    if 'primevideo' in i:
        try:
            for j in classifPV(i)[1]:
                dataepisode.loc[lig]=[dataplat.loc[dataplat['Diffuseur']==i, 'title'].values[0], j[0], 'Prime Video', j[1]]
                lig+=1
        except Exception as e:
            probdef.append((i, e))
        eta += 1



print(probdef)
print(len(probdef))

print(proburl)
print(len(proburl))
dataepisode.to_csv('dataepisodes.csv')
'''

probdef = []
proburl = []



def ttsaisons(url):
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
    }

    site=requests.get(url, headers=headers)
    if site.status_code==200:
        if 'fr' in url:
            saisons=re.findall(r'"seasonLink":"(/-/fr/detail/\w+/ref=atv_dp_season_select_s\d+)"', site.text)
        else:
            saisons = re.findall(r'"seasonLink":"(/detail/\w+/ref=atv_dp_season_select_s\d+)"', site.text)
            for i in range(len(saisons)):
                saisons[i]="/-/fr"+saisons[i]
        for i in range(len(saisons)):
            saisons[i]='https://www.primevideo.com'+saisons[i]
        return saisons


def classifPV(url):
    serie=True
    if 'app' in url:
        url=url+'&language=fr-FR'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
    }
    if serie==True:
        saisons=ttsaisons(url)
        classifep = []
        classifsais=[]
        numep=0
        try:
            #print(saisons)
            for saison in saisons:
                site=requests.get(saison, headers=headers)
                #print(site.text)
                if site.status_code==200:
                    detailepi=re.findall(r'<span class="_36qUej izvPPq"><span>S\. (\d+) ÉP\. (\d+)</span>.+?aria-label="Ce contenu est classé ([^"]+)"', site.text)
                    print (detailepi)

        except Exception as e:
            proburl.append((url, e))

print(classifPV('https://app.primevideo.com/detail?gti=amzn1.dv.gti.8b96ae49-3860-49a5-8d15-7bd50c2ef008'))


