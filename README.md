# Notebook
J'utilise Google Colab pour la plupart des tâches. Je vous joins donc un lien vers ce dernier (vous y avez ainsi accès en temps réel):
https://colab.research.google.com/drive/1UhJ15bjE1Mob_ZzN5uFZomTqPAj6DB6b?usp=sharing


# Code Pycharm
Documentation IMDbPY :
https://imdbpy.readthedocs.io/_/downloads/en/stable/pdf/

Documentation SimpleJustWatchAPI :
https://electronic-mango.github.io/simple-justwatch-python-api/

Pour le web scraping sur Paramount+, la requête XHR provient directement du site :
![image](https://github.com/user-attachments/assets/98436ac1-cbd5-4e3e-ae87-7e1358e1f3c6)
NB: Les éléments d’en-tête (headers) sont indiqués en bas de la page, dans la section "Request Headers"

Pour Apple TV, la méthode est quasiment identique, à la différence près que la requête XHR contient des paramètres:
![image](https://github.com/user-attachments/assets/a70db78a-6212-48bd-8def-81145063ff40)
NB: Les éléments d’en-tête (headers) sont indiqués en bas de la page, dans la section "Request Headers"

Pour les autres plateformes, ne disposant pas de requêtes XHR, les en-têtes User-Agent du document HTML sont suffisants :
![image](https://github.com/user-attachments/assets/7f7d5727-d448-4940-8dd1-19c78cbea32f)


