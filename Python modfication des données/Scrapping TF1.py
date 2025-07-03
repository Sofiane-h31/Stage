import numpy as np
from simplejustwatchapi import *
import pandas as pd
'''
dataseries=pd.read_csv('../../dataseries_30-06.csv', index_col=0)
ajouter=[]
prov=set()
eta=0
prob=[]
for k in dataseries.index:
    try:
        eta+=1
        print(f"{eta} / {len(dataseries)}")
        ser=details(dataseries.loc[k, 'idjw'], country='FR')
        for offre in ser.offers:
            if offre.monetization_type=='ADS':
                nouvelle_l={'Diffuseur': offre.url, 'SVOD': offre.package.name}
                prov.add(offre.package.name)
                for col in dataseries.columns:
                    if col not in nouvelle_l:
                        nouvelle_l[col]=dataseries.loc[k, col]
                ajouter.append(nouvelle_l)
    except Exception as e:
        prob.append((dataseries.loc[k, 'title'], e))
dfinter=pd.DataFrame(ajouter)
dataseries=pd.concat([dataseries, dfinter], ignore_index=True)

print(prov)
print(prob)
dataseries.to_csv('seriesgratuit.csv')

'''

dataseries=pd.read_csv('dataseries_01-07.csv', index_col=0)

print(dataseries[dataseries.duplicated(subset='Diffuseur')])
