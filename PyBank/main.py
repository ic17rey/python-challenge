#==================
# PyBank Challenge - create analysis of financial data that exports to a csv file
#==================
    
    # output csv file to include:
    # total number of months in the dataset
    # net total of "Profit/Losses" over the time period
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

    #move to the row beneath the header to begin analysis of data
   
    months = csv_reader.line_num
    csv_header = next(csv_reader)
    
    #print(csv_header)
    
    for row in csv_reader:
        
        #test the file path to budget_data.csv
        #print(row[0])
        months += 1
    
    print("Total months: " + str(months))