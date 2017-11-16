import csv
from itertools import ifilterfalse

classes = [];

ROW_TO_READ = 1;
def iscomment(s):
   return s.startswith('|') or not s.strip();

with open("census-income.names", 'r') as f:
    first = True;
    i = 0
    for line in ifilterfalse(iscomment, f):
        if (first):
            first = not first;
            classes = [classe.strip() for classe in line.split(', ')]
            classes[len(classes)-1] = classes[len(classes)-1][:-1]
            for classe in classes:
                print(classe);
        else :
            break;
        print("#" + str(i) + ": " + line);
        i+= 1;
    print("there were " + str(i) + " line(s).")

print classes;


#La section suivante traite le document csv data et en sort les valeurs
with open("census-income.data", 'rb') as csvfile:

    #Lis le csv en virant les espaces inutiles
    reader = csv.reader(csvfile, skipinitialspace=True)
    i = 0;

    #On lit chaque ligne pour le pretraitement
    for row in reader:

        #Il faut separer le pretraitement de chaque valeur puisque les valeurs nominales devront passer par la librairie
        #De plus, on doit traiter separement la derniere valeur du csv puisque les lignes finissent par un POINT.
        for string in row[:-1] :
            print(string);
        else :
            print(string[:-1])
        if (i == ROW_TO_READ):
            break;

        i += 1;
