# 🚀 Facial Recognition App

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

Ce projet est une application Flask pour la **reconnaissance faciale** utilisant **MongoDB** comme base de données. L'application permet aux utilisateurs de s'enregistrer avec une image de leur visage et de se connecter en utilisant la reconnaissance faciale.

---

## 📋 Table des matières

- [Prérequis](#prérequis)
- [Structure du projet](#structure-du-projet)
- [Lancement de l'application](#lancement-de-lapplication)
- [Endpoints](#endpoints)
- [Technologies utilisées](#technologies-utilisées)
- [Auteur](#auteur)

---

## 🛠️ Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## 📂 Structure du projet

Voici la structure du projet :

```
facial_recognition_app/
│
├── app/
│   ├── __init__.py
│   ├── app.py
│   └── requirements.txt
│
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## 🚀 Lancement de l'application

Suivez ces étapes pour lancer l'application :

1. **Cloner le projet** :
   ```bash
   git clone <repository_url>
   cd facial_recognition_app
   ```

2. **Construire et démarrer les conteneurs Docker** :
   ```bash
   docker-compose up --build
   ```

3. **Accéder à l'application** :
   - L'application sera disponible à l'adresse : `http://localhost:5000`.

---

## 🌐 Endpoints

### 🔐 **POST /register**
Enregistre un nouvel utilisateur avec une image de son visage.

**Paramètres** :
- `image` : Fichier image contenant le visage.
- `username` : Nom d'utilisateur.

**Exemple de requête** :
```bash
curl -X POST -F "image=@path/to/image.jpg" -F "username=john_doe" http://localhost:5000/register
```

---

### 🔑 **POST /login**
Authentifie un utilisateur en utilisant la reconnaissance faciale.

**Paramètres** :
- `image` : Fichier image contenant le visage.

**Exemple de requête** :
```bash
curl -X POST -F "image=@path/to/image.jpg" http://localhost:5000/login
```

---

## 🛠️ Technologies utilisées

- **Flask** : Framework web Python pour créer l'API.
- **MongoDB** : Base de données pour stocker les encodages faciaux.
- **Docker** : Pour conteneuriser l'application et MongoDB.
- **Face Recognition** : Bibliothèque Python pour la reconnaissance faciale.

---

## 👤 Auteur

Ce projet a été créé par Ba Ousmane. Pour toute question ou suggestion, n'hésitez pas à me contacter !

- **GitHub** : Ousmane-BA100
- **Email** : bousmane733@gmail.com

---

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

