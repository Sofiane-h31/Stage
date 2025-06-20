import pandas as pd
import requests
import re

from scipy.stats import probplot

datafilms=pd.read_csv('resfilmsCNC.csv', index_col=0)
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'
}
datafilms.insert(13, 'classifCNC', [None]*len(datafilms))
def agecnc(visa):
    site=requests.get(f"https://www.cnc.fr/professionnels/visas-et-classification/{visa}", headers=headers)
    age=re.search(r'<div class="th">Mention</div>\s+<div class="td">([^<]+)</div>', site.text)
    return age.group(1)

print(agecnc(99168))
idf=''
prob=[]
eta=0
for k in datafilms.index:
    if datafilms.loc[k, 'visaCNC']=='-':
        datafilms.loc[k, 'classifCNC']='-'
    else:
        if idf!=datafilms.loc[k, 'id']:
            eta+=1
            print(f"{datafilms.loc[k, 'title']}     {eta} / 1500")
            idf=datafilms.loc[k, 'id']
            if ' ' in str(datafilms.loc[k, 'visaCNC']):
                datafilms.loc[k, 'visaCNC']=int(str(datafilms.loc[k, 'visaCNC']).replace(' ',''))
            try:
                res=agecnc(datafilms.loc[k, 'visaCNC'])
                datafilms.loc[k, 'classifCNC'] = res
            except Exception as e:
                prob.append((datafilms.loc[k, 'title'], e))
        else:
            datafilms.loc[k, 'classifCNC']=res

print(prob)
print(len(prob))

datafilms.to_csv('testagecnc.csv')

