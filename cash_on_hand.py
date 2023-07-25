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

for item in cash_on_hand:
    print(item)

# grp data all according to each day first
for item[0] in cash_on_hand:
    item[3] = 0
    if item[0] == :
        item[3] += item[3]
        #sum up all item[3] where item[0]= 90 and subsequent days
# use list

def calculate_difference_between_days(cash_on_hand):
     """
     - To calculate 
     """
     for item[3] in cash_on_hand:
        if item[3] <= item[3]:
           item[3] - item[3]
        elif item[3] >= item[3]:
            item[3] - item[3]
        else: 
# use panda or num.py
           
      
summary_list = []
summary_list.append(f"{items[0]},{calculate_difference_between_days})



