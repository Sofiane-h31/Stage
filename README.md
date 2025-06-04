# Stage

Documentation IMDbPY :
https://imdbpy.readthedocs.io/_/downloads/en/stable/pdf/

Documentation SimpleJustWatchAPI :
https://electronic-mango.github.io/simple-justwatch-python-api/

Pour le WebScraping sur Paramount+, la requête XHR est issue du site directement :
![image](https://github.com/user-attachments/assets/98436ac1-cbd5-4e3e-ae87-7e1358e1f3c6)
Nb : Les élements d'entêtes (headers) sont indiquées en bas de la page (section "Request Headers")

Pour AppleTV la méthode est quasiment similaire, au détail près que la requête XHR dispose de paramètres
![image](https://github.com/user-attachments/assets/a70db78a-6212-48bd-8def-81145063ff40)
Nb : Les élements d'entêtes (headers) sont indiquées en bas de la page (section "Request Headers")


Les autres plateformes ne disposant pas de requêtes XHR, les entêtes de User-Agent du document HTML sont suffisantes :
![image](https://github.com/user-attachments/assets/7f7d5727-d448-4940-8dd1-19c78cbea32f)


