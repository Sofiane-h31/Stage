import pandas as pd
from simplejustwatchapi import *


datafilms=pd.read_csv('testfilms.csv', index_col=0)
idf=''
eta=0
prob=[]
datafilms['classifJW']=None
datafilms['Duree']=None
for k in datafilms.index:
    try:
        if idf!=datafilms.loc[k, 'id']:
            eta+=1
            idf=datafilms.loc[k, 'id']
            print(f"{datafilms.loc[k, 'title']}     {eta} / 1500")
            film=details(datafilms.loc[k, 'idjw'], "FR")
            datafilms.loc[k, 'Duree']=film.runtime_minutes
            datafilms.loc[k, 'classifJW']=film.age_certification
        else:
            datafilms.loc[k, 'Duree'] = film.runtime_minutes
            datafilms.loc[k, 'classifJW'] = film.age_certification
    except Exception as e:
        prob.append((datafilms.loc[k, 'title'], e))
datafilms.to_csv('datafilms_03-07.csv')
print(prob)
print(len(prob))
#nmp=[('Joker', ConnectTimeout('_ssl.c:993: The handshake operation timed out')), ('Slumdog Millionaire', ConnectTimeout('timed out')), ('Spider-Man: Homecoming', ConnectTimeout('timed out')), ('Fargo', ConnectTimeout('timed out')), ('Kingsman: The Secret Service', ConnectTimeout('timed out')), ('Ant-Man', ConnectTimeout('timed out')), ('X-Men: First Class', ConnectTimeout('timed out')), ('Million Dollar Baby', ConnectTimeout('timed out')), ('District 9', ConnectTimeout('timed out')), ('The Amazing Spider-Man', ConnectTimeout('timed out')), ('The Curious Case of Benjamin Button', ConnectTimeout('timed out')), ('Wonder Woman', ConnectTimeout('timed out')), ('Groundhog Day', ConnectTimeout('timed out')), ('Blade Runner 2049', ConnectTimeout('timed out')), ('Home Alone', ConnectTimeout('timed out')), ('Prometheus', ConnectTimeout('timed out')), ('X-Men', ConnectTimeout('timed out')), ('Cast Away', ConnectTimeout('timed out')), ('Argo', ConnectTimeout('timed out')), ('Zombieland', ConnectTimeout('timed out')), ('It', ConnectTimeout('timed out')), ('Nightcrawler', ConnectTimeout('timed out')), ('Limitless', ConnectTimeout('timed out')), ('A Quiet Place', ConnectTimeout('timed out')), ('The Great Gatsby', ConnectTimeout('timed out')), ('Despicable Me', ConnectTimeout('timed out')), ('Back to the Future Part II', ConnectTimeout('timed out')), ('X2: X-Men United', ConnectTimeout('timed out')), ('Crazy, Stupid, Love.', ConnectTimeout('timed out')), ('Dead Poets Society', ConnectTimeout('timed out')), ('Three Billboards Outside Ebbing, Missouri', ConnectTimeout('timed out')), ('Predator', ConnectTimeout('timed out')), ('Ant-Man and the Wasp', ConnectTimeout('timed out')), ('The Menu', ConnectTimeout('timed out')), ('The Machinist', ConnectTimeout('timed out')), ('Moana', ConnectTimeout('timed out')), ('Beetlejuice', ConnectTimeout('timed out')), ('The Lego Movie', ConnectTimeout('timed out')), ('The Italian Job', ConnectTimeout('timed out')), ('The Illusionist', ConnectTimeout('timed out')), ('The Nightmare Before Christmas', ConnectTimeout('timed out')), ('The Aviator', ConnectTimeout('timed out')), ('Pearl Harbor', ReadTimeout('The read operation timed out')), ('War for the Planet of the Apes', ConnectTimeout('timed out')), ('The Platform', ConnectTimeout('timed out')), ('Terminator Genisys', ConnectTimeout('timed out')), ('Hotel Transylvania', ConnectTimeout('timed out')), ('The Matrix Resurrections', ConnectTimeout('timed out')), ('Meet Joe Black', ConnectTimeout('timed out')), ('Alien Resurrection', ConnectTimeout('timed out')), ('Chronicle', ConnectTimeout('timed out')), ('Pitch Black', ConnectTimeout('timed out')), ('Mars Attacks!', ConnectTimeout('timed out')), ('Fast & Furious Presents: Hobbs & Shaw', ConnectTimeout('timed out')), ('Miss Congeniality', ConnectTimeout('timed out')), ('Mad Max', ConnectTimeout('timed out')), ('EuroTrip', ConnectTimeout('timed out')), ('A Good Day to Die Hard', ConnectTimeout('timed out')), ('Waterworld', ConnectTimeout('timed out')), ('The Next Three Days', ConnectTimeout('timed out')), ('PK', ConnectTimeout('timed out')), ('Bright', ConnectTimeout('timed out')), ('The Girl on the Train', ConnectTimeout('timed out')), ('Poltergeist', ConnectTimeout('timed out')), ('Surrogates', ConnectTimeout('timed out')), ('The Rocky Horror Picture Show', ConnectTimeout('timed out')), ('Wall Street', ConnectTimeout('timed out')), ('Past Lives', ConnectTimeout('timed out')), ('Still Alice', ConnectTimeout('timed out')), ('The Jacket', ConnectTimeout('timed out')), ('A Silent Voice: The Movie', ConnectTimeout('timed out')), ('Frost/Nixon', ConnectTimeout('timed out')), ('Attack the Block', ConnectTimeout('timed out'))]


