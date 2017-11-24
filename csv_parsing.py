# coding: utf8

import csv
import numpy as np

#Fonction de filtrage des commentaires et des lignes vides dans le fichier census-income.names
def iscomment(s):
   return not (s.startswith('|') or not s.strip());

def parse(nameFile, dataFile, options = {}):

    input = []
    output = []
    input_names = []
    output_names = []

    if not options.has_key("ignore"):
        options["ignore"] = []
    if not options.has_key("ignoreColumnThresold"):
        options["ignoreColumnThresold"] = 1

    with open(nameFile, 'r') as f:

        i = 0;
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

            else :

                linesplitted = [temp.strip() for temp in line.split(':')]

                #On recupere le nom de la ligne
                for subline in linesplitted[:-1] :
                    if i not in options["ignore"]:
                        input_names.append(subline)

                i+=1

    with open(dataFile, 'r') as csvfile:
        #Lis le csv en virant les espaces inutiles
        reader = csv.reader(csvfile, skipinitialspace=True)
        i = 0;

        csv_unknown_counts = None;

        #On lit chaque ligne pour le pretraitement
        for row in reader:

            row_transformed = [];

            if csv_unknown_counts == None:
                csv_unknown_counts = np.zeros(len(row)-1)

            for index, string in enumerate(row[:-1]) :

                if i in options["ignore"]:
                    break

                #If not ignored
                value = string[:-1] if len(row)-1==index else string;

                if value=="?":
                    csv_unknown_counts[index] += 1

                try:
                    value_transformed = float(value)
                except ValueError:
                    value_transformed = value

                row_transformed.append(value_transformed);

            if (i%1000 == 0):
                print(i)

            input.append(row_transformed);

            i += 1;

        csv_unknown_coefs = [float(x)/float(i) for x in csv_unknown_counts];

        print (csv_unknown_coefs)

    return [input,output,input_names,output_names]
