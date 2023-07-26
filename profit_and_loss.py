# from pathlib import Path
# import csv

# fp = Path.cwd()/"profit and loss.csv"

# with fp.open(mode="r", encoding="UTF-8", newline="") as file:
#     reader = csv.reader(file)
#     next(reader) #To skip the header

# #Creates an empty list to store profit and loss records
# profit_and_loss=[]

# #append profit and loss onto the profit and loss records
# for row in reader:
#     profit_and_loss.append

import csv
import requests

def compute_difference_and_max_increment(csv_url):
    response = requests.get(csv_url)
    lines = response.text.splitlines()

    # Assuming the first line contains the column headers
    csv_reader = csv.DictReader(lines[1:])

    data = list(csv_reader)

    # Convert numeric values from strings to integers
    for row in data:
        for key, value in row.items():
            if value.isnumeric():
                row[key] = int(value.replace(',', ''))

    # Compute the difference in the net profit column
    net_profit_values = [row['Net Profit'] for row in data]
    difference_in_net_profit = [net_profit_values[i] - net_profit_values[i-1] for i in range(1, len(net_profit_values))]

    # Find the day and amount of the highest increment
    max_increment_amount = max(difference_in_net_profit)
    max_increment_day = difference_in_net_profit.index(max_increment_amount) + 1

    return difference_in_net_profit, max_increment_day, max_increment_amount

# GitHub raw CSV URL
csv_url = 'https://raw.githubusercontent.com/urhmanda/project_group/main/csv_reports/profit_and_loss/profit_and_loss.csv'

# Call the function with the GitHub raw CSV URL
result, max_increment_day, max_increment_amount = compute_difference_and_max_increment(csv_url)

print("Difference in Net Profit Column:", result)
print("Day of Highest Increment:", max_increment_day)
print("Amount of Highest Increment:", max_increment_amount)