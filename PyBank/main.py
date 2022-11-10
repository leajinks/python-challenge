# Module 3 Challenge - PyBank

# Import module to create file path across OS's
import os

# Import module for reading CSV files
import csv

# Set file location of csv file
budget_csv = os.path.join("Resources", "budget_data.csv")

# Lists and variables to store data
total_profits = []
total_profits = 0
profit_change = []
row_count = 0
greatest_increase = 0
greatest_decrease = 0


# Open csv file
with open(budget_csv, encoding='utf-8') as budget:

    # store csv data in a reader "csvreader" and specify delimiter
    csvreader = csv.reader(budget, delimiter=',')

    # skip column headers
    next(csvreader)

    # set first row as row after header
    first_row = next(csvreader)

    # define initial variables before loop begins
    row_count = row_count + 1
    total_profits += int(first_row[1])
    previous_profits = int(first_row[1])

    # loop thru rows to calculate net total of profits/losses
    for row in csvreader:
        total_profits += int(row[1])
    
        # Calculate changes in profit/losses over the entire period (net change)
        # ignore first row for previous profits since there are none
        previous = 0 if row_count == 0 else previous_profits 
        net_change = int(row[1]) - previous
        previous_profits = int(row[1])
        profit_change.append(net_change)
      
        
         # The greatest increase in profits (date and amount) over the entire period
         # use change rather than profit
        if int(net_change) > greatest_increase:
          maxmonth = (row[0])
          greatest_increase = int(net_change) 
        elif (int(net_change)) < greatest_decrease:
          minmonth = (row[0])
          greatest_decrease = (int(net_change))

        # increment row count by 1
        row_count = row_count + 1


    # Calculate average change - number of changes is 85 not 86
    avg_profit_change = (sum(profit_change)/(row_count - 1))


# Output
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {row_count}\n"
    f"Total: ${total_profits}\n"
    f"Average Change: ${avg_profit_change}\n"
    f"Greatest increase in profits: {maxmonth}, ${greatest_increase}\n"
    f"Greatest decrease in profits: {minmonth}, ${greatest_decrease}\n"
)
print(output)



# Export text file with results
f = open("financial_analysis.txt", "w")
f.write(output)

