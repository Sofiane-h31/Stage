from pandas import read_csv
from simplejustwatchapi.justwatch import *
import pandas as pd
import numpy as np
from imdb import IMDb

'''

ttdonnees=pd.read_csv('../Datasets/data.csv', index_col=0)
series=ttdonnees[ttdonnees['type'].isin(['movie'])]
topseries = series.sort_values(by='numVotes', ascending=False)
dataseries=topseries



dataseries['idjw']=np.nan
#nomseries= dataseries.apply(lambda lig: [(lig['title'], lig['releaseYear'])], axis=1).tolist()
nomseries= list(dataseries['title'])
nmp=[]
rtrv=[]
eta=0
jw={}
eff=0
i=-1
dataseries['NbDiff']=np.nan
dataseries['Diffuseur(s)']=None
pasdediff=[]
for i in nomseries:
  yest=False
  eta += 1
  print(f"{i}    {eta} / {len(nomseries)}       {eff+1}/1500")
  prov=set()
  try:
    infos = search(i, "FR", count=30)
    for j in infos:
      if j.imdb_id==dataseries.index[eta-1] and len(j.offers)>0:
        yest=True
        for k in j.offers:            
          if k.monetization_type=='FLATRATE':
            if k.url=='https://tv.apple.com' :
              for h in j.offers:
                if h.monetization_type!='FLATRATE' and 'https://tv.apple.com' in h.url:
                  prov.add(h.url)
            else:
              if k.url[:26]!='https://www.canalplus.com/':
                prov.add(k.url)
        nbprov=len(list(prov))
        if nbprov!=0:
          dataseries.loc[dataseries['title'] == i, 'idjw'] = j.entry_id
          dataseries.at[dataseries.index[eta - 1], 'Diffuseur(s)'] = list(prov)
          dataseries.loc[dataseries['title'] == i, 'NbDiff'] = nbprov
          eff += 1
        else:
          pasdediff.append((i, dataseries.index[eta-1]))


        break
    if yest==False:
      nmp.append((i, dataseries.index[eta-1]))


  except Exception as e:
    print(e)

    rtrv.append(i)
    pass
  if eff==1500:
    break


print(f"\n{nmp}")
print(len(nmp), "\n")


print(pasdediff)
print(len(pasdediff))
dataseries=dataseries.dropna(subset=['idjw', 'Diffuseur(s)'])
dataseries.to_csv('filmsjustwatch+providers.csv')










ttdonnees=pd.read_csv('../Datasets/data.csv', index_col=0)
ancdonnes=pd.read_csv('../Datasets/dataseries_justwatch.csv', index_col=0)
series=ttdonnees[ttdonnees['type'].isin(['movie'])]
topseries = series.sort_values(by='numVotes', ascending=False)
dataseries=topseries


dataseries['idjw']=np.nan
#nomseries= dataseries.apply(lambda lig: [(lig['title'], lig['releaseYear'])], axis=1).tolist()
#nomseries= list(dataseries['title'])
nomseries=[]
nomseries=[('Pirates of the Caribbean: The Curse of the Black Pearl', 'tt0325980'), ('Harry Potter and the Deathly Hallows: Part 2', 'tt1201607'), ('Apocalypse Now', 'tt0078788'), ('The Kashmir Files', 'tt10811166'), ('The Fifth Element', 'tt0119116'), ('3 Idiots', 'tt1187043'), ('Wedding Crashers', 'tt0396269'), ('Hotel Rwanda', 'tt0395169'), ('How to Train Your Dragon 2', 'tt1646971'), ('Elf', 'tt0319343'), ('Crouching Tiger, Hidden Dragon', 'tt0190332'), ('Blow', 'tt0221027'), ('Austin Powers: International Man of Mystery', 'tt0118655'), ('The Boondock Saints', 'tt0144117'), ('Civil War', 'tt17279496'), ('Cowboys & Aliens', 'tt0409847'), ('Dogma', 'tt0120655'), ('A Walk to Remember', 'tt0281358'), ('Dangal', 'tt5074352'), ('Jai Bhim', 'tt15097216'), ('Girl, Interrupted', 'tt0172493'), ('The Happening', 'tt0949731'), ('Merge into Girl, Interrupted', 'tt30798231'), ('Like Stars on Earth', 'tt0986264'), ('Spaceballs', 'tt0094012'), ('Harold & Kumar Go to White Castle', 'tt0366551'), ('Adaptation.', 'tt0268126'), ('Grindhouse', 'tt0462322'), ('Hero', 'tt0299977'), ("She's the Man", 'tt0454945'), ('Radhe', 'tt10888594'), ('The Running Man', 'tt0093894'), ('Napoleon', 'tt13287846'), ('A Bronx Tale', 'tt0106489'), ('Godzilla Minus One', 'tt23289160'), ('The Wedding Singer', 'tt0120888'), ('K.G.F: Chapter 2', 'tt10698680'), ('I Am Sam', 'tt0277027'), ('The Texas Chainsaw Massacre', 'tt0324216'), ('Irreversible', 'tt0290673'), ('The Count of Monte Cristo', 'tt0245844'), ('A Quiet Place: Day One', 'tt13433802'), ('This Is Spinal Tap', 'tt0088258'), ('Stalker', 'tt0079944'), ('Bowling for Columbine', 'tt0310793'), ('John Q', 'tt0251160'), ('My Big Fat Greek Wedding', 'tt0259446'), ('Snakes on a Plane', 'tt0417148'), ('The Recruit', 'tt0292506'), ('Harold & Kumar Escape from Guantanamo Bay', 'tt0481536'), ('Hairspray', 'tt0427327'), ('Pleasantville', 'tt0120789'), ('Shanghai Noon', 'tt0184894'), ('Dil Bechara', 'tt8110330'), ('Carnage', 'tt1692486'), ('The Phantom of the Opera', 'tt0293508'), ('Shershaah', 'tt10295212'), ('Just Friends', 'tt0433400'), ('Freddy vs. Jason', 'tt0329101'), ('Friday', 'tt0113118'), ('Alice Through the Looking Glass', 'tt2567026'), ('Soorarai Pottru', 'tt10189514'), ('The Basketball Diaries', 'tt0112461'), ('Rat Race', 'tt0250687'), ('Death at a Funeral', 'tt0795368'), ('Rang De Basanti', 'tt0405508'), ('The Invitation', 'tt2400463'), ('Lagaan: Once Upon a Time in India', 'tt0169102'), ('Glengarry Glen Ross', 'tt0104348'), ('Fast Times at Ridgemont High', 'tt0083929'), ('Crocodile Dundee', 'tt0090555'), ('Cocaine Bear', 'tt14209916'), ('Frequency', 'tt0186151'), ('Little Children', 'tt0404203'), ('Bend It Like Beckham', 'tt0286499'), ('Van Wilder', 'tt0283111'), ('Primer', 'tt0390384'), ('House of Flying Daggers', 'tt0385004'), ('Tenacious D in the Pick of Destiny', 'tt0365830'), ('Little Nicky', 'tt0185431'), ('Hit Man', 'tt20215968'), ('Shanghai Knights', 'tt0300471'), ('Brahmastra Part One: Shiva', 'tt6277462'), ('August Rush', 'tt0426931'), ('Notorious', 'tt0038787'), ('American Fiction', 'tt23561236'), ('Captain America: Brave New World', 'tt14513804'), ('Alpha Dog', 'tt0426883'), ('Waiting...', 'tt0348333'), ('Andhadhun', 'tt8108198')]
nmp=[]
rtrv=[]
eta=0
jw={}
eff=0
i=-1
dataseries['NbDiff']=np.nan
dataseries['Diffuseur(s)']=None
pasdediff=[]
for ser in nomseries:
  i=ser[0]
  yest=False
  eta += 1
  print(f"{i}    {eta} / {len(nomseries)}       {eff+1}/1500")
  prov=set()
  try:
    infos = search(i, "FR", count=30)
    for j in infos:
      if j.scoring.imdb_score==dataseries.loc[ser[1], 'averageRating'] and j.release_year==dataseries.loc[ser[1], 'releaseYear']:
        yest=True
        if len(j.offers)==0:
          pasdediff.append((i, ser[1]))
          break
        for k in j.offers:
          if k.monetization_type=='FLATRATE':
            if k.url=='https://tv.apple.com':
              for h in j.offers:
                if h.monetization_type!='FLATRATE' and 'https://tv.apple.com' in h.url:
                  prov.add(h.url)
            else:
              if k.url[:26]!='https://www.canalplus.com/':
                prov.add(k.url)
        nbprov=len(list(prov))
        if nbprov!=0:
          dataseries.loc[dataseries['title'] == i, 'idjw'] = j.entry_id
          dataseries.at[ser[1], 'Diffuseur(s)'] = list(prov)
          dataseries.loc[dataseries['title'] == i, 'NbDiff'] = nbprov
          eff += 1
        else:
          pasdediff.append((i, dataseries.index[eta-1]))


        break
    if yest==False:
      nmp.append((i, ser[1]))


  except Exception as e:
    print("Erreur",e)

    rtrv.append(i)
    pass
  if eff==1500:
    break


print(f"\n{nmp}")
print(len(nmp), "\n")


print(pasdediff)
print(len(pasdediff))

print("NbErr critiques : ",len(rtrv))
datasample=dataseries.dropna(subset=['idjw', 'Diffuseur(s)'])
datasample.to_csv('retardatairesfilms.csv')


df=read_csv('platseries.csv', index_col=0)
df.drop('Diffuseur(s)', axis=1)
df.to_csv('platseriescomp.csv')

plat=IMDb()

data=pd.read_csv('dataplatseries.csv', index_col=0)
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

dataserie.to_csv('paystestseries.csv')

data=pd.read_csv('paystestseries.csv')
dataseries=read_csv('dataplatseries.csv', index_col=0)
res=pd.merge(dataseries,data[['id','CodePays']], on='id')
res.to_csv('resseries.csv')
'''
data=pd.read_csv('paystestseries.csv')


