def inside_cash():
    from pathlib import Path
    import csv

    # Create a file path to the CSV file.
    fp = Path.cwd() / 'csv_reports' / 'cash_on_hand.csv'

    # Read the CSV file to append from the CSV.
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # To skip the header

        # Create a dictionary to store cash on hand records for each day
        cash_on_hand = {}

        # Append cash on hand records into the cash_on_hand dictionary
        for row in reader:
            day = row[0]
            amount = row[3]

            # Check if the amount is numeric or not
            if not amount.replace('.', '', 1).isdigit():
                # If the amount is non-numeric, ignore it and continue to the next record
                continue

            amount = float(amount)

            if day not in cash_on_hand:
                cash_on_hand[day] = amount
            else:
                cash_on_hand[day] += amount

    # Generate a list of all possible days within the range (0 to 90)
    all_days = [str(day) for day in range(0, 91)]

    # Sort the list based on the day
    sorted_cash_on_hand = sorted(cash_on_hand.items(), key=lambda item: item[0])

    # Calculate the differences in Cash-on-Hand between each day
    differences = []
    current_cash = 0.0

    for day in all_days:
        if day in cash_on_hand:
            current_cash = cash_on_hand[day]
        differences.append(current_cash)

    # Calculate the differences in Cash-on-Hand between each day
    differences = [differences[i] - differences[i - 1] for i in range(1, len(differences))]

    # Track the highest increment and its corresponding day and amount
    highest_increment = max(differences)
    highest_increment_index = differences.index(highest_increment)
    highest_increment_day = all_days[highest_increment_index + 1]
    highest_increment_amount = cash_on_hand[highest_increment_day]

    number_of_days = len(all_days)
    print("Number of days recorded:", number_of_days)

    for i, difference in enumerate(differences, start=1):
        print(f"Day {i}: Difference in Amount: {difference}")

    print(f"\nHighest Increment:")
    print(f"Day: {highest_increment_day}")
    print(f"Amount: {highest_increment_amount}")