# Service Django REST

### Modifications à apporter

Avant de lancer le service, il faut modifier le fichier settings.py dans le dossier djangorest et ajouter l'ip hôte dans ALLOWED_HOSTS pour permettre la connection au service via cette adresse ip.

### Lancement

Via la console, se placer dans un premier temps dans le dossier du projet. Il faut alors lancer l'environnement pour python via la commande 
 env/Scripts/activate 
(projet sous Windows). Une fois dans l'environnement, trois commandes sont à exécuter :

      python manage.py makemigrations
      python manage.py migrate
      python manage.py runserver 0.0.0.0:8000
 
L'adresse du serveur et le port pouvant être modifiées, on peut alors accéder au service via l'adresse 'adresse_ip_ou_localhost':8000.

### Liens utiles

https://www.django-rest-framework.org/tutorial/quickstart/
