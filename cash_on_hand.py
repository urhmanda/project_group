# from pathlib import Path
# import csv

# # create a file to csv file.
# fp = Path.cwd() / 'csv_reports' / 'cash_on_hand.csv'

# # read the csv file to append from the csv.
# with fp.open(mode="r", encoding="UTF-8", newline="") as file:
#     reader = csv.reader(file)
#     next(reader) #To skip the header

#     # create empty list to store cash on_hand_records
#     cash_on_hand = []

#     # append cash on hand records into the cash_on_hand list
#     for row in reader:
#         """
#         - To get the data for each record
#         - and append relevant data(Day and Amount) to cash_on_hand list
#         """
#         cash_on_hand.append([row[0],row[3]])   

# cash_on_hand.sort(key = lambda record: int(record[0][90:]))

# for item in cash_on_hand:
#     print(item)

# # To store the number of days appended from cash_on_hand.csv into  cash_on_hand records
# days_set = set()

# for item in cash_on_hand:
#     """
#     - To calculate the number of days recorded in cash_on_hand
#     """
#     days_set.add(item[0])

# number_of_days = len(days_set)
# print("Number of days recorded:", number_of_days)

# sum_of_each_day = {}
# for item in cash_on_hand:
#     day = item[0]
#     amount = item[3]
#     if day not in sum_of_each_day:
#         """
#         - To add up current amount if day does not exist in cash_on_hand.csv
#         """
#         sum_of_each_day[day] = amount
#     else:
#         """
#         - To add amount to existing sum if day already exists in cash_on_hand.csv
#         """
#         sum_of_each_day[day] += amount


# def calculate_difference_between_days(cash_on_hand):
#      """
#      - To calculate the difference in amount (increase or decrease) between each day 
#      """
#      differences = []
#      for i in range(3, len(cash_on_hand)):
#          previous_amount = float(cash_on_hand[i-1][1])
#          current_amount = float(cash_on_hand[i][1])
#          difference = current_amount - previous_amount
#          differences.append(difference)
#          return differences
#      differences= calculate_difference_between_days(cash_on_hand)

# for i, difference in enumerate( calculate_difference_between_days, start = 3):
#     """
#     - To collate values calculated for the number of Days and the difference in amount between each of the days
#     """
#     print(f"Day {i}: Difference in Amount: {difference}")
  
# from pathlib import Path
# import csv

# # Create a file path to the CSV file.
# fp = Path.cwd() / 'csv_reports' / 'cash_on_hand.csv'

# # Read the CSV file to append from the CSV.
# with fp.open(mode="r", encoding="UTF-8", newline="") as file:
#     reader = csv.reader(file)
#     next(reader)  # To skip the header

#     # Create a dictionary to store cash on hand records for each day
#     cash_on_hand = {}

#     # Append cash on hand records into the cash_on_hand dictionary
#     for row in reader:
#         day = row[0]
#         amount = row[3]

#         # Check if the amount is numeric or not
#         if not amount.replace('.', '', 1).isdigit():
#             # If the amount is non-numeric, ignore it and continue to the next record
#             continue

#         amount = float(amount)

#         if day not in cash_on_hand:
#             cash_on_hand[day] = amount
#         else:
#             cash_on_hand[day] += amount

# # Sort the list based on the day
# sorted_cash_on_hand = sorted(cash_on_hand.items(), key=lambda item: item[0])

# # Calculate the differences in Cash-on-Hand between each day
# differences = [sorted_cash_on_hand[i][1] - sorted_cash_on_hand[i - 1][1] for i in range(1, len(sorted_cash_on_hand))]

# # Track the highest increment and its corresponding day and amount
# highest_increment = max(differences)
# highest_increment_index = differences.index(highest_increment)
# highest_increment_day = sorted_cash_on_hand[highest_increment_index + 1][0]
# highest_increment_amount = sorted_cash_on_hand[highest_increment_index + 1][1]

# number_of_days = len(sorted_cash_on_hand)
# print("Number of days recorded:", number_of_days)

# for i, difference in enumerate(differences, start=1):
#     print(f"Day {i}: Difference in Amount: {difference}")

