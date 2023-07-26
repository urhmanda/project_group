import csv
import urllib.request

def compute_difference_and_max_increment(csv_url):
    response = urllib.request.urlopen(csv_url)
    lines = response.read().decode('utf-8').splitlines()

    # Assuming the first line contains the column headers
    csv_reader = csv.reader(lines[1:])

    # Skip the first row (header row) to get the data rows
    next(csv_reader, None)

    # Convert numeric values from strings to integers and handle missing values
    data = []
    net_profit_values = []
    for row in csv_reader:
        row_data = []
        for cell in row:
            try:
                value = int(cell.replace(',', '').replace('(', '').replace(')', ''))
            except ValueError:
                value = None
            row_data.append(value)
        data.append(row_data)
        if row_data[-1] is not None:
            net_profit_values.append(row_data[-1])

    # Consider data for the first 90 days if available
    if len(net_profit_values) >= 90:
        net_profit_values = net_profit_values[:90]

        # Compute the difference in the net profit column
        difference_in_net_profit = []
        for i in range(1, len(net_profit_values)):
            difference = net_profit_values[i] - net_profit_values[i-1]
            difference_in_net_profit.append(difference)

        # Find the day and amount of the highest increment
        max_increment_amount = max(difference_in_net_profit)
        max_increment_day = difference_in_net_profit.index(max_increment_amount) + 1

        return data, difference_in_net_profit, max_increment_day, max_increment_amount

    else:
        return None, None, None, None

csv_url = 'https://raw.githubusercontent.com/urhmanda/project_group/main/csv_reports/profit_and_loss/profit_and_loss.csv'

try:
    # Call the function with the provided CSV URL
    data, result, max_increment_day, max_increment_amount = compute_difference_and_max_increment(csv_url)

    if data is not None and max_increment_amount is not None:
        print("Difference in Net Profit Column:", result)
        print("Day of Highest Increment:", max_increment_day)
        print("Amount of Highest Increment:", max_increment_amount)
    else:
        print("No data or invalid data in the 'Net Profit' column.")

except Exception as e:
    print("Error:", e)