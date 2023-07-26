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
        # get the data for each record
        #nand append relevant data(Day and Amount) to cash_on_hand list
        cash_on_hand.append([row[0],row[3]])   

cash_on_hand.sort(key = lambda record: int(record[0][90:]))

for item in cash_on_hand:
    print(item)

days = []
currentamount = ""

for item in cash_on_hand:
    """
    - To calculate the number of days recorded in salesRecords
    """
    if (item[0] != days):
        days.append([])
        print("yes")
        currentEmpId = item[0]
    item[-1].append(item)

summary_list =[]

for item[0] in cash_on_hand:
    """
    - To sum up amount for each day 
    """
    item[0] = 0
    item[3] = 0
    if item[0] >= 90:
        item[3] += item[3]
        #sum up all item[3] where item[0]= 90 and subsequent days
# use list

def calculate_difference_between_days(cash_on_hand):
     """
     - To calculate the difference in amount (increase or decrease) between each day 
     """
     for item[3] in cash_on_hand:
        if item[3] <= item[3]:
           item[3] - item[3]
        elif item[3] >= item[3]:
            item[3] - item[3]
        else: 
# use panda or num.py
           
      
summary_list.append(f"{item[0]},{calculate_difference_between_days})