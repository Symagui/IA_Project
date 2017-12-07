# IA_Project
Projet d'IA pour Telecom Nancy

Pour executer ce projet, entrer la commande

python [script]

Version : python 3
Dépendances : sklearn, numpy, scipy, graphviz et matplotlib pour une utilisation complète

ATTENTION, vous devez inclure dans le dossier d'installation les fichiers de données fournis sur Arche univ lorraine pour le projet d'IA (dans l'archive census.tar.gz).

Lancement de l'apprentissage et test automatique :
script = main.py

Optimisation des paramètres
script = superparameters_computation.py

Descriptions des scripts tiers :
= csv_parsing.py : transformation des données brut en convertissant les classes en données numériques, création d'un tableau adapté à sklearn et sauvegarde du nom des attributs
= csv_test.py : transformation des données de test uniquement (moins de traitements automatiques que csv_parsing.py)
= transform.py : Booleanisation via DictVectorizer et sauvegarde des nouveaux noms des attributs