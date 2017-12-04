# coding: utf8

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import csv_parsing
import csv_test
import transform
from sklearn import tree
from threading import Thread

precisions = []
threads = []

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

class Computation(Thread):
	def __init__(self, i, max_depth, min_impurity_decrease):
		Thread.__init__(self)
		self.max_depth = max_depth
		self.min_impurity_decrease = min_impurity_decrease
		self.i = i

	def run(self):
		global precisions
		precision = getPrecision(self.max_depth, self.min_impurity_decrease)		
		ax.scatter(self.max_depth, self.min_impurity_decrease, precision)
		precisions[self.i] = precision
		print(self.max_depth, "; ", self.min_impurity_decrease, " done")



input, output, input_names, output_names,column_ignored = csv_parsing.parse("census-income.names","census-income.data", {"ignore": [24], "ignoreColumnThresold": 0.1})
transformer, formated_input = transform.transform(input, input_names)
test,test_output = csv_test.parse_test("census-income.test", output_names, column_ignored)
formated_test = transform.transform_test(test, input_names, transformer)
print("Initialization done")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

i = 0
for max_depth in np.arange(1, 10) :
	for min_impurity_decrease in np.arange(0, 0.0001, 0.00001) :
		precisions.append(0)
		threads.append(Computation(i, max_depth, min_impurity_decrease))
		threads[-1].start()
		i += 1

		if (i % 4 == 0) :
			for n in range(i - 4, i) :
				threads[n].join()


for i in range(0, len(threads)) :
	threads[i].join()

print(precisions)

max_depth_final = 0
min_impurity_decrease_final = 0
precision_final = 0

i = 0
for max_depth in np.arange(1, 10) :
	for min_impurity_decrease in np.arange(0, 0.0001, 0.00001) :
		if (precisions[i] > precision_final) :
			precision_final = precisions[i]
			max_depth_final = max_depth
			min_impurity_decrease_final = min_impurity_decrease
		i += 1

print("Precision : ", precision_final)
print("Max depth : ", max_depth_final)
print("Min impurity decrease : ", min_impurity_decrease_final)

"""max_depth_final = 0
min_impurity_decrease_final = 0
precision_final = 0

for max_depth in np.arange(1, 10) :
	for min_impurity_decrease in np.arange(0, 0.01, 0.001) :
		precision = getPrecision(max_depth, min_impurity_decrease)		
		ax.scatter(max_depth, min_impurity_decrease, precision)
		if (precision > precision_final) :
			precision_final = precision
			max_depth_final = max_depth
			min_impurity_decrease_final = min_impurity_decrease
		print(max_depth, "; ", min_impurity_decrease, " done")

print("Precision : ", precision_final)
print("Max depth : ", max_depth_final)
print("Min impurity decrease : ", min_impurity_decrease_final)
plt.show()"""


