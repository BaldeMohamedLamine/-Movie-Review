FROM python:3.12-slim

WORKDIR /app

# Ajouter les dépendances système
RUN apt-get update && apt-get install -y \
    libpq-dev gcc --no-install-recommends && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copier les fichiers nécessaires
COPY requirements.txt .

# Mettre à jour pip
RUN pip install --upgrade pip

# Installer les dépendances Python
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
