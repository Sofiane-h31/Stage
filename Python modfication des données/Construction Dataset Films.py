from simplejustwatchapi.justwatch import search
import pandas as pd
from imdb import IMDb
import numpy as np
'''
ttdonnees=pd.read_csv('../Datasets/data.csv', index_col=0)
films=ttdonnees[ttdonnees['type']=='movie']
topfilms = films.sort_values(by='numVotes', ascending=False)
dataseries=topfilms[0:1501]



dataseries['idjw']=np.nan
#nomseries= dataseries.apply(lambda lig: [(lig['title'], lig['releaseYear'])], axis=1).tolist()
nomseries= list(dataseries['title'])

nmp=[]
rtrv=[]
eta=0
jw={}
for i in nomseries:
  yest=False
  eta += 1
  print(f"{i}    {eta} / {len(nomseries)}")
  try:
    infos = search(i, "FR")
    for j in infos:
      if j.imdb_id==dataseries.index[eta-1]:
        print('trouvé')
        yest=True
        dataseries.loc[dataseries['title'] == i, 'idjw'] =j.entry_id
        break
    if yest==False:
      nmp.append((i, dataseries.index[eta-1]))

  except:
    rtrv.append((i))
    pass


print(f"\n{nmp}")
print(len(nmp), "\n")


print(rtrv)
print(len(rtrv))
dataseries=dataseries.dropna(subset=['idjw'])
dataseries.to_csv('films_justwatch.csv')




#------------------------------------------------------------------------------ Ajout de données ------------------------------------------------------------------

datasetseries=pd.read_csv('dataseries_justwatch.csv')

datasetseries = datasetseries.iloc[:, 1].tolist()
#print(datasetseries)

dataseries= pd.read_csv('imdb_top_5000_tv_shows.csv', usecols=['id', 'primaryTitle', 'genres', 'averageRating', 'numVotes', 'startYear'])

dataseries['idjw']=np.nan

dataseries=dataseries.sort_values(by='numVotes' , ascending=False)

#nomseries= dataseries.apply(lambda lig: [(lig['title'], lig['releaseYear'])], axis=1).tolist()
nomseries= list(dataseries['primaryTitle'])
#print(nomseries)
#print(dataseries)
objo=999
nmp=[]
rtrv=[]
eta=0
jw={}
i=-1
while objo<1000:
  i+=1
  yest=False
  eta += 1
  print(f"{nomseries[i]}    {objo-998} / {1000-998}    {eta} / {len(nomseries)}")
  try:
    infos = search(nomseries[i], "FR")
    for j in infos:
      if j.imdb_id==dataseries.iloc[eta-1]['id'] and j.imdb_id not in datasetseries:
        dataseries.loc[dataseries['primaryTitle'] == nomseries[i], 'idjw'] =j.entry_id
        objo+=1


  except:
    pass


print(f"\n{nmp}")
print(len(nmp), "\n")


print(rtrv)
print(len(rtrv))
dataseries=dataseries.dropna(subset=['idjw'])
dataseries.to_csv('jspart2.csv')





df = pd.read_csv('dataseries_justwatch.csv')

doublons = df['id'].duplicated()

print(df[doublons])



plat=IMDb()

data=pd.read_csv('dataplatfilms.csv', index_col=0)
dataserie=data[['id', 'title']].copy()
dataserie=dataserie.drop_duplicates(subset='id', keep='first')
print(len(dataserie))
dataserie['CodePays']=None
eta=1
probleme=[]
for i in dataserie['id']:
    print(f"{(dataserie.loc[dataserie['id']==i, 'title']).to_string()}    {eta} / {len(dataserie)}")
    try:
        serie=plat.get_movie(i[2:])
        dataserie.loc[dataserie['id'] == i, 'CodePays'] = str(serie['country codes'])[1:-1]
    except Exception as e:
        probleme.append((i, e))
    eta+=1


print(probleme)
print(len(probleme))

dataserie.to_csv('paystestfilms.csv')
'''
data=pd.read_csv('paystestfilms.csv')
dataseries=pd.read_csv('dataplatfilms.csv', index_col=0)
res=pd.merge(dataseries,data[['id','CodePays']], on='id')
res.to_csv('resfilms.csv')




