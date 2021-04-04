#==================
# PyPoll Challenge - create analysis of election data that exports to csv file
#==================
    
# csv file output and analysis printed to terminal to include:
# total number of votes cast and list of candidates who received votes
# percentage of votes and number of votes each candidate won 
# winner of election from the popular vote
   
# begin with import of os and csv modules
import os
import csv

# identify the path to the resource file stored in PyBank
csv_path = os.path.join('.', 'Resources', 'election_data.csv')

# use the csv module to read the file
with open(csv_path) as file_handler:
    
    csv_reader = csv.reader(file_handler, delimiter=',')

    # move to the row beneath the header to begin analysis of data
    csv_header = next(csv_reader)

    # create a list to be used to analyze election_data.csv contents
    votes_list = []

    for row in csv_reader:
        
        votes_list.append(row[0])
        
    output = f'Election Results\n-----------------\n'
    output += f"Total Votes: {(len(votes_list))}\n"


# want to start a dictionary for votes_cast

votes_cast = {}

with open(csv_path) as file_handler:

    csv_reader = csv.reader(file_handler, delimiter=',')

    # move to the row beneath the header to begin analysis of data
    csv_header = next(csv_reader)

    for row in csv_reader:
        if row[2] not in votes_cast:
            votes_cast[row[2]] = 0
        votes_cast[row[2]] += 1


print(output)

# write output lines to csv in Analysis folder
output_path = os.path.join("Analysis", "analysis.csv")

with open(output_path, 'w', newline='') as data_file:

    data_file.write(output)



    
