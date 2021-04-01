#==================
# PyBank Challenge - create analysis of financial data that exports to a csv file
#==================
    
    # output csv file to include:
    # total number of months in the dataset
    # net total of "Profit/Losses" over the time period
    # calculate changes in profit/loss and find the average of those changes
    # date and amount of greatest increase in profits
    # date and amount of the greatest decrease
    # print analysis to the terminal and export to the output csv file

# begin with import of os and csv modules
import os
import csv

# identify the path to the resource file stored in PyBank
csv_path = os.path.join('.', 'Resources', 'budget_data.csv')

# use the csv module to read the file
with open(csv_path) as filehandler:

    csv_reader = csv.reader(filehandler, delimiter=',')
    
    csv_header = next(csv_reader)

    profits = 0

    for row in csv_reader:
        
    # to grab the count of rows in the csv file (subtract 1 for the header row)
        months = csv_reader.line_num - 1
        
        profits += int(row[1])
           
    print("Total months: " + str(months))
    print("Total Profit/Losses: $" + str(profits))
    
with open(csv_path) as filehandler:
  
    csv_reader = csv.reader(filehandler, delimiter=',')
    
    # move to the row beneath the header to begin analysis of data
    csv_header = next(csv_reader)
    
    # create a list from the csv file to analyze the profits/losses
    profits_list = []
       
    for row in csv_reader:
        print(row[1])
        profits_list.append(row[1])       
        