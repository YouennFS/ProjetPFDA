{\rtf1\ansi\ansicpg1252\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Projet Python \
\
## Description\
\
\pard\pardeftab720\partightenfactor0
\cf0 Actuellement, des v\'e9los de location sont introduits dans de nombreuses villes urbaines pour am\'e9liorer le confort de la mobilit\'e9. Il est important de rendre le v\'e9lo de location disponible et accessible au public au bon moment car cela r\'e9duit le temps d'attente. A terme, fournir \'e0 la ville une offre stable de v\'e9los de location devient une pr\'e9occupation majeure. La partie cruciale est la pr\'e9vision du nombre de v\'e9los requis \'e0 chaque heure pour un approvisionnement stable en v\'e9los de location.\
L'ensemble de donn\'e9es contient des informations m\'e9t\'e9orologiques (temp\'e9rature, humidit\'e9, vitesse du vent, visibilit\'e9, point de ros\'e9e, rayonnement solaire, chutes de neige, pr\'e9cipitations), le nombre de v\'e9los lou\'e9s par heure et des informations de date.\
\
## M\'e9thodologie\
\
Tout d\'92abord, afin d\'92\'e9tudier le dataset nous avons pris chaque variable ind\'e9pendamment et \'e9tudi\'e9 leur pertinence. \
A la suite de cette \'e9tude nous avons ajout\'e9 au dataset initial les variables qui nous semblaient manquantes.\
\
Ensuite, pour cr\'e9er le mod\'e8le nous avons tout d\'92abord scind\'e9 le dataset en deux parties : X_train et X_test\
\
Pour finir, nous avons test\'e9 trois mod\'e8les (Support Vector Machine, ARDRegression et RidgeCV) que nous avons compar\'e9 \'e0 travers un mean quarre error.\
\
Et enfin implantation d\'92une API.}