# coding: utf8

import csv
import csv_parsing
import csv_test
import transform
from sklearn import tree

input, output, input_names, output_names,column_ignored = csv_parsing.parse("census-income.names","census-income.data", {"ignore": [24], "ignoreColumnThresold": 0.1})
transformer, formated_input = transform.transform(input, input_names)

test,test_output = csv_test.parse_test("census-income.test", output_names, column_ignored)
formated_test = transform.transform_test(test, input_names, transformer)
print(formated_test[0])

clf = tree.DecisionTreeClassifier()
clf = clf.fit(formated_input, output)

print (clf.predict([formated_test[0]]))
print (test_output[0])

index = -1
for value in test_output:
	index += 1
	if (value == "50000+"):
		print("ce test devrait retourner 1")
		print(index)
		print(clf.predict([formated_test[index]]))
		break