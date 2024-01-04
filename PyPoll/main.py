#Operating system, CSV, and pandas modules imported.
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
    
    
    #An empty list is created to store the names of the candidates.
    candidates = []
    
    #csvreader is stored as a list called rows.
    rows = list(csvreader)
    
    #Loop through row in rows.
    for row in rows:
       
        #Each row in the file is looped through and total is incremented by 1, since each voter casts a single vote.
        total += 1
        
        #Every row in the file is looped through and each candidates name will be added to the list each time it appears.
        candidates.append(row[2])
    
    print('Total Votes: ', total)

    #All duplicates are removed from "candidates" to create a list where each candidate's name appears once.
    candidates1 = list(set(candidates))
    
    print("Candidates receiving votes: ", candidates1)
    


    #An empty list to hold the number of votes each candidate received is created.
    votes = []
    
    #For every name in the pared down list, the number of times that name occurs in the original list is counted and stored in "votes."
    for name in candidates1:
    
        votes.append(candidates.count(name))
    
    print("Votes for each candidate: ", votes)



    #The list of candidates and the list of their corresponding vote counts are zipped.
    candidate_counts = zip(candidates1, votes)
    
    #The largest vote count in votes is identified and stored as "high".
    high = max(votes)
    
    #Each tuple in "candidate_counts" is looped through and candidate names are printed with corresponding vote totals.
    for t in candidate_counts:
    
        print(t[0], ":", t[1])
        
        #When the first entry in a tuple matches the value of "high", the corresponding candidate name is assigned 
        #to the variable "winner".
        if t[1] == high:
            
            winner = t[0]
    
    
    
    
    
    #An empty list is created to hold the percentage of all votes each candidate received.
    percent = []

    #Each value in "votes" will be divided by "total" to get the percentage of votes. The value will be stored as a float.
    for num in votes:
    
        percent.append((num/total))
    
    #The list of candidates and the list of their corresponding vote percentages are zipped.
    vote_percent = zip(candidates1, percent)

    #The candidate name is printed with their vote percentage.
    for p in vote_percent:
    
        print(p[0], ":", 100 * p[1], "%")
    
    
    #The winner's name is printed.
    print('The winner is', winner,'.')
    
    
    
    file_path = 'C:\\Users\\Owner\\OneDrive\\Desktop\\python-challenge\\PyPoll\\analysis\\PyPoll-analysis.txt'

    with open(file_path,'w') as analysis:
        
        analysis.write(f'Total Votes:{total}\n')

        analysis.write(f'Candidates receiving votes:{candidates1}\n')

        for t in candidate_counts:

            analysis.write(f'{t[0]}:{t[1]}\n')

        for p in vote_percent:

            analysis.write(f'{p[0]}:{(100 * p[1])}%\n')

        analysis.write(f'The winner is {winner}.')

    analysis.close()

csvfile.close()


#The program won't accept my code for printing the candidates with their vote totals and vote percentages to the text file.        
            

