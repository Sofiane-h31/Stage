import pandas as pd
import numpy as np
import requests
import re
#------------------------------------------------------SÉRIES----------------------------------------------------------------------------------
dataplat=pd.read_csv('dataplatfilms.csv', index_col=0)
probdef=[]
proburl=[]

'''
def idserie(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
    }
    if 'episode' in url:

        siteep=requests.get(url, headers=headers)
        #print(siteep.text)
        url=re.search(r'"showUrl":"([^"]+)"', siteep.text).group(1)
        id=''
        for i in url[::-1]:
            if i!='/':
                id+=i
            else:
                break
        site=requests.get(url, headers=headers)
        classifserie=re.search(r'"contentRating":"([^"]+)"', site.text)
        return id[::-1], classifserie.group(1)
    else:
        id=''
        for i in url[29:]:
            if i!='?':
                id+=i
            else:
                break
        shlas=id.find('/')
        id=id[shlas+1:]
        site = requests.get(url, headers=headers)
        classifserie = re.search(r'"contentRating":"([^"]+)"', site.text)
        return id, classifserie.group(1)

erreurs=[]





def classifApple(url):
    try:
        id, classifserie=idserie(url)
        url = f"https://tv.apple.com/api/uts/v3/shows/{id}/episodes"

        params = {
            'caller': 'web',
            'locale': 'fr-FR',
            'nextToken': '0:999999999',
            'pfm': 'web',
            'sf': '143442',
            'utscf': 'OjAAAAEAAAAAAAAAEAAAACMA',
            'utsk': '6e3013c6d6fae3c2:::::235656c069bb0efb',
            'v': '82'
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
        }

        response = requests.get(url, params=params, headers=headers)

        if response.status_code == 200:
            data=response.json()

            episodes = data.get('data', {}).get('episodes', [])
            listepi=[]
            for ep in episodes:
                if 'rating' in ep.keys():
                    classif=ep['rating']['displayName']
                else:
                    classif = classifserie
                numsais = ep.get('seasonNumber', 'N/A')
                numep = ep.get('episodeNumber', 'N/A')
                listepi.append((numsais, numep, classif))
            return classifserie,listepi
    except Exception as e:
        proburl.append((url,e))



url='https://tv.apple.com/fr/episode/le-bon-cote-de-lenfer/umc.cmc.s80mx1ic96pu6ewupz8pfasf?at=1000l3V2&ct=app_tvplus&itscg=30200&itsct=justwatch_tv_12&playableId=tvs.sbd.4000%3AVSEVR0560101&showId=umc.cmc.1srk2goyh2q2zdxcx605w8vtx'
url2='https://tv.apple.com/fr/show/south-park/umc.cmc.1n9fnkfiemhayikewq5xitzn6?at=1000l3V2&ct=app_tv&itscg=30200&itsct=justwatch_tv_12'
url3='https://tv.apple.com/fr/show/yellowstone/umc.cmc.2bnarwrthyaosxk1pkoefxzj0?at=1000l3V2&ct=app_tv&itscg=30200&itsct=justwatch_tv_12'
print(classifApple('https://tv.apple.com/fr/show/frasier/umc.cmc.3y5ua8o8t6yea2aj66pqsptkd?at=1000l3V2&ct=app_tv&itscg=30200&itsct=justwatch_tv_12'))

eta = 0
for i in dataplat['Diffuseur']:
    print((dataplat.loc[dataplat['Diffuseur']==i, 'title']).to_string(), '     ', eta, '/ 118')
    if 'apple' in i:
        try:
            dataplat.loc[dataplat['Diffuseur'] == i, 'ClassificationSVOD'] = classifApple(i)[0]
        except Exception as e:
            probdef.append((i, e))
        eta += 1

print(probdef)
print(len(probdef))

print(proburl)
print(len(proburl))
dataplat.to_csv('dataplatTest.csv')

'''
#------------------------------------------------------FILMS----------------------------------------------------------------------------------


def idserie(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
    }
    if 'episode' in url:

        siteep=requests.get(url, headers=headers)
        #print(siteep.text)
        url=re.search(r'"showUrl":"([^"]+)"', siteep.text).group(1)
        id=''
        for i in url[::-1]:
            if i!='/':
                id+=i
            else:
                break
        site=requests.get(url, headers=headers)
        classifserie=re.search(r'"contentRating":"([^"]+)"', site.text)
        return id[::-1], classifserie.group(1)
    else:
        id=''
        site = requests.get(url, headers=headers)
        if 'show' in url:
            pars=url[29:]
            classifserie = re.search(r'"contentRating":"([^"]+)"', site.text)
        else:
            pars=url[42:]
            classifserie = re.search(r'aria-label="ClassÃ© ([^"]+)"', site.text)
            return classifserie.group(1)
        for i in pars:
            if i!='?':
                id+=i
            else:
                break
        shlas=id.find('/')
        id=id[shlas+1:]
        return classifserie.group(1)
#print(idserie('https://tv.apple.com/fr/show/yellowstone/umc.cmc.2bnarwrthyaosxk1pkoefxzj0?at=1000l3V2&ct=app_tv&itscg=30200&itsct=justwatch_tv_12'))
#print(idserie('https://tv.apple.com/fr/movie/napoleon/umc.cmc.25k80oxl3vo69c8rimk8v81s1?at=1000l3V2&ct=app_tvplus&itscg=30200&itsct=justwatch_tv_12'))



eta = 0
for i in dataplat['Diffuseur']:
    print((dataplat.loc[dataplat['Diffuseur']==i, 'title']).to_string(), '     ', eta, '/ 130')
    if 'apple' in i:
        try:
            dataplat.loc[dataplat['Diffuseur'] == i, 'ClassificationSVOD'] = idserie(i)
        except Exception as e:
            probdef.append((i, e))
        eta += 1

print(probdef)
print(len(probdef))

print(proburl)
print(len(proburl))
dataplat.to_csv('dataplatTest.csv')