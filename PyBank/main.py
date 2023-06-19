# Modules
import os
import csv

#Setting file path
csvpath = os.path.join("Resources", "budget_data.csv")

#Intializing variables
total_months = 0
total_amount = 0
total_change = 0
profit_change = []
change_month = []

#Opening and Reading Budget data file
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)  # Header row
    
    prev_row = 0
    for current_row in csvreader:
    
        total_months += 1
        total_amount += int(current_row[1])
        change = int(current_row[1]) - prev_row
        profit_change.append(change)
        change_month.append(current_row[0])
        prev_row = int(current_row[1])
    
    profit_change.pop(0)
    change_month.pop(0)
    greatest_increase = 0
    greatest_decrease = 0
    for x in range(len(profit_change)):
        total_change += profit_change[x]
        if profit_change[x] > greatest_increase:
            greatest_increase = profit_change[x]
            girow = x
        if profit_change[x] < greatest_decrease: 
            greatest_decrease = profit_change[x]
            gdrow = x   

    average_change = round((total_change/ (total_months - 1)), 2)

# Printing analysis to terminal 
print('')
print('Financial Analysis')
print('')
print('---------------------------------------------------')
print('')
print(f"Total months = {total_months}")   
print(f"Total amount = ${total_amount}") 
print(f"Average Change = ${average_change}")
print(f"Greatest Increase = {change_month[girow]} (${greatest_increase})")
print(f"Greatest Decrease = {change_month[gdrow]} (${greatest_decrease})")
print('')

# Opening/Creating a result text file using "write" mode and writing in the anaylsis 
output_path = os.path.join("analysis", "result.txt")
with open(output_path, 'w') as result:
    result.write('\n')
    result.write('Financial Analysis\n')
    result.write('\n')
    result.write('---------------------------------------------------\n')
    result.write('\n')
    result.write(f"Total months = {total_months}\n")   
    result.write(f"Total amount = ${total_amount}\n") 
    result.write(f"Average Change = ${average_change}\n")
    result.write(f"Greatest Increase = {change_month[girow]} (${greatest_increase})\n")
    result.write(f"Greatest Decrease = {change_month[gdrow]} (${greatest_decrease})\n")