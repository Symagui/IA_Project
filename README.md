# IA_Project
Projet d'IA pour Telecom Nancy

Pour executer ce projet, entrer la commande

python script.py

ATTENTION, vous devez inclure dans le dossier d'installation les fichiers de données fournis sur Arche univ lorraine pour le projet d'IA (dans l'archive census.tar.gz).


Pour préparer OneHotEncoder : 

http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html

Le premier paramètre détermine comment l'encodeur "trouve" la quantité de valeur (int) à transformer en boolean. Je sais pas si on peut le laisser à 'auto' (calcul à partir des valeurs fournies), sinon il faut calculer le nombre de valeurs différentes dans le fichier .names .

Le second paramètre correspond au mask, qui nous permettra d'envoyer toutes les valeurs dans le OneHotEncoder sans avoir à séparer les tableaux de "vrai int" et les "string transformés en int".

Les trois et quatrièmes paramètres ne sont pas utiles pour nous il me semble (à vérifier si vous tombez sur un autre problème que ceux qu'on a déjà découvert). Le 3eme correspond au type de sortie (float par defaut).

Le 5eme permet de prendre en compte les cas inconnus, et donc nous intéresse grandement ! Durant le prétraitement, il faudrait dans l'idéal laisser les '?' tels quels, et renseigner comme 5ème argument le string "?", ce qui lui fera comprendre que c'est une valeur à considérer comme "inconnu".  Je ne sais pas si cela fonctionnera si des "vrai int" sont inconnus par contre (puisque je suppose qu'avec le mask il ne les regardera pas).

Le problème est que le OneHotEncoder ne peut qu'ignorer ou soulever une erreur en cas de valeur inconnue, ainsi il faut apparement d'abord passer par la classe Imputer. VOIRE CHAPITRE 4.3.6 DU LIEN SUIVANT :

http://scikit-learn.org/stable/modules/preprocessing.html#preprocessing-categorical-features

L'imputer permet de remplacer les valeurs manquantes par d'autres valeurs (la moyenne ou la médianne peuvent être utiles en cas de int manquant), mais je ne sais pas comment traiter efficacement les string manquant (une moyenne ou une médianne risque de fausser le résultat puisqu'ils seront transformés en boolean).

On a donc deux solutions : Utiliser une des stratégies de remplissage automatique (qui sont : moyenne, médiane, plus fréquente), ou supprimer la colonne entière. Il faudrait si possible trouver le nombre de colonnes affectés (du moins pour les string) pour voir si la solution radicale de supprimer ces colonnes est acceptable, et si on a le temps il faudrait tester différentes méthodes pour traiter les string manquant (supprimer ou plus fréquent je pense sont les seules applicables).
