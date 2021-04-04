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
csv_path = os.path.join('Resources', 'budget_data.csv')

# temporarily put the data from the file to a variable file_handler
with open(csv_path) as file_handler:
  
    # create a variable to use csv.reader functionality and id what seperates the fields in the dataset
    csv_reader = csv.reader(file_handler, delimiter=',')
    
    # move to the row beneath the header to begin analysis of data
    csv_header = next(csv_reader)
    #first_row
    # create a list from the csv file data to analyze the profits/losses
    profits_list = []
    
    for row in csv_reader:
        profits_list.append(row[1])
        
        # find starting value for profits
        profit_month1 = profits_list[0]
        # find final value for profits (last row profits value)
        final_profits = profits_list[-1]
    
    #print(profit_month1)
    #print(final_profits)
    
    # find overall profit or loss over the months in the data set
    total = int(final_profits) - int(profit_month1) 

    # find the number of months involved
    total_months = len(profits_list)

    #print(total_months)
    #prints above all hold the correct values
    
    # calculate the incremental changes in profit value to find greatest increase and greatest decrease
# temporarily put the data from the file to a variable file_handler
with open(csv_path) as file_handler:
  
    # create a variable to use csv.reader functionality and id what seperates the fields in the dataset
    csv_reader = csv.reader(file_handler, delimiter=',')
    
    # move to the row beneath the header to begin analysis of data
    csv_header = next(csv_reader)
    months = 0
    total_profit = 0
    
    # prev_profit initialized as the first month's profit, other variables initialized to 0
    prev_profit = profit_month1
    current_profit = 0
    change_in_profit = 0
    average_change = 0
    round_average = 0
    
    # create a list to hold the changes in profits/losses
    change_in_profit_list = []
    # print prev_profit, to ensure equal to 867884 (first month profit)
    
    for row in csv_reader:
        #determine the change in the profit
        months += 1
        total_profit += int(row[1])
        #change_in_profit_list.append(int(row[1]) 
        #- int(prev_profit))

#change_in_profit = int(current_profit) - int(prev_profit)
    #print(change_in_profit)

        #to update profit amount to go through next loop
        #current_profit = prev_profit     
        #change_in_profit_list.append(row)
         

        #profit_change = int(row[1]) - prev_profit

    # still working to understand the change in profits
    # create variables and set counters to 0 for number of months, sum of profits/losses
    #total_profit = 0  
    #months = 0 
    
    # create variables and set counter for the changes in value and average
    # inc = ['',0]
    # dec = ['',10000000]
    
    # #change_avg = 0; calculated by alternate method
    
    # # create a loop through the rows to be able to make calculations
    # # need to store the calculated values as a list to be able to find max and min?
    # for i,row in enumerate(csv_reader):
        
    #     profit = int(row[1])
    #     months += 1
        
    #     # where i == 0 set change to 0 (during month one), as starting point
    #     if i == 0:
    #         prev_profit = profit
        
    #     # as loop progresses each change is profit for that row minus the previous row's profit
    #     change = profit - prev_profit

    #     # once change is stored then update prev-profit to current profit before move to next row        
    #     prev_profit = profit
        
    #     #change_avg += change; calculated average change by alternate method

    #     if change > inc[1]:
    #         inc[0] = row[0]
    #         inc[1] = change
        
    #     if change < dec[1]:
    #         dec[0] = row[0]
    #         dec[1] = change

    #     profits_list.append(profit)
              
    #     # find the sum of all the profits by adding to total as loop through the rows 
    #     total_profit += profit           
    
    # calculate the average change and round to two decimal places
    average_change = round(total / (total_months - 1), 2)
    print(average_change)

    #create a variable for output, that will be printed to terminal and exported to a file
    output = f'Financial Analysis\n------------------\n'    
    
    # use len to get number of months (row 2 of csv to end), add result to planned output
    output += f'Total months: {len(profits_list)}\n'
    
    # format values and add lines to output 
    #output += f'Total Profit/Losses: ${total_profit:,}\n'
    
    output += f'Total Profit/Losses: ${total_profit}\n'
    output += f'Average Change: ${average_change}\n'
    
    # find the max and min values of change in value, format, and add to output
    # adding the commas alters output file
    #output += f'Greatest Increase in Profits: {inc[0]} (${inc[1]:,})\n'
    #output += f'Greatest Decrease in Profits: {dec[0]} (${dec[1]:,})\n'

    #output += f'Greatest Increase in Profits: {inc[0]} (${inc[1]})\n'
    #output += f'Greatest Decrease in Profits: {dec[0]} (${dec[1]})\n'

# print output to terminal
print(output)

# write output lines to csv in Analysis folder
output_path = os.path.join('.', 'Analysis', 'analysis.csv')

with open(output_path, 'w', newline='') as data_file:

    data_file.write(output)     