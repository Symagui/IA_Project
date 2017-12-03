# coding: utf8

import csv
import csv_parsing
import csv_test
import transform
import numpy as np
import graphviz
import html
from sklearn import tree

print("Parsing .data and .names files - Start")
input, output, input_names, output_names,column_ignored = csv_parsing.parse("census-income.names","census-income.data", {"ignore": [24], "ignoreColumnThresold": 0.1})

print("Parsing .data and .names files - End")
print("Formating data - Start")

transformer, formated_input = transform.transform(input, input_names)
print("Formating data - End")
print("Parsing test file - Start")
test,test_output = csv_test.parse_test("census-income.test", output_names, column_ignored)
print("Parsing test file - End")
print("Formating test data - Start")
formated_test = transform.transform_test(test, input_names, transformer)
print("Formating test data - End")
print("Training the decision tree - Start")

clf = tree.DecisionTreeClassifier(max_depth = 10,
                                  min_impurity_decrease = 0.003,
                                  )

clf = clf.fit(formated_input, output)
print("Training the decision tree - End")
print("Predicting test classes - Start")
test_predicted = clf.predict(formated_test)
print("Predicting test classes - End")
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
print("")
print("")
print("Exporting DotFile to tree and Graph to tree.png")

feature_names_esc = [html.escape(name) for name in transformer.get_feature_names()]

dot_data = tree.export_graphviz(clf, out_file = None,
                                feature_names = feature_names_esc,
                                class_names = output_names,
                                special_characters = True,
                                rounded = True)

graph = graphviz.Source(dot_data, format='png')
graph.render("tree", view=True)


