# coding: utf8

import csv
import csv_parsing

input, output, input_names_correspondances, output_names_correspondances = csv_parsing.parse("census-income.names","census-income.data", {"ignore": [15,3], "ignoreColumnThresold": 0.1});

print("Converting database done.");
