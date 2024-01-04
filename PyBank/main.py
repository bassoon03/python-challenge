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
    increase = 0.0
    
    #Variable to store the greatest decrease, initialized to 0
    decrease = 0.0
    
    #Variable to store the total change, initialized to 0
    total = 0.0

    #List to store the values of the "Profits/Losses" column, starts as an empty list
    profits = []

    #List to store the values of the changes in "Profits/Losses" column from month to month
    #Starts as an empty list, will contain one less value than "profits" list
    profits_c = []
    
    
    rows = list(csvreader)
    #Loop through the rows in csvreader
    for row in rows:
        
        #"months" variable is incremented by 1 for each row in csvreader
        months += 1
        
        #"total" variable incremented by value in "Profits/Losses" column according to the row
        total += float(row[1])
        
        #"profits" list filled with values in "Profits/Losses" column
        profits.append(row[1])
    
    print(profits)
    
    #Looping throught the list "profits", we only want the differences between successive value, that is why the range
    #is 1 less than the length of the "profits"
    for i in range(len(profits)-1):
        
        
        #Differences between successive values in "profits" are compared. If they are greater than the variable "increase",
        #then "increase" is updated
        if float(profits[i+1]) -float(profits[i]) > increase:
            
            increase = float(profits[i+1]) - float(profits[i])
        
        #Similarly, if the difference between successive values in "profits" is less than "decrease", then "decrease" is updated
        if float(profits[i+1]) - float(profits[i]) < decrease:
            
            decrease = float(profits[i+1]) - float(profits[i])
        
        #The list "profits_c" is filled with the differences between successive value, that is, the changes between months
        profits_c.append(float(profits[i+1]) - float(profits[i]))

    
    
    
    #Number of months is printed
    print('Months: ', months)
    
    
    #Total profit or loss is printed
    print('Total: ', total)

   
    #The number of changes is 1 less than the number of months. To calculate the average change, "months" - 1 cannot equal 0
    if (months-1) != 0:
    
        
        #The average change is the sum of the elements of "profits_c" divided by 1 less than "months"
        print('Average Change: ', sum(profits_c)/(months-1))
    
    
    #The greatest increase is printed
    print('Greatest Increase: ', increase)
    
    
    #The greatest decrease is printed
    print('Greastest Decrease: ', decrease)


    #data1 = print('Months: ', months)
    #data2 = print('Total: ', total)
    #data3 = print('Average Change: ', sum(profits_c)/(months-1))
    #data4 = print('Greatest Increase: ', increase)
    #data5 = print('Greastest Decrease: ', decrease)

    file_pathx = 'C:\\Users\\Owner\\OneDrive\\Desktop\\python-challenge\\PyBank\\analysis\\PyBank-analysis.txt'

    with open(file_pathx,'w') as analysis_x:

        analysis_x.write(f'Months: {months}\n')

        analysis_x.write(f'Total: {total}\n')

        analysis_x.write(f'Average Change: {sum(profits_c)/(months-1)}\n')

        analysis_x.write(f'Greatest Increase: {increase}\n')

        analysis_x.write(f'Greatest Decrease: {decrease}')

    analysis_x.close()

csvfile.close()




