# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 19:37:28 2018

@author: LAO
Loading Data set to be feed to the model Neural Network
"""

from csv import reader

# Load a CSV file
def load_csv(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	return dataset

# Load dataset
filename = 'corrected.csv'
dataset = load_csv(filename)

def printDataset():
    for x in range(len(dataset)):
        ri = dataset[x]
        print(ri)
    