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

    unknown_element_by_row = []

    if not "ignore" in options:
        options["ignore"] = []
    if not "ignoreColumnThresold" in options:
        options["ignoreColumnThresold"] = 1
    if not "report" in options:
        options["report"] = True

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
            unknown_element_by_row.append(0);

            if csv_unknown_counts is None:
                csv_unknown_counts = np.zeros(len(row)-1)

            for index, value in enumerate(row) :

                if index<len(row)-len(options["ignore"]) :

                    if index in options["ignore"]:
                        continue

                    if value=="?":
                        csv_unknown_counts[index] += 1
                        unknown_element_by_row[i] += 1;

                    try:
                        value_transformed = float(value)
                    except ValueError:
                        value_transformed = value

                    row_transformed.append(value_transformed);

                else :
                    #Classe resultat
                    value = value[:-1]; #La dernière ligne contient un . final
                    if value not in output_names:
                        output_names.append(value)
                    output.append(output_names.index(value));

            if (i%10000 == 0):
                print(i)

            input.append(row_transformed);

            i += 1;

        csv_unknown_coefs = [float(x)/float(i) for x in csv_unknown_counts];

        ignore = []
        column_ignored = 0
        input = np.array(input, dtype=object)
        for index, value in enumerate(csv_unknown_coefs):
            if value>options["ignoreColumnThresold"]:
                #On élimine les lignes pas intéressantes qui sont donc dans ignore
                del input_names[index-column_ignored]
                input = np.delete(input, index-column_ignored, 1)
                ignore.append(index)
                column_ignored += 1

        input = input.tolist()

        #Update unknown columns by row
        unknown_element_by_row = [x-column_ignored for x in unknown_element_by_row]

        #Remove not fully known rows
        deleted_row = 0
        for index, value in enumerate(unknown_element_by_row):
            if value>0:
                del input[index-deleted_row]
                del output[index-deleted_row]
                deleted_row+=1;

        if options["report"]:
            print ("Deleted columns : ("+str(column_ignored)+") "+str(ignore))
            print ("Deleted columns coefs : "+str(csv_unknown_coefs))
            print ("Deleted rows because not fully known : "+str(deleted_row))
            print ("Total rows read : "+str(i))


    return [input,output,input_names,output_names, ignore+options["ignore"]]
