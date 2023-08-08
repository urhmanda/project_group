#Imports the functions of cash_on_hand.py, overhead.py and profit_and_loss.py
import cash_on_hand, overhead, profit_and_loss

#Function for putting all 3 functions from the different .py into 1 function
def main():

    #Makes the 3 different functions into 3 variables
    overhead_output = overhead.overhead_function()
    coh_output = cash_on_hand.coh_function()
    profitloss_output = profit_and_loss.profit_loss_function()
    
    return(overhead_output,coh_output,profitloss_output)

#Makes the 3 different functions into 1
overhead_output,coh_output,profitloss_output = main()
# print(profitloss_output)
with open('summary_report.txt', 'w') as file:
    file.write(overhead_output + coh_output + profitloss_output)
    

