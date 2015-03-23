import csv as csv
import numpy as np

csv_file_object = csv.reader(open('train.csv', 'rt'))

header = csv_file_object.__next__()

data = []

for row in csv_file_object:
    data.append(row)

data = np.array(data)

#print(data[0,3])