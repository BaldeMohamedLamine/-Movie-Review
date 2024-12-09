# Movie Review Application

## Description
Cette application web permet aux utilisateurs de partager des critiques de films, de commenter les critiques d'autres utilisateurs, et de noter des films. Elle est construite avec Django et utilise des fonctionnalités avancées pour améliorer l'expérience utilisateur.

## Fonctionnalités Principales
- **Gestion des utilisateurs** :
  - Inscription, connexion, déconnexion.
  - Profil utilisateur avec la possibilité de mettre à jour les informations personnelles.
  - Gestion des permissions : seuls les utilisateurs authentifiés peuvent écrire des critiques ou des commentaires.

- **Catalogue de films** :
  - Affichage d'une liste de films avec la possibilité de filtrer par genre, année de sortie, et note moyenne.
  - Page détaillée pour chaque film, incluant le casting, la note moyenne, et les critiques des utilisateurs.

- **Critiques de films** :
  - Les utilisateurs peuvent ajouter une critique pour un film avec une note (sur 5 étoiles).
  - Les critiques incluent un titre, un texte de critique, et la date de publication.
  - Un utilisateur ne peut publier qu'une seule critique par film, mais peut modifier ou supprimer sa critique.

- **Commentaires** :
  - Les utilisateurs peuvent commenter les critiques publiées par d'autres utilisateurs.
  - Les commentaires sont modérés par les administrateurs.

- **Notes et Classement** :
  - Calcul de la note moyenne des films en fonction des notes données dans les critiques.
  - Classement des films par popularité en fonction du nombre de critiques et de la note moyenne.

## Fonctionnalités Avancées
- Recherche de films et critiques.
- API REST pour accéder aux données de films, critiques et utilisateurs via des requêtes HTTP.
- Pagination sur les listes de films et de critiques.
- Intégration de services externes pour récupérer des informations des films.

## Installation
1. Clonez le dépôt :
   ```bash
   git clone <URL_DU_DEPOT>
   ```
2. Naviguez dans le répertoire du projet :
   ```bash
   cd Movie-Review
   ```
3. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
4. Effectuez les migrations :
   ```bash
   python manage.py migrate
   ```
5. Lancez le serveur :
   ```bash
   python manage.py runserver
   ```

## Contribuer
Les contributions sont les bienvenues ! Veuillez soumettre une demande de tirage pour toute modification.

## License
Ce projet est sous licence MIT.
