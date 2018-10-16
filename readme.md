Site disponible à l'adresse suivante : https://nathanetloic.herokuapp.com/

## Sans docker compose

1. Il vous faudra télécharger nodejs pour avoir npm : 
https://nodejs.org/en/download/package-manager/#debian-and-ubuntu-based-linux-distributions

Pour installer tous les fichiers du fichier requirements.txt dans votre virtualenv:

2. activer votre virtualenv avec la commande suivante : ```source bin/activate```
3. diriger vers le dossier qui contient requirements.txt : ```cd Project```
4. lancer la commande suivante: ```pip install -r requirements.txt```
5. Il faut ensuite se rendre dans le dossier Projet à la racine puis lancer cette commande pour installer tout les modules nodes nécessaire: ```npm install```
6. Rendre le script pour lancer les migrations et créer un superutilisateur exécutable : ```chmod u+x setupTODO.sh```
7. Lancer le script : ```./setupTODO.sh```
8. lancer le serveur avec la commande ```python3 manager.py runserver```

## Avec docker compose

1. Ou alors utiliser tout simplement docker-compose
   - a) installer docker-compose : https://docs.docker.com/compose/install/ 
   - b) si ce n'est pas déjà fait s'ajouter dans le groupe docker : ```sudo usermod -aG docker $USER```
2. diriger vers le dossier qui contient requirements.txt : ```cd Project```
3. Rendre le script pour lancer les migrations et créer un superutilisateur exécutable : ```chmod u+x setupTODO.sh```
4. Lancer le script : ```./setupTODO.sh```
5. utiliser la commande ```docker-compose build``` pour construire l'Image avec le Dockerfile
6. utiliser la commande ```docker-compose up``` pour lancer le service web et lancer le serveur à l'adresse http://0.0.0.0:8000/ dans votre navigateur
