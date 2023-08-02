def profit_loss_function():
    from pathlib import Path
    import csv

<<<<<<< HEAD
    def find_cash_deficit(data):
        cash_deficit_list = []
        for i in range(1, len(data)):
            day, cash = data[i]
            prev_day, prev_cash = data[i - 1]
            if cash > prev_cash:
                """
                - To calculate difference in amount of cash if current day's cash is less than previous day's
                """
                cash_deficit = cash - prev_cash
                cash_deficit_list.append((day, cash_deficit))
        return cash_deficit_list
=======
    #define the funciton being used for the calculation of cash surplus or deficit
    def PNL_F():
        """"
        This calculates either the net profit surplus for each day or the net profit deficit for each day.
        """
        #Read the Profit and Loss excel from csv_reports
        fp_read = Path.cwd() /"csv_reports\profit_loss.csv"
        #Put the output into a new .txt file
        fp_write = Path.cwd() /"summary_report.txt"
        fp_write.touch()
>>>>>>> 8caf6d04c7ee7b64742a2eba0a8b3bf4098a294b

        #assign the variable for the net profit on the previous day, equate it to 0
        prev_pl = 0
        #assign the variable for the net profit on the current day, equate it to 0
        curr_pl = 0

        #assign a variable for the output type for the possible outcomes (deficit/surplus)
        output = 1

        #open the excel file and begin the commands needed on the excel file
        with fp_read.open(mode="r", encoding="UTF8", newline="") as file:
            # create csv reader object using csv
            reader = csv.reader(file)
            # to skip reading header
            next(reader)
            # iterate each row with loop
            for row in reader:
<<<<<<< HEAD
                """
                - To add data for number of days and amount of cash into "data", which is an empty list
                """
                day = int(row[0])
                cash = int(row[1])
                data.append((day, cash))
        return data
=======
                #assign the value in the second columnn with index to the current net profit
                curr_pl = float(row[4])
                #create an event where if the current net profit is less than the previous net profit
                if curr_pl < prev_pl:
                    #assign the output to a different value to indicate a different output type
                    output = 2

                    # write the result to a text file
                    with fp_write.open(mode="a", encoding="UTF8", newline="") as file:
                        #the difference between net profit on the previous day and the current day
                        difference = prev_pl - curr_pl
                        file.write(f"[PROFIT DEFICIT] DAY:{row[0]}, AMOUNT: USD{difference}\n")
                #assign the previous net profit to the current net profit so the loop can restart
                prev_pl = curr_pl

        #create a condition where ouput = 1, which is when the deficit condition is not fufilled, meaning that the result is a surplus
        if output == 1:
            #write the result to a text file
            with fp_write.open(mode="a", encoding="UTF8", newline="") as file:
                file.write(f"[PROFIT SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")

    #end the function
    PNL_F()

>>>>>>> 8caf6d04c7ee7b64742a2eba0a8b3bf4098a294b



