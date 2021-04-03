#==================
# PyBank Challenge - create analysis of financial data that exports to a csv file
#==================
    
# csv file output and analysis printed to terminal to include:
# total number of months in the dataset and total "Profit/Losses" over the time period
# calculate changes in profit/loss and average of those changes
# date and amount of greatest increase and greatest decrease in profits
 

# begin with import of os and csv modules
import os
import csv

# identify the path to the resource file stored in PyBank
csv_path = os.path.join('.', 'Resources', 'budget_data.csv')

# temporarily put the data from the file to a variable file_handler
with open(csv_path) as file_handler:
  
    # create a variable to use csv.reader functionality and id what seperates the fields in the dataset
    csv_reader = csv.reader(file_handler, delimiter=',')
    
    # move to the row beneath the header to begin analysis of data
    csv_header = next(csv_reader)
    
    # create a list from the csv file data to analyze the profits/losses
    profits_list = []
    
    # create variables and set counters to 0 for number of months, sum of profits/losses
    total_profit = 0  
    months = 0 
    
    # create variables and set counter for the changes in value and average
    inc = ['',0]
    dec = ['',10000000]
    
    #change_avg = 0; calculated by alternate method
    
    # create a loop through the rows to be able to make calculations
    for i,row in enumerate(csv_reader):
        
        profit = int(row[1])
        months += 1
        
        # where i == 0 set change to 0 (during month one), as starting point
        if i == 0:
            prev_profit = profit
        
        # as loop progresses each change is profit for that row minus the previous row's profit
        change = profit - prev_profit

        # once change is stored then update prev-profit to current profit before move to next row        
        prev_profit = profit
        
        #change_avg += change; calculated average change by alternate method

        if change > inc[1]:
            inc[0] = row[0]
            inc[1] = change
        
        if change < dec[1]:
            dec[0] = row[0]
            dec[1] = change

        profits_list.append(profit)
               
        # find the sum of all the profits by adding to total as loop through the rows 
        total_profit += profit
     
     # identify the total amount of change from 1st month to last month of the data set   
        start_value = profits_list[0]

        final_value = profits_list[-1]
    
    # average change will be total_value_change divided by the number of changes (months) that occurred
    # number of changes occuring is months - 1   
    total_value_change = int(final_value) - int(start_value)
    average_change = (total_value_change / (months - 1))
    round_average = round(average_change, 2)
    
    #create a variable for output, that will be printed to terminal and exported to a file
    output = f'Financial Analysis\n------------------\n'    
    
    # use len to get number of months (row 2 of csv to end), add result to planned output
    output += f"Total months: {len(profits_list)}\n"
    
    # format values and add lines to output 
    #output += f"Total Profit/Losses: ${total_profit:,}\n"
    output += f"Total Profit/Losses: ${total_profit}\n"
    output += f"Average Change: ${round_average}\n"
    
    # find the max and min values of change in value, format, and add to output
    #output += f"Greatest Increase in Profits: {inc[0]} (${inc[1]:,})\n"
    #output += f"Greatest Decrease in Profits: {dec[0]} (${dec[1]:,})\n"

    output += f"Greatest Increase in Profits: {inc[0]} (${inc[1]})\n"
    output += f"Greatest Decrease in Profits: {dec[0]} (${dec[1]})\n"

# print output to terminal
print(output)

# write output lines to csv in Analysis folder
output_path = os.path.join(".", "Analysis", "analysis.csv")

with open(output_path, 'w', newline='') as data_file:

    data_file.write(output) 