from pathlib import Path
import csv

# create a file to csv file.
fp = Path.cwd() / 'PFB_grp_proj' / 'project_group' / 'cash on hand.csv'

# read the csv file to append from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) 

# create empty list to store cash on hand records
cash_on_hand = []
