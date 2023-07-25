from pathlib import Path
import csv

# create a file to csv file.
fp = Path.cwd() / 'csv_reports' / 'cash_on_hand.csv'

# read the csv file to append from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) 

    # create empty list to store cash on hand records
    cash_on_hand = []

    # append cash on hand records into the cash_on_hand list
    for row in reader:
        # get the yea for each record
        #and append the cash_on_hand list
        cash_on_hand.append([row[0],row[1],row[2],row[3]])   

print("hi")