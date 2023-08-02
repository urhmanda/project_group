from pathlib import Path
import csv

#define the funciton being used for the calculation of cash surplus or deficit
def PNL_F():
    """"
    This calculates either the net profit surplus for each day or the net profit deficit for each day.
    """
    #Read the Profit and Loss excel from csv_reports
    fp_read = Path.cwd() /"csv_reports\Profit and Loss.csv"
    #Put the output into a new .txt file
    fp_write = Path.cwd() /"summary"
    fp_write.touch()

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
                    file.write(f"[NET PROFIT DEFICIT] DAY:{row[0]}, AMOUNT: USD{difference}\n")
            #assign the previous net profit to the current net profit so the loop can restart
            prev_pl = curr_pl

    #create a condition where ouput = 1, which is when the deficit condition is not fufilled, meaning that the result is a surplus
    if output == 1:
        #write the result to a text file
        with fp_write.open(mode="a", encoding="UTF8", newline="") as file:
            file.write(f"[NET PROFIT SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")

#end the function
PNL_F()





