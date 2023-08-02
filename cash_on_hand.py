def inside_COH():
    import csv

    def find_cash_deficit(data):
        cash_deficit_list = []
        for i in range(1, len(data)):
            day, cash = data[i]
            prev_day, prev_cash = data[i - 1]
            if cash < prev_cash:
                """
                - To calculate difference in amount of cash on hand if current day's cash is lesser than previous day's
                """
                cash_deficit = prev_cash - cash
                cash_deficit_list.append((day, cash_deficit))
        return cash_deficit_list

    def read_csv_data(file_path):
        data = []
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header if it exists
            for row in reader:
                """
                - To add data for number of days and amount of cash into "data", which is an empty list
                """
                day = int(row[0])
                cash = int(row[1])
                data.append((day, cash))
        return data

    # Provide the relative file path directly
    csv_file_path = "csv_reports/COH.csv"
    data = read_csv_data(csv_file_path)

    cash_deficits = find_cash_deficit(data)

    for day, deficit in cash_deficits:
        print(f"[CASH DEFICIT] DAY: {day}, AMOUNT: USD{deficit}")
