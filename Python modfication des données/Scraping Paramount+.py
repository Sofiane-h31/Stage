import requests
import re
import pandas as pd

probdef=[]
proburl = []
def classifPara(url):
    #try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        }
        if 'show' in url:
            noms = ''
            for i in url[36:]:
                if i != '/':
                    noms += i
                else:
                    break

            site=requests.get(url, headers=headers)
            #print(site.text)
            saisons=re.findall(r'\s*<option value="([^"]*)"\n?\s*', site.text)
            for i in range(len(saisons)):
                saisons[i]=int(saisons[i])
            res=[]


            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Referer": url,
                "X-Requested-With": "XMLHttpRequest",
            }
            for saison in saisons:
                url = f"https://www.paramountplus.com/fr/shows/{noms}/xhr/episodes/page/0/size/100/xs/0/season/{saison}/"
                response = requests.get(url, headers=headers)

                response.raise_for_status()
                data = response.json()
                episodes = data.get("result", {}).get("data", [])

                if episodes==[]:
                    break
                #print(episodes)
                for ep in episodes:
                    res.append((ep.get('season_number'),ep.get('episode_number') ,ep.get('rating')))    #ep.get('label') pour le nom
                #print(cpt)
            return max(res, key=lambda x: int(x[1]) if x[1]!='' else 1)[1], res
        else:
            site=requests.get(url, headers=headers)
            age=re.search(r'"contentRating":"([^"]+)"', site.text)
            if age==None and site.status_code==200:
                return '0'
            return age.group(1)
    #except Exception as e:
        #proburl.append((url, e))



print(classifPara('https://www.paramountplus.com/shows/yellowstone/video/vPXPeC4posOemTL_KvmcbAPhi6j_s7_f/yellowstone-daybreak?searchReferral='))
#print(proburl)
'''
eta = 0
for i in dataplat['Diffuseur']:
    print((dataplat.loc[dataplat['Diffuseur']==i, 'title']).to_string(), '     ', eta, '/ 135')
    if 'paramount' in i:
        if dataplat.loc[dataplat['Diffuseur'] == i, 'ClassificationSVOD'].isna().any():
            try:
                dataplat.loc[dataplat['Diffuseur'] == i, 'ClassificationSVOD'] = classifPara(i)
            except Exception as e:
                probdef.append((i, e))
            eta += 1

print(probdef)
print(len(probdef))

print(proburl)
print(len(proburl))
dataplat.to_csv('dataplatTest.csv')
'''
#------------------------------------------------- EPISODES -----------------------------------
dataseries=pd.read_csv('resseries.csv', index_col=0)
dataepisodes=pd.read_csv('dataepisodes2.csv', index_col=0)
eta=0
for i in dataseries.index[:186]:
    eta+=1
    print(f"{dataseries.loc[i, 'title']}      {eta} / 186")
    try:
        if dataseries.loc[i, 'SVOD']=='Paramount+':
            res=classifPara(dataseries.loc[i, 'Diffuseur'])[1]
            for h in res:
                dataepisodes=dataepisodes._append({'idSerie':dataseries.loc[i, 'id'], 'title':dataseries.loc[i, 'title'],'SVOD': dataseries.loc[i, 'SVOD'] ,'saison':h[0], 'episode':h[1], 'ClassifEP':h[2]}, ignore_index=True)
    except Exception as e:
        proburl.append((dataseries.loc[i, 'id'], e))
print(dataepisodes)
dataepisodes.to_csv('dataepisodes2Test.csv')

print(proburl)
print(len(proburl))
