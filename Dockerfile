# Utiliser l'image officielle de Rasa
FROM rasa/rasa:latest-full

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers du projet dans le conteneur
COPY . /app

# Installer les dépendances supplémentaires
RUN pip install -r requirements.txt

# Exposer le port 5005 (port par défaut pour Rasa) et 5055 (pour les actions personnalisées)
EXPOSE 5005
EXPOSE 5055

# Lancer le serveur Rasa et le serveur des actions
CMD ["sh", "-c", "rasa run --enable-api --cors '*' --credentials credentials.yml & rasa run actions"]
