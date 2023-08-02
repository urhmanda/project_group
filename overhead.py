def overhead_function():
    from pathlib import Path
    import csv

    # create a file to csv file.
    fp = Path.cwd()/"csv_reports"/"overhead.csv"

    # read the csv file to append from the csv.
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header

        # create an empty lists to store overhead record
        overheadrecords = []

        # append overhead record into the overhead list
        for row in reader:
            """
            - To get the day, items and amount for each record
            - and append the overhead list
            """
            overheadrecords.append([row[1],row[3]])   



    # create an empty list to store unique overheads from overheadrecords
    overhead_list = [] 

    for item in overheadrecords:
        """
        - if overhead not in overhead_list, append overhead to overhead_list
        """
        if item[0] not in overhead_list:
            overhead_list.append(item[0])

    # create an empty list to store results of overhead_summary for each overhead
    overhead_summary = []

    def overhead_amount(overhead_category):
        """
        - This function returns total amount based on overhead category
        - Required parameters: Overhead category 
        """

        # calculate the total amount for the given overhead in each overhead record
        amount = 0
        for item in overheadrecords:
            if item[0] == overhead_category:
                amount += float(item[1])
        
        return (amount)
    
    total_all_overhead = 0
    highest_overhead = 0 
    highest_overhead_category = ""

    # For loop iterates through each overhead category in overhead_list
    for overhead_category in overhead_list:
        # Calculate total overhead for current category using the overhead_amount function
        total_overhead = overhead_amount(overhead_category)  
        # Calculate sum of all overhead expenses for all categories
        total_all_overhead += total_overhead 

        # If statement checks if total overhead of current category is higher than current highest overhead 
        # to find the highest overhead and its respective category
        if total_overhead > highest_overhead: 
            highest_overhead = total_overhead 
            highest_overhead_category = overhead_category 

    # find the percentage of highest overhead if the total of all overhead expenses is not equal to 0 
    if total_all_overhead != 0:
        highest_overhead_percentage = (highest_overhead / total_all_overhead) * 100
        print(f'[HIGHEST OVERHEAD] {highest_overhead_category.upper()}: {round(highest_overhead_percentage,2)}%')
        




