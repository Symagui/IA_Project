# coding: utf8

import csv
import csv_parsing
import csv_test
import transform
import numpy as np
from sklearn import tree

input, output, input_names, output_names,column_ignored = csv_parsing.parse("census-income.names","census-income.data", {"ignore": [24], "ignoreColumnThresold": 0.1})
transformer, formated_input = transform.transform(input, input_names)

test,test_output = csv_test.parse_test("census-income.test", output_names, column_ignored)
formated_test = transform.transform_test(test, input_names, transformer)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(formated_input, output)

test_predicted = clf.predict(formated_test)
total_rows = len(test_predicted)
index = 0
true_pos = 0
false_pos = 0
true_neg = 0
false_neg = 0
for index in range(total_rows):
    if (test_predicted[index] == test_output[index]):
        if (test_predicted[index] == 0):
            true_pos += 1
        else:
            true_neg += 1
    elif (test_predicted[index] == 0):
        false_pos += 1;
    else :
        false_neg +=1

print("Test Results :  (positive means '- 50000')")
print("true_pos : "+str(true_pos)+" - "+"{:.0%}".format(true_pos/total_rows))
print("true_neg : "+str(true_neg)+" - "+"{:.0%}".format(true_neg/total_rows))
print("false_pos: "+str(false_pos)+" - "+"{:.0%}".format(false_pos/total_rows))
print("false_neg: "+str(false_neg)+" - "+"{:.0%}".format(false_neg/total_rows))
print("Total row: "+str(total_rows)+" - "+"{:.0%}".format(total_rows/total_rows))
print("Correct %: "+"{:.0%}".format((true_pos+true_neg)/total_rows))
print("Précision: "+"{:.0%}".format(true_pos/(true_pos+false_pos)))
print("Rappel   : "+"{:.0%}".format(true_pos/(true_pos+false_neg)))




