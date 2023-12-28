import os
import csv
import math

file = 'C:\\Users\\Owner\\OneDrive\\Desktop\\python-challenge\\PyBank\\Resources\\budget_data.csv'

with open(file) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    print(csvreader)
    
    csv_header = next(csvreader)
    
    print(f"CSV Header: {csv_header}")
    

    
    months = 0.0
    
    greatest = 0.0
    
    least = 0.0
    
    total = 0.0
    
    change = 0.0
    
    average = 0.0
    
    for row in csvreader:
        
        months += 1
        
        if float(row[1]) > greatest:
        
            greatest = float(row[1])
        
        if float(row[1]) < least:
        
            least = float(row[1])
        
        total += math.fabs(float(row[1]))
        
        change += float(row[1])
    
    print('Months: ', months)
    
    print('Greatest Increase: ', greatest)
    
    print('Greastest Decrease: ', least)
    
    print('Total: ', total)
    


    if months != 0:
        
        average = change/months
    
    print('Average Change: ', average)

