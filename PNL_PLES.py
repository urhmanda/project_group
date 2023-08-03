#define the function used to calculate the cash surplus/deficit
def profitandloss_function():
    """
    this function calculates the net profit deficit day on day, if not, the net profit surplus day on day

    there are no parameters
    """
    # import the relevant modules
    from pathlib import Path
    import csv

    #Read the excel file of overheads from the csv_reports file
    fp_read = Path.cwd() /"project_group"/"csv_reports"/"Profit and Loss.csv"
    #write the output into a new .txt file titled "team_members.txt"
    fp_write = Path.cwd() /"project_group"/"team_members.txt"
    fp_write.touch()

    #assigning the varialbe for net profit on previous days, making it 0
    previous_pnl = 0
    #assigning the variable for net profit on the current day, making it 0
    current_pnl = 0

    #assigning a variable for the possible outcomes, deficit or surplus
    output = 1

    #opens the excel file and starts the commands needed
    with fp_read.open(mode="r", encoding="UTF8", newline="") as file:
        #creates csv reader
        reader = csv.reader(file)
        #skips header
        next(reader)
        for row in reader:
            #ssigns the second columnn's value to the current net profit
            current_pnl= float(row[4])
            #for if when there is a day where the current net profit is less than the previous day
            if current_pnl < previous_pnl:
                #assigns the output to another value to show a different output type
                output = 2

                #writes the outcome to a text file
                with fp_write.open(mode="a", encoding="UTF8", newline="") as file:
                    #Current day subtract the previous day net profit
                    difference=previous_pnl-current_pnl
                    file.write(f"[PROFIT DEFICIT] Day:{row[0]}, AMOUNT: USD({difference}\n)")
                #assign the previous net profit to the new current net profit so that the process can continue
                previous_pnl = current_pnl

                #condition when output=1, meaning that the result is a surplus
                if output == 1:
                        #writes the result to a text file
                        with fp_write.open(mode="a", encoding="UTF8", newline="") as file:
                            file.write(f"[NET PROFIT SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")

                
#end the function
# profitandloss_function()


