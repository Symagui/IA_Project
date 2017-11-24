# coding: utf8

import csv
import csv_parsing
import transform

input, output, input_names, output_names = csv_parsing.parse("census-income.names","census-income.data", {"ignore": [24], "ignoreColumnThresold": 0.1});
print("Converting database done.")

formated_input_names, formated_input = transform.transform(input, input_names)
print(formated_input_names)
