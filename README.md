# Projet E-Commerce mini App

Ce projet est une mini application e-commerce basée sur Django (Django Rest Framework) et Vue.js qui permet de gérer les produits d’un catalogue.  

L'organisation du projet est la suivante :  
- `ecom-app-front` : Le frontend développé avec Vue.js.  
- `ecom-app-back` : Le backend développé avec Django REST Framework.  

---

## Prérequis

- Python 3.9+ installé  
- Node.js (v14+ recommandé) et npm  
- Git installé  
---

## Instructions d'installation

### Configuration du Backend (Django)

1. **Accédez au dossier du Backend** :  
   cd ecom-app-Back
2. **Installer les dépendances** :  
   pip install -r requirements.txt
3. **Appliquer les migrations** :  
   python manage.py migrate
4. **Lancer le serveur** :  
   python manage.py runserver

### Configuration du Frontend (Vue js)

1. **Accédez au dossier du frontend** :  
   cd ecom-app-front
2. **Create a .env file** :  
   cp .env.example .env
3. **Modifiez le fichier .env pour correspondre à vos paramètres locaux, par exemple l'URL de l'API**:
    API_BASE_URL=http://example:8000/api/
3. **Installer les dépendences** :  
   npm install
4. **Lancer le serveur** :  
   npm run dev



