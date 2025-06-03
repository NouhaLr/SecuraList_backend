Projet Flutter + Django : Vente de produits d'occasion
Application mobile permettant aux utilisateurs de publier, consulter et gérer des produits d’occasion. Elle comprend un frontend Flutter et un backend Django avec API REST et GraphQL.

Fonctionnalités principales
Frontend (Flutter)
Authentification par email (inscription, connexion, mot de passe oublié)

Ajout de produit (nom + description)

Catégorisation automatique du produit (faite côté backend)

Affichage de la liste des produits

Visualisation des sessions d’appareil actives
Backend (Django)
Authentification avec JWT (via Djoser)

API REST : utilisateurs, produits, sessions d'appareil

API GraphQL : requêtes sur les produits

Catégorisation automatique basée sur le texte du produit

Technologies
Backend : Django, Django REST Framework, Djoser, Graphene-Django
Frontend : Flutter, Provider, http, graphql_flutter


Installation
Backend
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


Frontend
cd flutter_app
flutter pub get
flutter run

Exemple de requête GraphQL
query {
  allUsers {
    id
    username
    email
  }
}

Exemple de catégorisation
Lorsqu'un produit est ajouté avec une description, le backend déduit automatiquement une catégorie (ex. "Électronique", "Maison", etc.) à l'enregistrement.

Structure du projet
backend/
  users/
  products/
  graphql_api/
flutter_app/
  lib/
    pages/
    services/
    widgets/
README.md
