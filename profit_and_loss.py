def profit_loss_function():
    from pathlib import Path
    import csv

    def find_profit_deficit(data):
        profit_deficit_list = []
        for i in range(1, len(data)):
            day, profit = data[i]
            prev_day, prev_profit = data[i - 1]
            if profit < prev_profit:
                """
                - To calculate difference in amount of profit if current day's profit is lesser than previous day's
                """
                profit_deficit = profit - prev_profit
                profit_deficit_list.append((day, profit_deficit))
        return profit_deficit_list

    def read_csv_data(file_path):
            """
            - This function reads data from csv file and return a list of tuples
            """
            data = []
            with open(file_path, newline='') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Skip the header if it exists
                for row in reader:
                    """
                    - To add data for number of days and amount of profit into "data", which is an empty list
                    """
                    day = int(row[0])
                    profit = int(row[1])
                    data.append((day, profit))
            return data

        # Provide the relative file path directly
    csv_file_path = "csv_reports/profit_loss.csv"
    data = read_csv_data(csv_file_path)

    profit_deficits = find_profit_deficit(data)

    result_str = "" # result_str will store formatted profit deficits information as a string
    for day, deficit in profit_deficits:
            result_str += f"[PROFIT DEFICIT] DAY: {day}, AMOUNT: USD{deficit}\n"
    return result_str

        