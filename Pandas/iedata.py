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
	floorplans = []

	for rows in reader:
		if rows[0] != lastprop:
			hoods.append(rows[0])
			floorplans.append(rows[-2:])

		lastprop = rows[0]


#print(type(header))
print(header)
print(hoods)
print(rows[-2:])