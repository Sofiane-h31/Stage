from flask import Flask, jsonify, request
import threading
import time
import ollama

# Crée l'application Flask
app = Flask(__name__)

# Fonction pour interagir avec Ollama
def interact_with_ollama(prompt):
    response = ollama.chat(model="llama3.2", messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.get_json()
        prompt = data.get('prompt', 'Expliquez-moi la gravité.')  # Par défaut si aucune donnée n'est envoyée
        response_from_ollama = interact_with_ollama(prompt)  # Appel à Ollama ici
        return jsonify(message="Data received", response_from_ollama=response_from_ollama)
    else:
        return jsonify(message="Hello from the server!")

def run_flask():
    app.run(debug=True, port=5000, use_reloader=False)

flask_thread = threading.Thread(target=run_flask)
flask_thread.daemon = True
flask_thread.start()

time.sleep(2)

