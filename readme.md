Site disponible à l'adresse suivante :
https://nathanetloic.herokuapp.com/

il vous faudra télécharger nodejs pour avoir npm:

https://nodejs.org/en/download/package-manager/#debian-and-ubuntu-based-linux-distributions

Pour installer tous les fichiers du fichier requirements.txt dans votre virtualenv:

1. activer votre virtualenv avec la commande suivante : source bin/activate
2. diriger vers le dossier qui contient requirements.txt : cd Project
3. lancer la commande suivante: pip install -r requirements.txt

Il faut ensuite se rendre dans le dossier Projet à la racine puis lancer cette commande pour installer tout les modules nodes nécessaire:

npm install

Ou alors utiliser tout simplement docker-compose

1. installer docker-compose : https://docs.docker.com/compose/install/
2. se diriger vers le dossier project : cd Project
3. utiliser la commande docker-compose build pour construire l'Image avec le Dockerfile
4. utiliser la commande docker-compose up pour lancer le service web et lancer le serveur à l'adresse http://0.0.0.0:8000/ dans votre navigateur
