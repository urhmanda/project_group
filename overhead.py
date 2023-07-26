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
    # if overhead not in overhead_list, append overhead to overhead_list
    if item[0] not in overhead_list:
        overhead_list.append(item[0])


# # create an empty list to store results of overhead_summary for each overhead
# summary_list = []

# calculate the total amount for the given overhead in each overhead record
expenses = 0  
for item in overheadrecords:
    if item[1] not in expenses:
        expenses.append(item[1])
print(expenses)
    


    # # calculate the overhead percentages
    # overhead_percent = 0
    # for item in overheadrecords:
    #     if item[0] not in overhead_percent:
    #         overhead_percent += float(item[1] / amount) * 100

# # Iterate through each type of overhead 
# for overhead in overhead_list:
#     summary = overhead_summary(overhead) # call emp_summary function to get summary 
#     summary_list.append(summary) # append summary into summary_list

# for summary in summary_list:
#     print (f'{summary}')









