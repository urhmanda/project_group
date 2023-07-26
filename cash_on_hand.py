from pathlib import Path
import csv

# create a file to csv file.
fp = Path.cwd() / 'csv_reports' / 'cash_on_hand.csv'

# read the csv file to append from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) #To skip the header

    # create empty list to store cash on hand records
    cash_on_hand = []

    # append cash on hand records into the cash_on_hand list
    for row in reader:
        """
        - To get the data for each record
        - and append relevant data(Day and Amount) to cash_on_hand list
        """
        cash_on_hand.append([row[0],row[3]])   

cash_on_hand.sort(key = lambda record: float(record[0][90:]))

for item in cash_on_hand:
    print(item)

# To store the number of days
days_set = set()

for item in cash_on_hand:
    """
    - To calculate the number of days recorded in cash_on_hand
    """
    days_set.add(item[0])

number_of_days = len(days_set)
print("Number of days recorded:", number_of_days)

sum_of_each_day = {}
for item in cash_on_hand:
    day = item[0]
    amount = item[3]
    if day not in sum_of_each_day:
        """
        - To add up current amount if day does not exist in cash_on_hand.csv
        """
        sum_of_each_day[day] = amount
    else:
        """
        - To add amount to existing sum if day already exists in cash_on_hand.csv
        """
        sum_of_each_day[day] += amount


def calculate_difference_between_days(cash_on_hand):
     """
     - To calculate the difference in amount (increase or decrease) between each day 
     """
     differences = []
     for i in range(3, len(cash_on_hand)):
         previous_amount = float(cash_on_hand[i-1][1])
         current_amount = float(cash_on_hand[i][1])
         difference = current_amount - previous_amount
         differences.append(difference)
         return differences
     differences= calculate_difference_between_days(cash_on_hand)

for i, difference in enumerate( calculate_difference_between_days, start = 3):
    """
    - To collate values calculated for the number of Days and the difference in amount between each of the days
    """
    print(f"Day {i}: Difference in Amount: {difference}")