# coding: utf8

import csv
import csv_parsing

input, output, input_names, output_names = csv_parsing.parse("census-income.names","census-income.data", {"ignore": [24], "ignoreColumnThresold": 0.1});

print("Converting database done.");
