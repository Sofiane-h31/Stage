import requests
import re
from imdb import IMDb
import pandas as pd
import numpy as np
#Classif IMDb
'''
plat=IMDb()
dataseries=pd.read_csv('filmsproviders.csv')
dataseries['ClassifImdb']=None
nmp=[]
pasdeclass=[]
eta=0
for i in dataseries['id']:
    eta+=1
    print(f"{eta} / {len(dataseries['id'])}")
    yest=False
    try:
        oeuvre=plat.get_movie(i[2:])
        for j in oeuvre['certificates']:
            j=j.lower()
            if 'france' in j:
                yest=True
                j=j.replace('france:','').strip()
                dataseries.loc[dataseries['id']==i, 'ClassifImdb']=j
                break
        if yest==False:
            pasdeclass.append(i)
    except:
        nmp.append(i)
print(dataseries)

dataseries.to_csv('filmsclassifIMDB.csv')

print(nmp)
print(len(nmp))
#['tt14533970']

print(pasdeclass)
print(len(pasdeclass))
#Series
#['tt12637874', 'tt2788316', 'tt31806037', 'tt13649112', 'tt11737520', 'tt13210838', 'tt9813792', 'tt1628033', 'tt13622776', 'tt15567174', 'tt14954666', 'tt2934286', 'tt16358384', 'tt24053860', 'tt13309742', 'tt33503491', 'tt0314979', 'tt0115167', 'tt9018736', 'tt15571732', 'tt21209876', 'tt13111078', 'tt24069848', 'tt5611024', 'tt11514868', 'tt18347622', 'tt27995113', 'tt18923754', 'tt1344204', 'tt11117570', 'tt11016042', 'tt26933824', 'tt16283804', 'tt19768024', 'tt5622316', 'tt1610527', 'tt14186672', 'tt10466872', 'tt2887954', 'tt0103584', 'tt14044212', 'tt22074164', 'tt17220216', 'tt0105958', 'tt23872886', 'tt15837600', 'tt11000902', 'tt0363328', 'tt16026746', 'tt13966962', 'tt1195935', 'tt2297757', 'tt8550732', 'tt1519931', 'tt27444205', 'tt9859436', 'tt12324366', 'tt22248376', 'tt11379026', 'tt7472896', 'tt0101188', 'tt16418808', 'tt14524712', 'tt0472027', 'tt20600980', 'tt32252772', 'tt1255913', 'tt16288804', 'tt8740614', 'tt30003786', 'tt9425132', 'tt15574312', 'tt26670955', 'tt13062500', 'tt1986770', 'tt3960394', 'tt8342862', 'tt2262532', 'tt20863760', 'tt7216636', 'tt13138834', 'tt15227418', 'tt14482414', 'tt13406036', 'tt15204292', 'tt22091076', 'tt17632862', 'tt9184820', 'tt0388644', 'tt0297494', 'tt6040674', 'tt16296870', 'tt33204697', 'tt11794812', 'tt6792200', 'tt8226360', 'tt15203646', 'tt0135659', 'tt15222080', 'tt3155320', 'tt0421030', 'tt0883772', 'tt0948103', 'tt0098878', 'tt2244495', 'tt28106741', 'tt14674086', 'tt18075020', 'tt22797582', 'tt11097240', 'tt0300865', 'tt30317229', 'tt0366005', 'tt28267514', 'tt13875494', 'tt0346314', 'tt14833612', 'tt12074628', 'tt12197698', 'tt27668559', 'tt11083696', 'tt6478318', 'tt15716776', 'tt21975436', 'tt1279024', 'tt15358446', 'tt2406376', 'tt16969708', 'tt0279077', 'tt10569934', 'tt10399902', 'tt19395018', 'tt13911284', 'tt28104766', 'tt11379456', 'tt3431758', 'tt1660055', 'tt14263564', 'tt11475228', 'tt31019484', 'tt27740241', 'tt21072112', 'tt0310455', 'tt3696720', 'tt13103134', 'tt28118211', 'tt16283758', 'tt11471892', 'tt8685324', 'tt26225038', 'tt17524566', 'tt0839188', 'tt5497534', 'tt6474236', 'tt0101076', 'tt26545355', 'tt8323628', 'tt1640719', 'tt7263328', 'tt1943524', 'tt3469052', 'tt27792190', 'tt8403664', 'tt17513352', 'tt5370118', 'tt0787985', 'tt4295140', 'tt26676489', 'tt13024830', 'tt0106079', 'tt30423279', 'tt0185133', 'tt14879018', 'tt1626038', 'tt26737616', 'tt2543796', 'tt1913273', 'tt22780536', 'tt19891306', 'tt11691684', 'tt0429087', 'tt14466018', 'tt11899030', 'tt7865090', 'tt15428778', 'tt0098924', 'tt29485149', 'tt0403778', 'tt30826447', 'tt9892936', 'tt0985344', 'tt1799631', 'tt5797194', 'tt29135600', 'tt1370334', 'tt5182866', 'tt29569035', 'tt11165002', 'tt1173427', 'tt0280277', 'tt1186356', 'tt28256288', 'tt1214085', 'tt3613454', 'tt13623608', 'tt0433722', 'tt15439048', 'tt31812476', 'tt0983514', 'tt15384586', 'tt20234568', 'tt6157148', 'tt17720272', 'tt3243098', 'tt21057450', 'tt15845610', 'tt14681596', 'tt18926162', 'tt22352854', 'tt6494622', 'tt21874396', 'tt23649128', 'tt0350448', 'tt0145628', 'tt11822998', 'tt20285780', 'tt9174718', 'tt16098700', 'tt21906238', 'tt9307686', 'tt1830491', 'tt15399640', 'tt0120570', 'tt32019314', 'tt26591110', 'tt6560040', 'tt18970124', 'tt10975574', 'tt21375036', 'tt2378794', 'tt13409432', 'tt2314952', 'tt0481256', 'tt26743760', 'tt18228732', 'tt24640580', 'tt16027074', 'tt14167390', 'tt1832045', 'tt11897688', 'tt1252374', 'tt30428143', 'tt23037654', 'tt2802008', 'tt11525188', 'tt8213522', 'tt27494999', 'tt6354518', 'tt13400006', 'tt2391224', 'tt11947418', 'tt5514358', 'tt0315008', 'tt5396394', 'tt6112414', 'tt0816397', 'tt3516878', 'tt8888540', 'tt9103932', 'tt4284216', 'tt0088528', 'tt15471900', 'tt2492296', 'tt21030032', 'tt8069036', 'tt21088136', 'tt21209804', 'tt14271652', 'tt14832996', 'tt14153236', 'tt10837476', 'tt5884792', 'tt0161952', 'tt8690728', 'tt14452228', 'tt8230448', 'tt23221806', 'tt5197860', 'tt9764386', 'tt31122777', 'tt0489598', 'tt3507484', 'tt6256484', 'tt15426714', 'tt14582876', 'tt6112556', 'tt2229907', 'tt12879418', 'tt15483276', 'tt23664162', 'tt19072562', 'tt31183656', 'tt3487410', 'tt25811262', 'tt6824234', 'tt12063450', 'tt1178522', 'tt5097050', 'tt5966882', 'tt5839454', 'tt2794380', 'tt31491435', 'tt35257773', 'tt3069212', 'tt2703720', 'tt11307176', 'tt1319900', 'tt14115938', 'tt18070898', 'tt12887536', 'tt10266874', 'tt21621494', 'tt14371926', 'tt13643704', 'tt28093628', 'tt27838483', 'tt14124236', 'tt31186958', 'tt4580372', 'tt9704568', 'tt27031263', 'tt8773420', 'tt21831910', 'tt33301469', 'tt8515016', 'tt35590630', 'tt10731032', 'tt0337792', 'tt15435876', 'tt26748649', 'tt6205862', 'tt14160712']

#Films
#['tt17351924', 'tt0356150', 'tt12747748', 'tt4873118', 'tt16419074', 'tt3359350', 'tt4698684', 'tt23849204', 'tt5177120', 'tt14998742', 'tt12915716', 'tt13654226', 'tt0351977', 'tt0401383', 'tt2170593', 'tt13452446']
'''
#Classif générique

import pandas as pd
import numpy as np
import requests
import re


dataplat=pd.read_csv('dataplatseries.csv', index_col=0)
probdef=[]
proburl=[]
def classifGen(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    } #En-tetes à modifier pour chaque plateforme

    site = requests.get(url, headers=headers)

    if site.status_code == 200:
        age=re.search(r'title="Moins de (\d{1,2}) ans"', site.text)  #Regex a modifier pour chaque plateforme
        return age.group(1)
    else:proburl.append(url)



eta = 0
for i in dataplat['Diffuseur']:
    print((dataplat.loc[dataplat['Diffuseur']==i, 'title']).to_string(), '     ', eta, '/ 299')
    if 'canal' in i: #'canal' ici mais mettre le nom de la plateforme
        try:
            dataplat.loc[dataplat['Diffuseur'] == i, 'ClassificationSVOD'] = classifGen(i)
        except Exception as e:
            probdef.append((i, e))
        eta += 1

print(probdef)
print(len(probdef))

print(proburl)
print(len(proburl))
dataplat.to_csv('dataplatTest.csv')









