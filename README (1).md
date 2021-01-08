# Projet Python 

## Description

Actuellement, des vélos de location sont introduits dans de nombreuses villes urbaines pour améliorer le confort de la mobilité. Il est important de rendre le vélo de location disponible et accessible au public au bon moment car cela réduit le temps d'attente. A terme, fournir à la ville une offre stable de vélos de location devient une préoccupation majeure. La partie cruciale est la prévision du nombre de vélos requis à chaque heure pour un approvisionnement stable en vélos de location.
L'ensemble de données contient des informations météorologiques (température, humidité, vitesse du vent, visibilité, point de rosée, rayonnement solaire, chutes de neige, précipitations), le nombre de vélos loués par heure et des informations de date.

## Méthodologie

Tout d’abord, afin d’étudier le dataset nous avons pris chaque variable indépendamment et étudié leur pertinence. 
A la suite de cette étude nous avons ajouté au dataset initial les variables qui nous semblaient manquantes.

Ensuite, pour créer le modèle nous avons tout d’abord scindé le dataset en deux parties : X_train et X_test

Pour finir, nous avons testé trois modèles (Support Vector Machine, ARDRegression et RidgeCV) que nous avons comparé à travers un mean quarre error.

Et enfin implantation d’une API.