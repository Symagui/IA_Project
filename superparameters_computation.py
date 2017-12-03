# coding: utf8

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import csv_parsing
import csv_test
import transform
from sklearn import tree

def getPrecision(max_depth, min_impurity_decrease) :
	clf = tree.DecisionTreeClassifier(max_depth = max_depth, min_impurity_decrease = min_impurity_decrease)
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
			false_pos += 1
		else :
			false_neg +=1
	return true_pos/(true_pos+false_pos)

input, output, input_names, output_names,column_ignored = csv_parsing.parse("census-income.names","census-income.data", {"ignore": [24], "ignoreColumnThresold": 0.1})
transformer, formated_input = transform.transform(input, input_names)
test,test_output = csv_test.parse_test("census-income.test", output_names, column_ignored)
formated_test = transform.transform_test(test, input_names, transformer)
print("Initialization done")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for max_depth in np.arange(1, 10) :
	for min_impurity_decrease in np.arange(0, 1, 0.3) :
		precision = getPrecision(max_depth, min_impurity_decrease)		
		ax.scatter(max_depth, min_impurity_decrease, precision)
		print(max_depth, "; ", min_impurity_decrease, " done")


plt.show()


