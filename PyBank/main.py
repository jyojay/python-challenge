# Modules
import os
import csv

#Setting file path
csvpath = os.path.join("Resources", "budget_data.csv")

# Initializing variables including list variables to store change in profit and corresponing date
total_months = 0
total_amount = 0
total_change = 0
profit_change = []
change_month = []

# Opening and Reading Budget data csv file
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header_row = next(csvreader)  # Header row stored 
    # Note: Variable assignment is not necessary here as we only want to skip the header but have used variable to fulfill assignment requirement
    
    prev_row = 0 # Initializing variable for storing previous month's profit

    # Lopping through all lines of csv data after header
    for current_row in csvreader:
        total_months += 1 # Counting the number of months
        total_amount += int(current_row[1]) # Adding up the value of profit for each line of data
        change = int(current_row[1]) - prev_row # Calculating the difference in profit between current and previous month
        profit_change.append(change) # Storing change in profit to a list
        change_month.append(current_row[0]) # Storing corresponding date to a list
        prev_row = int(current_row[1]) # Assigning value of current profit to previous month's for using to compare in next iteration 
    
    # Removing first value from lists for change in profit and corresponding month 
    # Note: First value of change in profit saved did not have an actual previous month's profit to calculate the difference hence this value was removed
    profit_change.pop(0)
    change_month.pop(0)
    
    # Initializing variables for Greatest increase and Greatest decrease
    greatest_increase = 0
    greatest_decrease = 0
    
    # Looping as many times as the length of profit_change list for finding Greatest increase and Greatest decrease in profit
    for x in range(len(profit_change)):
        total_change += profit_change[x] # Adding up the change in profits in a variable 
        
        # Finding Greatest increase
        if profit_change[x] > greatest_increase: 
            greatest_increase = profit_change[x]
            girow = x # Saving position of the Greatest increase value in the list

        # Finding Greatest decrease   
        if profit_change[x] < greatest_decrease: 
            greatest_decrease = profit_change[x]
            gdrow = x  # Saving position of the Greatest decrease value in the list 

    average_change = round((total_change/ len(profit_change)), 2) # Calculating average change in profit and rounding to 2 decimal places
      
# Printing analysis to terminal with required formatting
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

# Opening/Creating a result text file using "write" mode and writing in the analysis with required formatting
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