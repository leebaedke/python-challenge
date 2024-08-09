# Import dependencies

import os
import csv
from collections import Counter


# File path
pyPoll_csv = os.path.join("Resources", "election_data.csv")

# Initialize variable
total_votes = 0

# Create empty lists 
candidates = []
results = []

# Create an empty counter
vote_counts = Counter()



# Read the CSV file
with open(pyPoll_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header row
    next(csv_reader)

    # Process each row in the CSV file
    for row in csv_reader:
        total_votes += 1
        candidate = row[2]
        candidates.append(candidate)
        vote_counts[candidate] += 1

# Calculate results
 
for candidate, votes in vote_counts.items():
    percentage = (votes / total_votes) * 100
    results.append((candidate, votes, percentage))

# Sort results by number of votes (descending)
results.sort(key=lambda x: x[1], reverse=True)

# Determine the winner
winner = results[0][0]


# Print the results to the terminal

print("") #insert empty line
print("Election Results")
print("----------------------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------------------")
for candidate, votes, percentage in results:
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("----------------------------------------")    
print(f"Winner: {winner}")
print("----------------------------------------")


# Export results to a text file

output_path = os.path.join("analysis", "election_results.txt")
with open(output_path, 'w') as txtfile:
    txtfile.write("") #insert empty line
    txtfile.write("\nElection Results\n")
    txtfile.write("----------------------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("----------------------------------------\n")
    for candidate, votes, percentage in results:
        txtfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    txtfile.write("----------------------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("----------------------------------------\n")








