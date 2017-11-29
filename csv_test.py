# coding: utf8

import csv
import numpy as np

def parse_test(testFile, output_names, ignoredColumns) :

	test = []
	test_output = []

	with open(testFile, 'r') as csvfile :
		reader = csv.reader(csvfile, skipinitialspace=True)
		for row in reader:
			transformed_row = []
			for index, value in enumerate(row) :
				if (not index in ignoredColumns) :
					try:
						transformed_row.append(float(value))
					except ValueError:
						transformed_row.append(value)
			if (not "?" in transformed_row and transformed_row != []) :
				test_output.append(output_names.index(transformed_row[-1][:-1]))
				test.append(transformed_row[:-1])

	return [test,test_output]