from pathlib import Path
import csv

# create a file to csv file.
fp = Path.cwd()/"csv_reports"/"overhead.csv"

# read the csv file to append from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty lists to store overhead record
    overheadrecords = []

    # append overhead record into the overhead list
    for row in reader:
        #get the day, items and amount for each record
        #and append the overhead list
        overheadrecords.append([row[1],row[3]])   



# create an empty list to store unique overheads from overheadrecords
overhead_list = [] 
for item in overheadrecords:
    # if day not in days_list, append day to days_list
    if item[0] not in overhead_list:
        overhead_list.append(item[0])

# create an empty list to store results of overhead_summary for each overhead
overhead_summary = []

def overhead_summary(overhead):
    '''
    - This function returns total amount based on type of overhead
    - Required parameters: Type of overhead 
    '''

    # calculate the total amount for the given overhead in each overhead record
    amount = 0
    for item in overhead:
        if item[0] == overhead:
            amount += float(item[1])

    # # calculate the overhead percentages
    # overhead_percent = 0
    # for item in overhead:
    #     if item 
