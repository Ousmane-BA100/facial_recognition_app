# Utiliser une image de base Python
FROM python:3.9-slim

# Installer les dépendances système nécessaires pour dlib et CMake
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    cmake \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances
COPY app/requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste des fichiers de l'application
COPY app/ .

# Exposer le port 5000
EXPOSE 5000

# Commande pour lancer l'application
CMD ["python", "app.py"]