import csv
import os

file = "budget_data.csv"
outputfile = "budget_analysi.csv"

with open(file) as budget_data:
	reader = csv.reader(budget_data)
	header = next(reader)
	firstrow = next(reader)
	net_start = int(firstrow[1])
	monthtracker = 1
	netprofit = net_start 
	lastnet = 0
	netchangelist = []
	prevnet = net_start

	greatest_increase = 0
	greatest_decrease = 0

	for rows in reader:
		net = int(rows[1])
		date = rows[0]


		monthtracker = monthtracker + 1

		netprofit = net + netprofit 

		netchange = net - prevnet
		prevnet = net

		netchangelist.append(netchange)

		lastnet = net

		if greatest_increase is 0 or netchange > greatest_increase[1]:
			greatest_increase = (date, netchange)
		if greatest_decrease is 0 or netchange < greatest_decrease[1]:
			greatest_decrease = (date, netchange)

avg_change = sum(netchangelist) / len(netchangelist)


output = f"""
Financial Analysis
-----------------------------
Months: {monthtracker}
Net Profit: ${netprofit}
Average Change: ${avg_change}
Greatest Increase: ${greatest_increase[1]} ({greatest_increase[0]})
Greatest Decrease: ${greatest_decrease[1]} ({greatest_decrease[0]})
"""

print(output)

with open(outputfile,"w") as txt_file:
	txt_file.write(output)
