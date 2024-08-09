# Import dependencies

import os
import csv
 
# File path

pyBank_csv = os.path.join("Resources", "budget_data.csv")
 
# Initialize variables to zero

total_months = 0
total_profit_losses = 0
previous_profit_losses = 0

# Create empty lists to store data

changes = []
dates = []
 
# Open the CSV file

with open(pyBank_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
 
    # Skip the header row
    next(csv_reader)
 
    # Loop through each row in the CSV file

    for row in csv_reader:
        date = row[0]
        profit_loss = int(row[1])
 
        # Count total months

        total_months += 1
 
        # Calculate total profit/losses

        total_profit_losses += profit_loss
 
        # Calculate change in profit/losses &
        # Append values to the lists "changes" and "dates"
        if total_months > 1:
            change = profit_loss - previous_profit_losses
            changes.append(change)
            dates.append(date)
 
        previous_profit_losses = profit_loss
 
# Calculate the average change

average_change = sum(changes) / len(changes)
 
# Find greatest increase and greatest decrease

greatest_increase = max(changes)
greatest_decrease = min(changes)
increase_date = dates[changes.index(greatest_increase)]
decrease_date = dates[changes.index(greatest_decrease)]
 


# Print the analysis to the terminal

print("") #insert empty line
print("Financial Analysis")
print("--------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})")



# Export the analysis to a text file

output_path = os.path.join("analysis", "financial_analysis.txt")
with open(output_path, 'w') as txtfile:    
    txtfile.write("Financial Analysis\n")
    txtfile.write("--------------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total_profit_losses}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {increase_date} (${greatest_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})\n")
 
