import requests
import re
import pandas as pd

dataplat=pd.read_csv('dataplatfilms.csv', index_col=0)
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

            response = requests.get(url, headers=headers)
            saison=re.search(r'\s*<option value="([^"]*)"\n?\s*selected', response.text)
            saison=int(saison.group(1))
            res=[]


            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Referer": url,
                "X-Requested-With": "XMLHttpRequest",
            }
            numep=1
            while True:

                url = f"https://www.paramountplus.com/fr/shows/{noms}/xhr/episodes/page/0/size/100/xs/0/season/{saison}/"
                response = requests.get(url, headers=headers)

                response.raise_for_status()
                data = response.json()
                episodes = data.get("result", {}).get("data", [])
                if episodes==[]:
                    break
                #print(episodes)
                for ep in episodes:
                    res.append((numep, ep.get('rating')))    #ep.get('label') pour le nom
                    numep+=1
                saison+=1
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



#print(classifPara('https://www.paramountplus.com/movies/terminal/SbftopjV73X6FMDkxZwA5UZ722osA2fp?searchReferral='))
#print(proburl)

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

