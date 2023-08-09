#Creates a function to find cash deficits
def coh_function():
    import csv

    def find_cash_deficit_and_surplus(data):
        """
        - This function finds cash deficits and the highest net cash surplus in data
        """
        cash_deficit_list = []
        highest_increment_day = None
        highest_increment_amount = 0

        for i in range(1, len(data)):
            day, cash = data[i]
            prev_day, prev_cash = data[i - 1]

            # Calculate net cash increment for current day
            increment = cash - prev_cash

            if increment < 0:
                """
                - To calculate difference in net cash if current day's cash is lesser than previous day's
                """
                cash_deficit = prev_cash - cash
                cash_deficit_list.append((day, cash_deficit))
           
            elif increment > 0:
                """
                - Checks if increment is higher than previous highest 
                """
                if increment > highest_increment_amount:
                    highest_increment_day = day
                    highest_increment_amount = increment
    
        return cash_deficit_list, highest_increment_day, highest_increment_amount

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
                - To add data for number of days and amount of cash into "data", which is an empty list
                """
                day = int(row[0])
                cash = int(row[1])
                data.append((day, cash))
        return data

    # Provide the relative file path directly
    csv_file_path = "csv_reports/cash_on_hand.csv"
    data = read_csv_data(csv_file_path)

    cash_deficits, highest_increment_day, highest_increment_amount = find_cash_deficit_and_surplus(data)

    result_str = "" # result_str will store formatted information about cash deficits or highest net cash surplus as a string

    if cash_deficits:
        """
        - Checks if there are any cash deficits
        """
        for day, deficit in cash_deficits:
            """
            - Iterate through each day and deficits in cash_deficits
            """
            result_str += f"[CASH DEFICIT] DAY: {day}, AMOUNT: USD{deficit}\n"
            """
            - Create a string indicating a cash deficit and append to result_str
            """
    else:
        """
        - If there are no cash deficits, indicate a cash surplus
        """
        result_str += f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN PREVIOUS DAY\n"
        """
        - Check if there is information about the highest increment in cash surplus
        """
        if highest_increment_day is not None:
            """
            - Append information on highest cash surplus increment to result_str
            """
            result_str += f"[HIGHEST NET CASH SURPLUS] DAY: {highest_increment_day}, AMOUNT: USD{highest_increment_amount}\n"
    
    return result_str