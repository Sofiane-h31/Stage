from simplejustwatchapi.justwatch import *
import pandas as pd
import numpy as np
'''
data=pd.read_csv('seriejustwatch+providers.csv', index_col=False)
idsjs=list(data['idjw'])
probleme=[('The Office', 'tt0290978', 'tt0386676', 'ts21621'), ('Suits', 'tt1967681', 'tt1632701', 'ts22277'), ('ONE PIECE', 'tt11737520', 'tt0388629', 'ts255424'), ('The X-Files', 'tt4370492', 'tt0106179', 'ts20974'), ('Doctor Who', 'tt31433814', 'tt0436992', 'ts422861'), ('Twin Peaks: The Return', 'tt4093826', 'tt0098936', 'ts86729'), ('Gossip Girl', 'tt10653784', 'tt0397442', 'ts288382'), ('The Penguin', 'tt15494650', 'tt15435876', 'ts341776'), ('Battlestar Galactica', 'tt0314979', 'tt0407362', 'ts56662'), ('ONE PIECE', 'tt11737520', 'tt0388629', 'ts255424'), ('Cowboy Bebop', 'tt1267295', 'tt0213338', 'ts85985'), ('The Office', 'tt0290978', 'tt0386676', 'ts21621'), ('Frasier', 'tt14124236', 'tt0106004', 'ts407546'), ('Secret Invasion', 'tt13158566', 'tt13157618', 'ts269540'), ('Twin Peaks: The Return', 'tt4093826', 'tt0098936', 'ts86729'), ('Battlestar Galactica', 'tt0314979', 'tt0407362', 'ts56662'), ('The Bridge', 'tt2406376', 'tt1733785', 'ts15770'), ('Dark Matter', 'tt4159076', 'tt19231492', 'ts35253'), ('Kingdom', 'tt3673794', 'tt6611916', 'ts20749'), ('Dark Matter', 'tt4159076', 'tt19231492', 'ts35253'), ('Cowboy Bebop', 'tt1267295', 'tt0213338', 'ts85985'), ('S.W.A.T.', 'tt6594670', 'tt6111130', 'ts304703'), ('The Staircase', 'tt0388644', 'tt11324406', 'ts26091'), ('DuckTales', 'tt5531466', 'tt0092345', 'ts57862'), ('The Staircase', 'tt0388644', 'tt11324406', 'ts26091'), ('Being Human', 'tt1349938', 'tt1595680', 'ts11224'), ('Being Human', 'tt1349938', 'tt1595680', 'ts11224'), ('Doctor Who', 'tt31433814', 'tt0436992', 'ts422861'), ('The Smurfs', 'tt29883471', 'tt0081933', 'ts35721'), ('The Bridge', 'tt2406376', 'tt1733785', 'ts15770'), ('Doug', 'tt0122815', 'tt0101084', 'ts6600'), ('Kingdom', 'tt3673794', 'tt6611916', 'ts20749'), ('Shaun the Sheep', 'tt9253298', 'tt0983983', 'ts33559'), ('Gossip Girl', 'tt10653784', 'tt0397442', 'ts288382'), ('DuckTales', 'tt5531466', 'tt0092345', 'ts57862'), ('Frasier', 'tt14124236', 'tt0106004', 'ts407546')]
eta=0
for i in probleme:
    print(f"{eta} / {len(probleme)}")
    serie=details(i[3])
    data.loc[data['idjw']==i[3], 'id']=serie.imdb_id
    eta+=1


data.to_csv('series+provMAJ.csv')

'''





'''
probleme=[]
eta=0
prob=0
for i in idsjs:
    try:
        print(f"{eta} / {len(idsjs)}    Problèmes:{prob}")
        serie=details(i, country="FR")
        if data[data['idjw']==i].index[0] != serie.imdb_id:
            probleme.append((serie.title, serie.imdb_id, data[data['idjw']==i].index[0], i)) #titre, idAPI, idDataset, idJW
            prob+=1
        eta+=1
    except Exception as e:
        print(f'---------------------Erreur {e} idJW :{i}------------------------------------')
print(probleme)
print(len(probleme))
'''
