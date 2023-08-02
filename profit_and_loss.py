
import csv

def read_csv(file_path):
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        data = [list(map(int, row)) for row in csv_reader]
    return header, data

def check_profit_deficit(data):
    deficit_days = []
    previous_net_profit = None

    for day, _, _, _, net_profit in data:
        if previous_net_profit is not None and net_profit < previous_net_profit:
            deficit_days.append((day, previous_net_profit - net_profit))
        previous_net_profit = net_profit

    return deficit_days

def main():
    file_path = "csv_reports/Profit and Loss.csv"
    header, data = read_csv(file_path)

    deficit_days = check_profit_deficit(data)

    if deficit_days:
        for day, deficit in deficit_days:
            print(f"[PROFIT DEFICIT] Day: {day}, Amount: USD {deficit}")
    else:
        print("No days with lower net profit than the previous day.")

if __name__ == "__main__":
    main()
