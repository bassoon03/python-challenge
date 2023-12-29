import os
import csv

file = 'C:\\Users\\Owner\\OneDrive\\Desktop\\python-challenge\\PyPoll\\Resources\\election_data.csv'

with open(file) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    print(csvreader)
    
    csv_header = next(csvreader)
    
    print(f"CSV Header: {csv_header}")

    
    total = 0
    
    for row in csvreader:
    
        total += 1
    
    print('Total Votes: ', total)

    
    candidates = []
    
    for row in csvreader:
        candidates.append(row[4])
    
    print(candidates)
    candidates = list(set(candidates))
    print(candidates)
        
            

