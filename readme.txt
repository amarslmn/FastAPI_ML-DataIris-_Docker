Voici un résumé des différentes étapes de votre projet :
________________________________________________________

1- Vous avez créé une API RESTful pour prédire l'espèce d'une fleur Iris à partir 
de ses mesures morphologiques. Pour cela, vous avez utilisé le framework FastAPI.

2-Vous avez créé un modèle de machine learning pour prédire l'espèce d'une fleur Iris à partir de ses mesures morphologiques 
en utilisant le dataset Iris. Vous avez entraîné ce modèle en utilisant la bibliothèque scikit-learn.

3-Vous avez créé un script pour exporter votre modèle dans un fichier pickle, qui permet de le sauvegarder et de le charger facilement.

4-Vous avez créé une fonction qui utilise le modèle pour faire une prédiction à partir de nouvelles données.

5-Vous avez créé une route POST pour votre API, qui prend des données en entrée et renvoie une prédiction en sortie. Pour cela, 
vous avez utilisé FastAPI et Pydantic pour valider les données d'entrée.

6-Vous avez utilisé Uvicorn pour lancer votre application en mode asynchrone.

7-Vous avez créé un script pour lancer votre application en utilisant Gunicorn, un serveur web compatible avec Uvicorn, 
pour gérer les connexions entrantes et sortantes de votre application.

8-Vous avez testé votre application en utilisant Postman, une plateforme de développement d'API qui vous permet de 
tester rapidement les différentes routes de votre API.

En résumé, vous avez utilisé plusieurs technologies pour créer une API RESTful de prédiction de l'espèce d'une fleur Iris à partir
 de ses mesures morphologiques, en utilisant un modèle de machine learning entraîné avec scikit-learn et exporté dans un fichier pickle.
  Vous avez utilisé FastAPI pour créer votre application, Uvicorn pour la lancer en mode asynchrone, Gunicorn pour gérer les
 connexions entrantes et sortantes, et Postman pour tester votre API.

 ______________________________________________________________________________________________________________________________________________


 Voici 5 points clés importants de ce projet :
 ____________________________________________

1-La création d'une API RESTful à l'aide de FastAPI pour fournir des prédictions de classification de fleurs d'iris à partir 
d'un modèle entraîné.

2-L'utilisation d'un modèle de classification d'iris pré-entraîné en utilisant le dataset d'iris pour prédire l'espèce de fleurs 
d'iris en fonction de leurs caractéristiques.

3-La serialization et la désérialisation du modèle à l'aide de la bibliothèque pickle pour le stocker en tant que fichier binaire et 
le charger pour les prédictions ultérieures.

4-L'utilisation de pandas pour créer un DataFrame contenant les données d'entrée reçues de l'utilisateur via l'API, et la conversion
 des valeurs de ce DataFrame en un tableau NumPy pour les prédictions.

5-Le déploiement de l'API sur un serveur web asynchrone à l'aide de Uvicorn et Gunicorn pour une performance optimale.


Mot clée :

1-Serveur web: Un serveur web est un programme qui permet de répondre aux requêtes d'un client en envoyant des pages web ou des données.
 Il permet de rendre des sites web ou des applications web accessibles sur internet.

2-API: Une API (Application Programming Interface) est une interface qui permet la communication entre différentes applications. 
Elle définit les règles pour la communication entre ces applications.

3-API Restful: Une API Restful est une API qui suit les principes de l'architecture REST (Representational State Transfer).
 Elle utilise les méthodes HTTP pour accéder aux ressources et retourne des réponses en JSON.

4-Serveur web asynchrone: Un serveur web asynchrone utilise des méthodes asynchrones pour gérer les requêtes des clients. 
Cela permet d'optimiser les performances en évitant les temps d'attente et les blocages.

5-FastAPI: FastAPI est un framework pour le développement d'API web basé sur Python. Il permet de créer des API rapides, 
facilement testables et facilement évolutives.

6-Uvicorn: Uvicorn est un serveur web asynchrone pour Python. Il est utilisé pour exécuter des applications basées sur FastAPI.

7-Gunicorn: Gunicorn est un serveur web WSGI pour Python. Il permet de servir des applications web basées sur différents frameworks 
Python, dont FastAPI.

8-Serialization et désérialisation du modèle de prédiction: La serialization et la désérialisation du modèle de prédiction consiste à 
transformer un modèle de prédiction (qui est un objet Python) en un format qui peut être sauvegardé et chargé ultérieurement. 
La serialization permet de sauvegarder le modèle dans un fichier, tandis que la désérialisation permet de le charger à partir de ce fichier.
 Dans ce projet, le module pickle est utilisé pour la serialization et la désérialisation du modèle de prédiction.
 
9- Un serveur web WSGI (Web Server Gateway Interface): est une interface standard entre les serveurs web et les applications web écrites 
en langage de programmation Python. WSGI permet de séparer l'application web de son serveur web, permettant ainsi à l'application 
d'être exécutée sur n'importe quel serveur WSGI compatible.

10- Pickle: est un module Python qui permet de sérialiser et de désérialiser des objets Python. En d'autres termes, 
il permet de transformer des objets Python en une représentation binaire, qui peut être stockée sur le disque dur ou transférée sur le réseau,
 et de les re-transformer en objets Python ultérieurement. Dans le contexte de ce projet, pickle a été utilisé pour stocker 
 le modèle de prédiction sous forme de fichier binaire, ce qui permet de le charger rapidement à chaque appel de l'API 
 plutôt que de re-entraîner le modèle à chaque fois.
