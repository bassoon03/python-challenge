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
    
    print('Total Values: ', total)

    candidates = {}
    
    for row in csvreader:
    
        if row[2] not in candidates.keys():
    
            candidates[row[2]] = 1
    
        else:
    
            candidates[row[2]] += 1
    

    for keys, value in candidates.items():
    
        print(keys)
    
        print(keys, ":", value)
    
        print(keys,":", 100*(value/total),"%")

    
    key_list = list(candidates.keys())
    
    value_list = list(candidates.values())
    
    print('The winner is ', key_list[value_list.index(max(value_list))])