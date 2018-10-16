Site disponible à l'adresse suivante : https://nathanetloic.herokuapp.com/

1. Il vous faudra télécharger nodejs pour avoir npm : 
https://nodejs.org/en/download/package-manager/#debian-and-ubuntu-based-linux-distributions

Pour installer tous les fichiers du fichier requirements.txt dans votre virtualenv:

2. activer votre virtualenv avec la commande suivante : ```source bin/activate```
3. diriger vers le dossier qui contient requirements.txt : ```cd Project```
4. Appliquer les migrations : ```python3 manage.py makemigrations``` et ```python3 manage.py migrate```
5. Creer un superutilisateur pour accéder à l'administration : 
    ```echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'pass')" | ./manage.py shell```
6. lancer la commande suivante: ```pip install -r requirements.txt```

7.Il faut ensuite se rendre dans le dossier Projet à la racine puis lancer cette commande pour installer tout les modules nodes nécessaire: ```npm install```

8. lancer le serveur avec la commande ```python3 manager.py runserver```

Ou alors utiliser tout simplement docker-compose

1. a) installer docker-compose : https://docs.docker.com/compose/install/ 
   b) si ce n'est pas déjà fait Ajouter vous dans le groupe docker : ```sudo usermod -aG docker $USER```
2. se diriger vers le dossier project : ```cd Project```
3. Appliquer les migrations : ```python3 manage.py makemigrations``` et ```python3 manage.py migrate```
4. Créer un superutilisateur pour accéder à l'administration : 
    ```echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'pass')" | ./manage.py shell```
5. utiliser la commande ```docker-compose build``` pour construire l'Image avec le Dockerfile
6. utiliser la commande ```docker-compose up``` pour lancer le service web et lancer le serveur à l'adresse http://0.0.0.0:8000/ dans votre navigateur
