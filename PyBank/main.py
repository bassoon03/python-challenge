#Import operating system module
import os

#Import Comma Separated Value module
import csv

#File pathway stored as "file"
file = 'C:\\Users\\Owner\\OneDrive\\Desktop\\python-challenge\\PyBank\\Resources\\budget_data.csv'

#"file" is opened as csvfile
with open(file) as csvfile:
    
    #"file" is read using csv.reader and stored as csvreader
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #The header row of the csv file is stored
    csv_header = next(csvreader)
    
    #The header row of the csv file is printed
    print(f"CSV Header: {csv_header}")
    

    
    
    #Variable to store the number of months under consideration, initialized to 0
    months = 0.0
    
    #Variable to store the greatest increase, initialized to 0
    greatest = 0.0
    
    #Variable to store the greatest decrease, initialized to 0
    least = 0.0
    
    #Variable to store the total change, initialized to 0
    total = 0.0

    #List to store the values of the "Profits/Losses" column, starts as an empty list
    profits = []

    #List to store the values of the changes in "Profits/Losses" column from month to month
    #Starts as an empty list, will contain one less value than "profits" list
    profits_c = []
    
    
    
    #Loop through the rows in csvreader
    for row in csvreader:
        
        #"months" variable is incremented by 1 for each row in csvreader
        months += 1
        
        #"total" variable incremented by value in "Profits/Losses" column according to the row
        total += float(row[1])
        
        #"profits" list filled with values in "Profits/Losses" column
        profits.append(row[1])
    
    
    
    #Looping throught the list "profits", we only want the differences between successive value, that is why the range
    #is 1 less than the length of the "profits"
    for i in range(len(profits)-1):
        
        
        #Differences between successive values in "profits" are compared. If they are greater than the variable "greatest",
        #then "greatest" is updated
        if profits[i+1]-profits[i] > greatest:
            
            greatest = profits[i+1]-profits[i]
        
        #Similarly, if the difference between successive values in "profits" is less than "least", then least is updated
        if profits[i+1]-profits[i] < least:
            
            least = profits[i+1]-profits[i]
        
        #The list "profits_c" is filled with the differences between successive value, that is, the changes
        profits_c.append(profits[i+1]-profits[i])

    
    
    
    #Number of months is printed
    print('Months: ', months)
    
    
    #Total profit or loss is printed
    print('Total: ', total)

   
    #The number of changes is 1 less than the number of months. To calculate the average change, "months" - 1 cannot equal 0
    if (months-1) != 0:
    
        
        #The average change is the sum of the elements of "profits_c" divided by 1 less than "months"
        print('Average Change: ', sum(profits_c)/(months-1))
    
    
    #The greatest increase is printed
    print('Greatest Increase: ', greatest)
    
    
    #The greatest decrease is printed
    print('Greastest Decrease: ', least)

