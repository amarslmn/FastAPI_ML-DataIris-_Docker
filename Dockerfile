# utiliser une image de base qui contient python 3.8

FROM python:3.8-slim-buster

# définir le répertoire de travail de l'application

WORKDIR /app

# Copier les fichiers de l'application dans le conteneur

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Exposer le port utilisé par l'application 

EXPOSE 80

# Lancer l'application

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]