# def profit_loss_function():
#     import csv

#     def find_profit_deficit(data):
#         '''
#         - This function finds profit deficits in data
#         '''
#         profit_deficit_list = []
#         for i in range(1, len(data)):
#             day, profit = data[i]
#             prev_day, prev_profit = data[i - 1]
#             if profit > prev_profit:
#                 profit_deficit = profit - prev_profit
#                 profit_deficit_list.append((day, profit_deficit))
#         return profit_deficit_list

#     def read_csv_data(file_path):
#         '''
#         - This function reads data from csv file and return a list of tuples
#         '''
#         data = []
#         # Provide the relative file path directly
#         with open(file_path, newline='') as csvfile:
#             reader = csv.reader(csvfile)
#             next(reader)  # Skip the header if it exists
#             for row in reader:
#                 day = int(row[0])
#                 profit = int(row[1])
#                 data.append((day, profit))
#         return data

#     # Provide the relative file path directly for 'PNL.csv'
#     csv_file_path = "csv_reports/profit_loss.csv"
#     data = read_csv_data(csv_file_path)

#     profit_deficits = find_profit_deficit(data)

#     result_str = "" # result_str will store formatted output as a string
#     for day, deficit in profit_deficits:
#         result_str += f"[PROFIT DEFICIT] Day: {day}, Amount: USD{deficit}\n"
#     return result_str