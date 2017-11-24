# coding: utf8

import csv

final_classes = [];

ROW_TO_READ = 1;

row_names_correspondances = [];
database = [];

#Fonction de filtrage des commentaires et des lignes vides dans le fichier census-income.names
def iscomment(s):
   return not (s.startswith('|') or not s.strip());


#Recuperation des differents attributs, de leurs valeurs possibles et des differentes classes dans le fichier census-income.names
with open("census-income.names", 'r') as f:
    first = True;
    #On recupere les lignes non inutiles
    for line in filter(iscomment, f):

        #La première ligne est traitee differement des autres car elle ne contient que les classes finales, et pas de nom supplementaire
        if (first):
            first = not first;
            #Un peu de magie qui split la ligne selon le csv, la strip et la mets dans un array
            final_classes = [classe.strip() for classe in line.split(',')]

            #Suppression du POINT a la fin de la derniere classe
            final_classes[-1] = final_classes[-1][:-1]

            #Juste un print de test
            """
            for classe in classes:
                print(classe);
            """
        else :

            linesplitted = [temp.strip() for temp in line.split(':')]

            #On recupere le nom de la ligne
            for subline in linesplitted[:-1] :
                print("col : " + subline)
            #On recupere la liste des valeurs associees a ce nom
            else:
                #Pour chaque valeur on strip et on enlève le POINT de la dernière valeur
                values = [value.strip() for value in linesplitted[-1].split(',')]
                values[-1] = values[-1][:-1]
                row_names_correspondances.append(values);

#print final_classes;


#La section suivante traite le document csv data et en sort les valeurs
with open("census-income.data", 'r') as csvfile:

    #Lis le csv en virant les espaces inutiles
    reader = csv.reader(csvfile, skipinitialspace=True)
    i = 0;

    #On lit chaque ligne pour le pretraitement
    for row in reader:

        row_transformed = [];

        #Il faut separer le pretraitement de chaque valeur puisque les valeurs nominales devront passer par la librairie
        #De plus, on doit traiter separement la derniere valeur du csv puisque les lignes finissent par un POINT.
        for index, string in enumerate(row[:-1]) :
            value = string[:-1] if len(row)-1==index else string;

            print(index);

            if value in row_names_correspondances[index]:
                value_transformed = row_names_correspondances[index].index(value);
            else:
                value_transformed = -1 if value=="?" else float(value);

            row_transformed.append(value_transformed);

        if (i == ROW_TO_READ):
            break;

        database.append(row_transformed);

        i += 1;

print("Converting database done.");
