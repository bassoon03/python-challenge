import os
import csv
import math

file = 'C:\\Users\\Owner\\OneDrive\\Desktop\\python-challenge\\PyBank\\Resources\\budget_data.csv'
with open(file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    for row in csvreader:
        print(row)
    
    months = 0
    for row in csvreader:
        months += 1
        print('Months: ', months)

    

