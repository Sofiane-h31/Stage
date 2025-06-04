import pandas as pd
import requests
import re
dataplat=pd.read_csv('dataplatfilms.csv', index_col=0)
probdef=[]
proburl=[]

def classifCanal(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    }

    site = requests.get(url, headers=headers)

    if site.status_code == 200:
        age=re.search(r'title="Moins de (\d{1,2}) ans"', site.text)
        return '-'+age.group(1)
    else:proburl.append(url)






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


