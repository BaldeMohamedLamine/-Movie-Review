FROM python:3.12-bullseye

# Ne pas écrire de fichiers .pyc
ENV PYTHONDONTWRITEBYTECODE =1

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier des dépendances
COPY  requirements.txt .

# Mettre à jour pip et installer les dépendances
RUN pip install --upgrade pip

RUN pip install -r requirements.txt

# Copier le reste du projet
COPY . .

# Exposer le port 8080
EXPOSE 8080

# Définir la commande pour démarrer l'application avec Uvicorn
CMD ["uvicorn", "movie_review.asgi:application", "--host", "0.0.0.0", "--port", "8080"]
