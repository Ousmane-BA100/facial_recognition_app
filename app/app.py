from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
import numpy as np
import face_recognition

app = Flask(__name__)
CORS(app)

# Configuration de la connexion MongoDB
app.config["MONGO_URI"] = "mongodb://mongo:27017/biometric_db"
mongo = PyMongo(app)

# Collection des utilisateurs
collection = mongo.db.users

### Enregistrer un utilisateur avec une image
@app.route('/register', methods=['POST'])
def register():
    file = request.files['image']
    username = request.form.get('username')
    
    if not file or not username:
        return jsonify({"error": "Image et username requis"}), 400

    # Charger l’image et extraire les encodages faciaux
    image = face_recognition.load_image_file(file)
    encodings = face_recognition.face_encodings(image)

    if len(encodings) == 0:
        return jsonify({"error": "Aucun visage détecté"}), 400

    # Convertir en JSON
    encoding_list = encodings[0].tolist()

    # Stocker dans MongoDB
    collection.insert_one({"username": username, "encoding": encoding_list})

    return jsonify({"message": f"Utilisateur {username} enregistré avec succès !"})

### Vérifier l’identité avec MongoDB (Login)
@app.route('/login', methods=['POST'])
def login():
    file = request.files['image']
    
    if not file:
        return jsonify({"error": "Image requise"}), 400

    # Charger l’image et extraire les encodages faciaux
    image = face_recognition.load_image_file(file)
    encodings = face_recognition.face_encodings(image)

    if len(encodings) == 0:
        return jsonify({"error": "Aucun visage détecté"}), 400

    unknown_encoding = encodings[0]

    # Récupérer les utilisateurs enregistrés
    users = collection.find()

    for user in users:
        stored_encoding = np.array(user["encoding"])
        match = face_recognition.compare_faces([stored_encoding], unknown_encoding)[0]
        
        if match:
            return jsonify({"message": f"Authentification réussie pour {user['username']} !"})

    return jsonify({"error": "Aucun visage correspondant trouvé"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)