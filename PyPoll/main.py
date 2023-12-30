#Operating system and CSV modules imported.
import os
import csv

#Name of the file to be read into Python.
file = 'C:\\Users\\Owner\\OneDrive\\Desktop\\python-challenge\\PyPoll\\Resources\\election_data.csv'

#The file is opened and read into Python.
with open(file) as csvfile:
    
    #The file is read using csv.reader and stored as csvreader.
    csvreader = csv.reader(csvfile, delimiter=',')
    
    print(csvreader)
    
    #The header column is stored and printed.
    csv_header = next(csvreader)
    
    print(f"CSV Header: {csv_header}")

    #A variable "total" will store the total number of votes cast and is initialized at 0.
    total = 0
    
    #Each row in the file is looped through and total is incremented by 1, since each voter casts a single vote.
    for row in csvreader:
    
        total += 1
    
    print('Total Votes: ', total)

    #An empty list is created to store the names of the candidates.
    candidates = []
    
    #Every row in the file is looped through and each candidates name will be added to the list each time it appears.
    for row in csvreader:
        
        candidates.append(row[2])
    
    
    #Duplicate elements are stripped from the list "candidates."
    candidates1 = list(set(candidates))
    
    print(candidates1)
    
    #An empty list to hold the number of votes each candidate received is created.
    votes = []
    
    #For every name in the pared down, the number of times that name occurs in the original list is counted and stored in "votes."
    for name in candidates1:
    
        votes.append(candidates.count(name))
    
    print(votes)

    #The list of candidates and the list of their corresponding vote counts are zipped.
    candidate_counts = zip(candidates1, votes)
    
    #The candidates name is printed with their vote count.
    for name in candidates1:
    
        print(name, ":", candidate_counts[name][1]) #May need to be 0 instead of name
    
    
    #An empty list is created to hold the percentage of all votes each candidate received.
    percent = []

    #Each value in "votes" will be divided by "total" to get the percentage of votes. The value will be stored as a float.
    for num in votes:
    
        percent.append(float(num/total))
    
    #The list of candidates and the list of their corresponding vote percentages are zipped.
    vote_percent = zip(candidates1, percent)

    #The candidate name is printed with their vote percentage.
    for name in candidates1:
    
        print(name, ":", vote_percent[name][1], "%") #May need to be 0 instead of name
    
    
    #The highest vote count is found by using the max function on the list "votes" and is stored as votes. 
    high = max(votes)
    
    #Every tuple in candidate_counts is looped through with second item in each tuple compared to the value of "high."
    #When the value of the second item matches the value of "high," the corresponding candidate is decalared the winner.
    for pair in candidate_counts:
    
        if pair[1] == high:
    
            print('The winner is ', pair[0])


        
            

