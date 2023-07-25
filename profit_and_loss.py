from pathlib import Path
import csv

fp = Path.cwd()/"profit and loss.csv"

with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) #To skip the header

#Creates an empty list to store profit and loss records
profit_and_loss=[]

