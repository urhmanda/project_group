from pathlib import Path
import csv

# create a file to csv file.
fp = Path.cwd()/"csv_reports"/"overhead.csv"

# read the csv file to append from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty lists to store overhead record
    overhead = []

    # append overhead record into the overhead list
    for row in reader:
        #get the day, items and amount for each record
        #and append the overhead list
        overhead.append([row[0],row[1],row[3]])   

print(overhead)
