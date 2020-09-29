
import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    
    # Read each row of Data after the header

    for row in csvreader:
        print(row)

# The total number of months included in dataset

rows = list(csvreader(open("budget_data.csv"))) row_count = len(rows)
