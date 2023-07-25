from pathlib import Path
import csv
fp = Path.cwd() / 'PFB_grp_proj' / 'cash on hand.csv'
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) 

cash_on_hand = 