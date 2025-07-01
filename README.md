# POE-Django

Un projet Django de formation avec des vues simples et des templates.

## 🚀 Installation et Configuration

### Prérequis
- Python 3.11+ installé sur votre système
- Git installé

### 1. Cloner le projet
```bash
git clone https://github.com/votre-username/POE-Django.git
cd POE-Django
```

### 2. Créer et activer l'environnement virtuel
```bash
# Créer l'environnement virtuel
python -m venv mon_env

# Activer l'environnement (Windows)
mon_env\Scripts\activate

# Activer l'environnement (macOS/Linux)
source mon_env/bin/activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Configuration des variables d'environnement
```bash
# Copier le fichier d'exemple
cp .env.example .env

# Modifier le fichier .env avec vos propres valeurs
# Notamment changer la SECRET_KEY
```

### 5. Configurer la base de données
```bash
# Appliquer les migrations
python manage.py migrate

# (Optionnel) Créer un superutilisateur pour l'admin
python manage.py createsuperuser
```

### 6. Lancer le serveur de développement
```bash
python manage.py runserver
```

Le projet sera accessible à l'adresse : `http://127.0.0.1:8000/`

## 📁 Structure du projet

```
POE-Django/
├── .gitignore                   # Fichiers à ignorer par Git
├── manage.py                    # Script de gestion Django
├── requirements.txt             # Dépendances Python
├── README.md                    # Documentation du projet
├── db.sqlite3                   # Base de données SQLite (généré après migrate)
├── mon_env/                     # Environnement virtuel Python (ignoré par Git)
│   ├── Scripts/                # Scripts d'activation (Windows)
│   ├── Lib/                    # Bibliothèques Python installées
│   └── Include/                # Fichiers d'en-tête
├── project/                     # Configuration principale
│   ├── __init__.py             # Package Python
│   ├── settings.py             # Paramètres Django
│   ├── urls.py                 # URLs principales
│   ├── wsgi.py                 # Configuration WSGI
│   ├── asgi.py                 # Configuration ASGI
│   └── __pycache__/            # Fichiers Python compilés (ignorés par Git)
└── core/                       # Application principale
    ├── __init__.py             # Package Python
    ├── views.py                # Vues de l'application
    ├── urls.py                 # URLs de l'application
    ├── models.py               # Modèles de données
    ├── admin.py                # Configuration admin
    ├── apps.py                 # Configuration de l'application
    ├── tests.py                # Tests unitaires
    ├── migrations/             # Migrations de base de données
    │   ├── __init__.py
    │   └── __pycache__/        # Fichiers compilés (ignorés par Git)
    ├── templates/core/         # Templates HTML
    │   └── home.page.html      # Template de la page d'accueil
    └── __pycache__/            # Fichiers Python compilés (ignorés par Git)
```

### ⚠️ Fichiers ignorés par Git

Les éléments suivants sont présents localement mais **non versionnés** grâce au `.gitignore` :

- `mon_env/` : Environnement virtuel Python
- `db.sqlite3` : Base de données locale
- `__pycache__/` : Fichiers Python compilés (.pyc)
- `.vscode/` : Configuration VS Code
- `*.log` : Fichiers de logs

## 🌐 URLs disponibles

- **Page d'accueil** : `http://127.0.0.1:8000/`
  - Affiche le template avec une variable dynamique
- **Vue dynamique** : `http://127.0.0.1:8000/dyn/{nombre}`
  - Exemple : `http://127.0.0.1:8000/dyn/50`
- **Sous-application Core** : `http://127.0.0.1:8000/core/`
  - Message simple depuis l'application core
- **Administration Django** : `http://127.0.0.1:8000/admin/`
  - Interface d'administration (nécessite un superutilisateur)

## 🛠️ Fonctionnalités

- **Templates Django** : Utilisation de templates HTML avec variables dynamiques
- **URLs dynamiques** : Gestion de paramètres dans les URLs
- **Applications modulaires** : Séparation des fonctionnalités avec l'app `core`
- **Interface d'administration** : Admin Django intégré

## 🔧 Développement

### Commandes utiles
```bash
# Créer une nouvelle migration
python manage.py makemigrations

# Appliquer les migrations
python manage.py migrate

# Collecter les fichiers statiques
python manage.py collectstatic

# Lancer les tests
python manage.py test

# Vérifier la configuration
python manage.py check
```

### Ajouter une nouvelle application
```bash
python manage.py startapp nom_app
```

N'oubliez pas d'ajouter la nouvelle application dans `INSTALLED_APPS` dans `settings.py`.

## 📦 Dépendances

- **Django 5.2.3** : Framework web Python
- **asgiref 3.8.1** : Support ASGI pour Django
- **sqlparse 0.5.3** : Parser SQL pour Django
- **tzdata 2025.2** : Données de fuseaux horaires

## 🔍 Dépannage

### Erreur "No module named 'django'"
```bash
# Vérifiez que l'environnement virtuel est activé
mon_env\Scripts\activate
pip install -r requirements.txt
```

### Erreur de migration
```bash
python manage.py makemigrations
python manage.py migrate
```

### Erreur de port déjà utilisé
```bash
# Utiliser un autre port
python manage.py runserver 8001
```

### Problèmes de cache
```bash
# Supprimer les fichiers cache
find . -name "*.pyc" -delete
find . -name "__pycache__" -type d -exec rm -rf {} +
```

## ⚠️ Sécurité

**Important pour la production :**

- Changez la `SECRET_KEY` dans `settings.py`
- Mettez `DEBUG = False` en production
- Configurez `ALLOWED_HOSTS` selon votre domaine
- Utilisez des variables d'environnement pour les données sensibles
- Configurez HTTPS en production

## 🤝 Contribution

1. Forkez le projet
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/nouvelle-fonctionnalite`)
3. Committez vos changements (`git commit -am 'Ajout nouvelle fonctionnalité'`)
4. Pushez vers la branche (`git push origin feature/nouvelle-fonctionnalite`)
5. Ouvrez une Pull Request

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 🐛 Problèmes connus

- Assurez-vous que l'environnement virtuel est activé avant d'installer les dépendances
- Si vous rencontrez des erreurs de modules, vérifiez que Django est bien installé avec `pip list`
- Le fichier `.gitignore` doit être à la racine du projet pour fonctionner correctement

## 📞 Support

Pour toute question ou problème, ouvrez une issue sur GitHub ou contactez l'équipe de développement.

---

**Dernière mise à jour :** Janvier 2025
