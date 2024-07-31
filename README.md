# notif Plateforme de streaming
## Introduction
ce projet vise à créer un systeme de notification qui averti les utilisateurs ayant regardé une série, que cette dernière arrive à expiration et sera retirée de la plateforme.
## Contexte du projet
Ce projet s'inscrit dans un contexte où plusieurs plateforme de streaming offre des séries qui sont `louées` et ayant une date d'expiration. Il sera donc question pour nous de notifier les utilisateurs ayant vus au moins 2 épisodes de la série que celle ci, sera retirée de la plateforme. 

Il seront notifiés par :
### Email
une notification leur sera envoyé sur l'email avec lequel ils se sont inscrit sur la plateforme
### Push notification
Pour ceux ayant l'appli de streaming, un push notification leur sera envoyé.

## Structure des fichiers
- `Datas`: Contient les tables donnant les informations sur les utilisateurs, les séries diffusées, les épisodes, et les historiques
- `Docs`: Contient la documentation du projet
- `Notebooks`: Contient les différents notebooks qui seront utilisés