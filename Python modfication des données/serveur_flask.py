from flask import Flask, jsonify, request
import threading
import requests
import time

# Crée l'application Flask
app = Flask(__name__)

# Route qui accepte les méthodes GET et POST
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Si c'est une requête POST, on traite les données
        data = request.get_json()  # On récupère les données JSON envoyées avec la requête POST
        return jsonify(message="Data received", received_data=data)
    else:
        # Si c'est une requête GET, on renvoie un message par défaut
        return jsonify(message="Hello from the server!")

# Fonction pour lancer le serveur Flask dans un thread
def run_flask():
    app.run(debug=True, port=5000, use_reloader=False)  # Désactiver le reloader

# Démarre Flask dans un thread séparé
flask_thread = threading.Thread(target=run_flask)
flask_thread.daemon = True  # Permet au thread de se fermer quand le programme principal se ferme
flask_thread.start()

# Attendre quelques secondes pour s'assurer que le serveur Flask est démarré
time.sleep(2)  # Attendre 2 secondes pour s'assurer que le serveur est prêt

# Envoie la requête POST après que Flask est démarré
url = "http://127.0.0.1:5000"
data = {
    "key": "value"
}

response = requests.post(url, json=data)

# Affiche la réponse du serveur
print(response.text)
