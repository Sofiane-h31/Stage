import requests
import re
import pandas as pd
dataplat=pd.read_csv('dataplatfilms.csv', index_col=0)
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


#print(classifdisney("https://disneyplus.bn5x.net/c/1206980/705874/9358?u=https%3A%2F%2Fwww.disneyplus.com%2Fmovies%2Fthe-happening%2F2V6FKeZRE593&subId3=justappsvod"))

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