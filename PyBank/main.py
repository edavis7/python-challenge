import os

import csv

csvpath = os.path.join('budget_data.csv')

total_months = 0
total_amount = 0
average_change = 0
maxpercent = 0
minpercent = 0


with open(csvpath, newline = '') as csvfile:
    read_file = csv.reader(csvfile)
    # Read the header row first (skip this part if there is no header)
    csv_header = next(read_file)
    #print(csv_header)
    first_row = next(read_file)
    #print(first_row[0])
    #print(first_row[1])

    total_months = total_months + 1
    total_amount = total_amount + int(first_row[1])
    bank = []
    prev = int(first_row[1])

    for row in read_file:
        total_months += 1
        total_amount = total_amount + int(row[1])
        

        diff_prev = int(row[1]) - prev
        
        prev = int(row[1])
        bank.append(diff_prev)
        average_change = sum(bank)/len(bank)
        maxpercent = max(bank)
        minpercent = min(bank)

    print(total_months)       
    print(total_amount)   
    print(average_change)
    print(maxpercent)
    print(minpercent)

output_file = os.path.join('analysis', 'Budget_Analysis.txt')

with open("Budget_Analysis.txt","w") as text_file:
    print(f"Budget Analysis", file=text_file)
    print("----------------------------", file=text_file)
    print(f"Total Months: {total_months}", file=text_file) 
    print(f"Total: ${total_amount}", file=text_file)
    print(f"Average Change: ${average_change}", file=text_file) 
    print(f"Greatest Increase in Profits: {maxpercent}", file=text_file)
    print(f"Greatest Decrease in Profits: {minpercent}", file=text_file)