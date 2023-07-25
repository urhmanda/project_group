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

for items in cash_on_hand:
    print(items)

# grp data all according to each day first
for items[0] in cash_on_hand:
    if items[0] == 90:
        #sum up all items[3] where items[0]= 90 and subsequent


def calculate_difference_between_days(cash_on_hand):
     """
     - To calculate 
     """
     for items[3] in cash_on_hand:
        if items[3] <= items[3]:
           items[3] - items[3]
        elif items[3] >= items[3]:
            items[3] - items[3]
        else: 

           
      
summary_list = []
summary_list.append(f"{items[0]},{calculate_difference_between_days})



