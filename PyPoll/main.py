# Modules
import os
import csv

# Setting file path
csvpath = os.path.join("Resources", "election_data.csv")

# Initializing variables including dictionary to store unique candidate name and correesponding total votes
total_votes = 0
candidate_votes = {}

# Opening and Reading election data csv file
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)  # Header row skipped
    
    # Looping through all lines of csv data after header
    for current_row in csvreader:
        total_votes += 1 # Counting the total votes

        # If the current candidate name is not in candidate_votes dictionary already then adding it as a key with value 0
        if current_row[2] not in candidate_votes:
            candidate_votes[current_row[2]] = 0
        
        # Incrementing the value of votes aginst current candidate by one in the dictionary
        candidate_votes[current_row[2]] += 1  

candidate_name = list(candidate_votes.keys()) # creating a list of all keys from the dictionary
candidate_totalvotes = list(candidate_votes.values()) # creating a list of all values from the dictionary

max_votes = 0 # Initializing variable for finding highest vote number

# Looping as many times as the length of list with total votes of each candidate for finding Winner
for x in range(len(candidate_totalvotes)):
    if candidate_totalvotes[x] > max_votes:
        max_votes = candidate_totalvotes[x]
        row_max = x # Saving position of the highest votes in the list 

percent_votes = [] # List initialised for saving all values of percentage of votes

# Printing analysis to terminal with required formatting
print('')
print('Election Results')
print('')
print('---------------------------------------------------')
print('')
print(f"Total votes = {total_votes}")
print('')
print('---------------------------------------------------')
print('') 
# Loopimg to print the list of candidates with corresponding percentage and total number of votes
for candidate in range(len(candidate_name)):
    # Calculating percent of votes and saving to a list. Value rounded to 3 decimal places
    percent_votes.append(round(candidate_totalvotes[candidate]*100/total_votes,3))
    print(f"{candidate_name[candidate]}: {percent_votes[candidate]}% ({candidate_totalvotes[candidate]})")
print('')
print('---------------------------------------------------')
print('') 
print(f"Winner: {candidate_name[row_max]}") 
print('')
print('---------------------------------------------------')
print('') 

# Opening/Creating a result text file using "write" mode and writing in the anaylsis 
output_path = os.path.join("analysis", "result.txt")
with open(output_path, 'w') as result:
    result.write('\n')
    result.write('Election Results\n')
    result.write('\n')
    result.write('---------------------------------------------------\n')
    result.write('\n')
    result.write(f"Total votes = {total_votes}\n")
    result.write('\n')
    result.write('---------------------------------------------------\n')
    result.write('\n')
    # Loopimg to write to file the list of candidates with corresponding percentage and total number of votes
    for candidate in range(len(candidate_name)):
        result.write(f"{candidate_name[candidate]}: {percent_votes[candidate]}% ({candidate_totalvotes[candidate]})\n")
    result.write('\n')
    result.write('---------------------------------------------------\n')
    result.write('\n')
    result.write(f"Winner: {candidate_name[row_max]}\n") 
    result.write('\n')
    result.write('---------------------------------------------------\n')
    result.write('\n')