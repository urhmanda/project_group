def inside_PNL():
    import csv

    # Function to check for cash deficit
    def check_cash_deficit(data):
        cash_deficit_days = []
        prev_profit = None

        for row in data:
            day, _, _, _, net_profit = row
            net_profit = int(net_profit)

            if prev_profit is not None and net_profit < prev_profit:
                deficit_amount = prev_profit - net_profit
                cash_deficit_days.append((day, deficit_amount))

            prev_profit = net_profit

        return cash_deficit_days

    # Read data from CSV file
    data = []
    with open("PNL.csv", "r") as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)  # Skip header row
        for row in csv_reader:
            data.append(row)

    # Check for cash deficit days
    cash_deficit_days = check_cash_deficit(data)

    # Print the messages for cash deficit days
    for day, deficit_amount in cash_deficit_days:
        print(f"[PROFIT DEFICIT] Day: {day}, Amount: USD{deficit_amount}")