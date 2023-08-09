#Creates a function that will be made for finding the days where there are profit loss
def profit_loss_function():
    import csv

    def find_profit_deficit_and_surplus(data):
        """
        - This function finds profit deficits and the highest net profit surplus in data
        "'"
        profit_deficit_list = []
        highest_increment_day = None
        highest_increment_amount = 0

        for i in range(1, len(data)):
            day, profit = data[i]
            prev_day, prev_profit = data[i - 1]

            # Calculate net profit increment for current day
            increment = profit - prev_profit

            if increment < 0:
                # To calculate difference in net profit if current day's profit is lesser than previous day's
                profit_deficit = prev_profit - profit
                profit_deficit_list.append((day, profit_deficit))
           
            elif increment > 0:
                # Checks if increment is higher than previous highest 
                if increment > highest_increment_amount:
                    highest_increment_day = day
                    highest_increment_amount = increment
    
        return profit_deficit_list, highest_increment_day, highest_increment_amount

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
                profit = int(row[4])
                data.append((day, profit))
        return data

    # Provide the relative file path directly
    csv_file_path = "csv_reports/profit_loss.csv"
    data = read_csv_data(csv_file_path)

    profit_deficits, highest_increment_day, highest_increment_amount = find_profit_deficit_and_surplus(data)

    result_str = "" # result_str will store formatted information about profit deficits or highest net profit surplus as a string

    if profit_deficits:
        for day, deficit in profit_deficits:
            result_str += f"[PROFIT DEFICIT] DAY: {day}, AMOUNT: USD{deficit}\n"
    else:
        result_str += f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY\n"
        if highest_increment_day is not None:
            result_str += f"[HIGHEST NET PROFIT SURPLUS] DAY: {highest_increment_day}, AMOUNT: USD{highest_increment_amount}\n"
    
    return result_str

        