import pandas as pd
import numpy as np
import requests
import re


dataplat=pd.read_csv('platfilms.csv', index_col=0)
dataplat['ClassificationSVOD']=None

probdef = []


def classifnetflix(url):
    url = url[:24] + 'fr/' + url[24:]
    serie = False  # Modifier pour les films

    headers = {
        'Accept-Encoding': 'identity'
    }

    site = requests.get(url, headers=headers)

    html = site.text
    # print(html)
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