# print(f"\nHighest Increment:")
# print(f"Day: {highest_increment_day}")
# print(f"Amount: {highest_increment_amount}")

# from pathlib import Path
# import csv

# # Create a file path to the CSV file.
# fp = Path.cwd() / 'csv_reports' / 'cash_on_hand.csv'

# # Read the CSV file to append from the CSV.
# with fp.open(mode="r", encoding="UTF-8", newline="") as file:
#     reader = csv.reader(file)
#     next(reader)  # To skip the header

#     # Create a dictionary to store cash on hand records for each day
#     cash_on_hand = {}

#     # Append cash on hand records into the cash_on_hand dictionary
#     for row in reader:
#         day = row[0]
#         amount = row[3]

#         # Check if the amount is numeric or not
#         if not amount.replace('.', '', 1).isdigit():
#             # If the amount is non-numeric, ignore it and continue to the next record
#             continue

#         amount = float(amount)

#         if day not in cash_on_hand:
#             cash_on_hand[day] = amount
#         else:
#             cash_on_hand[day] += amount

# # Generate a list of all possible days within the range (1 to 90)
# all_days = [str(day) for day in range(1, 91)]

# # Sort the list based on the day
# sorted_cash_on_hand = sorted(cash_on_hand.items(), key=lambda item: item[0])

# # Calculate the differences in Cash-on-Hand between each day
# differences = []
# current_cash = 0.0

# for day in all_days:
#     if day in cash_on_hand:
#         current_cash = cash_on_hand[day]
#     differences.append(current_cash)

# # Calculate the differences in Cash-on-Hand between each day
# differences = [differences[i] - differences[i - 1] for i in range(1, len(differences))]

# # Track the highest increment and its corresponding day and amount
# highest_increment = max(differences)
# highest_increment_index = differences.index(highest_increment)
# highest_increment_day = all_days[highest_increment_index + 1]
# highest_increment_amount = cash_on_hand[highest_increment_day]

# number_of_days = len(all_days)
# print("Number of days recorded:", number_of_days)

# for i, difference in enumerate(differences, start=1):
#     print(f"Day {i}: Difference in Amount: {difference}")

# print(f"\nHighest Increment:")
# print(f"Day: {highest_increment_day}")
# print(f"Amount: {highest_increment_amount}")

from pathlib import Path
import csv

# Create a file path to the CSV file.
fp = Path.cwd() / 'csv_reports' / 'cash_on_hand.csv'

# Read the CSV file to append from the CSV.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)  # To skip the header

    # Create a dictionary to store cash on hand records for each day
    cash_on_hand = {}

    # Append cash on hand records into the cash_on_hand dictionary
    for row in reader:
        day = row[0]
        amount = row[3]

        # Check if the amount is numeric or not
        if not amount.replace('.', '', 1).isdigit():
            # If the amount is non-numeric, ignore it and continue to the next record
            continue

        amount = float(amount)

        if day not in cash_on_hand:
            cash_on_hand[day] = amount
        else:
            cash_on_hand[day] += amount

# Generate a list of all possible days within the range (0 to 90)
all_days = [str(day) for day in range(0, 91)]

# Sort the list based on the day
sorted_cash_on_hand = sorted(cash_on_hand.items(), key=lambda item: item[0])

# Calculate the differences in Cash-on-Hand between each day
differences = []
current_cash = 0.0

for day in all_days:
    if day in cash_on_hand:
        current_cash = cash_on_hand[day]
    differences.append(current_cash)

# Calculate the differences in Cash-on-Hand between each day
differences = [differences[i] - differences[i - 1] for i in range(1, len(differences))]

# Track the highest increment and its corresponding day and amount
highest_increment = max(differences)
highest_increment_index = differences.index(highest_increment)
highest_increment_day = all_days[highest_increment_index + 1]
highest_increment_amount = cash_on_hand[highest_increment_day]

number_of_days = len(all_days)
print("Number of days recorded:", number_of_days)

for i, difference in enumerate(differences, start=1):
    print(f"Day {i}: Difference in Amount: {difference}")

print(f"\nHighest Increment:")
print(f"Day: {highest_increment_day}")
print(f"Amount: {highest_increment_amount}")