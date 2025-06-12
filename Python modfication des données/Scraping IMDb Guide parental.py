import pandas as pd
import requests
import re
dataseries=pd.read_csv('resseriesvecteur.csv', index_col=0)
valparent=[None]*len(dataseries)
dataseries.insert(12, 'ValNudite', valparent)
dataseries.insert(13, 'ValViolence', valparent)
dataseries.insert(14, 'ValVulgarite', valparent)
dataseries.insert(15, 'ValStupefiants', valparent)
dataseries.insert(16, 'ValIntensite', valparent)

def parental(url):
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'
    }
    site=requests.get(url, headers=headers)
    #print(site.text)
    elemparent=re.findall(r'"text":"([^"]+)","__typename":"ParentsGuideCategory"},"severity":\{"id":".+?","text":"([^"]+)","votedFor":([^,]+),"__typename":"SeverityLevel"},"totalSeverityVotes":([^,]+)', site.text)
    return elemparent

print(parental('https://www.imdb.com/fr/title/tt0903747/parentalguide/?ref_=tt_stry_pg'))
prob=[]
idSer=''
eta=0
for h in dataseries.index[:20]:
    try:
        if dataseries.loc[h, 'id']!=idSer:
            eta += 1
            print(f"{dataseries.loc[h, 'title']}    {eta} / 1500" )
            idSer=dataseries.loc[h, 'id']
            res=parental(f"https://www.imdb.com/fr/title/{idSer}/parentalguide/?ref_=tt_stry_pg")
        for k in res:
            if 'nudité' in k[0]:
                dataseries.loc[h, 'ValNudite']=f"{k[1]}:{round(int(k[2])/int(k[3])*100, 2)}%"
            if 'horreur' in k[0]:
                dataseries.loc[h, 'ValViolence']=f"{k[1]}:{round(int(k[2])/int(k[3])*100, 2)}%"
            if 'vulgaires' in k[0]:
                dataseries.loc[h, 'ValVulgarite']=f"{k[1]}:{round(int(k[2])/int(k[3])*100, 2)}%"
            if 'tabagisme' in k[0]:
                dataseries.loc[h, 'ValStupefiants']=f"{k[1]}:{round(int(k[2])/int(k[3])*100, 2)}%"
            if 'intensité' in k[0]:
                dataseries.loc[h, 'ValIntensite']=f"{k[1]}:{round(int(k[2])/int(k[3])*100, 2)}%"
    except Exception as e:
        prob.append((h, dataseries.loc[h, 'id'], e))

print(prob)
print(len(prob))

dataseries.to_csv('dataseriesParental.csv')