FROM python:3.12-slim

WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt .

# Mettre à jour pip
RUN pip install --upgrade pip

# Installer les dépendances Python
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
