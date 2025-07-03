import ollama
import pandas as pd
import re
import requests
import concurrent.futures
import threading  # Pour gérer le verrou

# Charger les données
dataseries = pd.read_csv('dataseriesParental.csv', index_col=0)
dataseries['ScoreParental'] = None

# Variables globales
ids = ''
eta = 0
prob = []

# Créer un verrou pour l'accès aux variables globales
lock = threading.Lock()

# Fonction pour interagir avec Ollama
def motscles(ids):
    site = requests.get(f'https://www.imdb.com/fr/title/{ids}/keywords/', headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"}).text

    listemc = re.findall(r'ref_=ttkw_kw_\d+">(.+?)</a>', site)
    mots = ','.join(listemc)
    response = ollama.chat(model="gemma3", messages=[  # Assurez-vous que le modèle est correct
        {"role": "system", "content": "Tu dois analyser les listes et retourner une moyenne sur 100 du contenu explicite, incluant la violence, la nudité, la drogue, etc. Ne retourne que le score (le nombre)."},
        {"role": "user", "content": f"Voici la nouvelle liste de mots-clés : {mots}\nRetourne uniquement le score moyen sur 100."}
    ])
    return response['message']['content']

# Fonction pour mettre à jour le score pour chaque film
def update_score(k):
    global ids, eta  # Utilisation des variables globales
    try:
        with lock:  # Verrouiller l'accès aux variables globales
            if ids != dataseries.loc[k, 'id']:
                eta += 1
                ids = dataseries.loc[k, 'id']
                res = motscles(ids)  # Appel à Ollama pour récupérer le score
                dataseries.loc[k, 'ScoreParental'] = res
                print(f"{dataseries.loc[k, 'title']} : {res}    {eta} / 1500")
            else:
                dataseries.loc[k, 'ScoreParental'] = res
    except Exception as e:
        prob.append((dataseries.loc[k, 'title'], e))  # Enregistrer les erreurs

# Utiliser ThreadPoolExecutor pour exécuter les requêtes en parallèle
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(update_score, dataseries.index)

# Si des erreurs ont été enregistrées, les afficher
if prob:
    print("Erreurs rencontrées :")
    for title, error in prob:
        print(f"{title}: {error}")
