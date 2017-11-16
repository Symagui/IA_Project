import csv
with open("census-income.data", 'rb') as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    i = 0;
    for row in reader:
        if (i == 1):
            break;
        i += 1;
        for string in row :
            print(string);
