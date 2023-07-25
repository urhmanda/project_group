from pathlib import Path
import csv

fp = Path.cwd()/"overhead.csv"

with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) 
