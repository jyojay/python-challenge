# Modules
import os
import csv

#Setting file path
csvpath = os.path.join("Resources", "election_data.csv")

#Intializing variables
total_votes = 0
candidate_votes = {}

#Opening and Reading election data file
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)  # Header row
    
    for current_row in csvreader:
        total_votes += 1
        if current_row[2] not in candidate_votes:
            candidate_votes[current_row[2]] = 0
        candidate_votes[current_row[2]] += 1  

#max_votes = max(candidate_votes, key = candidate_votes.get) --- Method 1
#max_votes = next(iter(candidate_votes))  ----- Method 2
# for key in candidate_votes:
#     if candidate_votes[key] > candidate_votes[max_votes]:
#         max_votes = key
#print(candidate_votes)
# print(max_votes)

candidate_name = list(candidate_votes.keys())
candidate_totalvotes = list(candidate_votes.values())
max_votes = 0
for x in range(len(candidate_totalvotes)):
    if candidate_totalvotes[x] > max_votes:
        max_votes = candidate_totalvotes[x]
        row_max = x
#print(candidate_name[row_max])
percent_votes = []
# Printing analysis to terminal 
print('')
print('Election Results')
print('')
print('---------------------------------------------------')
print('')
print(f"Total votes = {total_votes}")
print('')
print('---------------------------------------------------')
print('') 
for candidate in range(len(candidate_name)):
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
    for candidate in range(len(candidate_name)):
        result.write(f"{candidate_name[candidate]}: {percent_votes[candidate]}% ({candidate_totalvotes[candidate]})\n")
    result.write('\n')
    result.write('---------------------------------------------------\n')
    result.write('\n')
    result.write(f"Winner: {candidate_name[row_max]}\n") 
    result.write('\n')
    result.write('---------------------------------------------------\n')
    result.write('\n')