# Module 3 Challenge - PyPoll

# Import module to create file path across OS's
import os

# Import module for reading CSV files
import csv

# Set file location of csv file
election_csv = os.path.join("Resources", "election_data.csv")

# Lists and variables to store data
candidate = ""
candilist = []
row_count = 0
candipercent = 0
vote_count = 0

# Open csv file
with open(election_csv, encoding='utf-8') as election:

    # store csv data in a reader "csvreader" and specify delimiter
    csvreader = csv.reader(election, delimiter=',')

    # skip column headers
    next(csvreader)

    # set first row as row after header
    first_row = next(csvreader)

    # define initial variables before loop begins
    row_count = row_count + 1
    CCSvote = 0
    DGvote = 0
    RADvote = 0

    # loop thru rows
    for row in csvreader:
        
        # create a list of all votes for each candidate
        candidate = row[2]

        #if candidate not already in list, put them there
        if candidate not in candilist:
            candilist.append(candidate)

        #tally votes for each candidate
        if candidate == "Charles Casper Stockham":
            CCSvote = CCSvote + 1
        elif candidate == "Diana DeGette":
            DGvote = DGvote + 1
        else:
            RADvote = RADvote + 1

        row_count = row_count + 1

    # calculate percentages:
    CCSpercentage = CCSvote/row_count
    DGpercentage = DGvote/row_count
    RADpercentage = RADvote/row_count

    #Winner = max vote count
  

# Output
output = (
    f"Election Results\n"
    f"----------------------------\n"
    f"Total Votes: {row_count}\n"
    f"Charles Casper Stockham: {CCSpercentage}% {CCSvote}\n"
    f"Diana DeGette: {DGpercentage}% {DGvote}\n"
    f"Raymon Anthony Doane: {RADpercentage}% {RADvote}\n"
    f"----------------------------\n"
    f"Winner: Diana DeGette\n"
    f"----------------------------\n"
)
print(output)



# Export text file with results
f = open("election_analysis.txt", "w")
f.write(output)

