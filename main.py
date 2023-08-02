import cash_on_hand, overhead, profit_and_loss

def main():
    
    overhead_output = overhead.overhead_function()
    coh_output = cash_on_hand.coh_function()
    profitloss_output = profit_and_loss.profit_loss_function()
    
    return(overhead_output,coh_output,profitloss_output)

overhead_output,coh_output,profitloss_output = main()

with open('summary_report.txt', 'w') as file:
    file.write(overhead_output + coh_output + profitloss_output)
    

