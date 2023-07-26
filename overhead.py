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


# --------------------------------------------------------


# create an empty list to store unique expense categories from overheadrecords
expense_category_list = [] 
for item in overheadrecords:
    # if expense category not in expense_category_list, append expense category to expense_category_list 
    if item[0] not in expense_category_list:
        expense_category_list.append(item[0])

def summary(expense_category):
    '''
    - This function returns the sum of overhead expenses based on expense_category
    - Required parameters: expense category
    '''
    total_expenses = 0 

    for item in overheadrecords:
        if item[0] == expense_category:
            total_expenses += int(item[1])
    
    return total_expenses

total_all_expenses = 0 
highest_expense = 0 
highst_expense_category = 0 

# for loop iterates through each expense category
for expense_category in expense_category_list:
    totalexpenses = summary(expense_category) # call summary function to get total expenses of a category
    total_all_expenses += totalexpenses # get sum of expenses of all expense categories

    if totalexpenses > highest_expense:
        highest_expense = totalexpenses 
        highst_expense_category = expense_category 

if total_all_expenses != 0:
    highest_expense_percentage = (highest_expense / total_all_expenses) * 100
    
print(f"[HIGHEST OVERHEAD] {highst_expense_category.upper()}: {round(highest_expense_percentage,2)}%")









