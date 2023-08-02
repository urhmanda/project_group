def coh_function():
    import csv

    def find_cash_deficit(data):
        '''
        - This function finds cash deficits in data
        '''
        cash_deficit_list = []
        for i in range(1, len(data)):
            day, cash = data[i]
            prev_day, prev_cash = data[i - 1]
            if cash < prev_cash:
                cash_deficit = prev_cash - cash
                cash_deficit_list.append((day, cash_deficit))
        return cash_deficit_list

    def read_csv_data(file_path):
        '''
        - This function reads data from csv file and return a list of tuples
        '''
        data = []
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header if it exists
            for row in reader:
                day = int(row[0])
                cash = int(row[1])
                data.append((day, cash))
        return data

    # Provide the relative file path directly
    csv_file_path = "csv_reports/cash_on_hand.csv"
    data = read_csv_data(csv_file_path)

    cash_deficits = find_cash_deficit(data)

    result_str = "" # result_str will store formatted cash deficits information as a string
    for day, deficit in cash_deficits:
        result_str += f"[CASH DEFICIT] DAY: {day}, AMOUNT: USD{deficit}\n"
    return result_str
