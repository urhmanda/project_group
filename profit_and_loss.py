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

# Function to compute the difference in net profit and find the day and amount of the highest increment
def compute_difference_and_max_increment(file_path):
    net_profit_column = "Net Profit"
    net_profit_diff_column = "Net Profit Difference"

    data = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)

    # Convert net profit columns to numeric
    for row in data:
        for i in range(len(row)):
            if row[i].startswith("Day :"):
                row[i] = int(row[i].split("-")[-1].strip())
            elif "," in row[i]:
                row[i] = int(row[i].replace(",", ""))

    # Compute the difference in net profit
    for i in range(1, len(data)):
        data[i].append(data[i][data[0].index(net_profit_column)] - data[i - 1][data[0].index(net_profit_column)])

    # Find the day and amount of the highest increment
    max_increment_day = max(data[1:], key=lambda x: x[-1])
    max_increment_amount = max_increment_day[-1]

    return data, max_increment_day[0], max_increment_amount

# Get the result and print it
result, max_increment_day, max_increment_amount = compute_difference_and_max_increment('profit_and_loss.csv')
for row in result:
    print(row)

print("\nDay and amount of highest increment:")
print("Day:", max_increment_day)
print("Amount:", max_increment_amount)