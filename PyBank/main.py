import csv
import os

# Files to load and output (Remember to change these)
file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("analysis", "budget_analysis.txt")

# Total Vote Counter
total = 0
sum = 0
sumchange = 0
# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as budget_data:
    reader = csv.reader(budget_data)

    # Read the header
    header = next(reader)
    firstrow = next(reader)

    previous =int(firstrow[1])
    sum = previous 
    total = 1
    # For each row...
    for row in reader:
        # print(row)
        total = total+1
    
        current = int(row[1])
        sum = sum+current
        change = current-previous
        sumchange = sumchange+change
        previous = current
    avgchange = sumchange/(total-1)    
    print(total)
    print(sum)
    print(avgchange)
    print(sumchange)
