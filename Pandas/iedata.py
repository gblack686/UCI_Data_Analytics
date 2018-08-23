import os
import pandas as pd
import csv


file = os.path.join("Inland_Empire_Request.csv")

with open(file) as iedata:

	reader = csv.reader(iedata)
	header = next(reader)
	firstrow = next(reader)
	lastprop = None
	hoods = []

	for rows in reader:
		if rows[0] != lastprop:
			hoods.append(rows[0])

		lastprop = rows[0]


#print(type(header))
print(header)
print(rows[-2:])