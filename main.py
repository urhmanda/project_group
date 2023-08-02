import cash_on_hand, overhead, profitloss_draft

def main():

    overhead_output = overhead.overhead_function()
    coh_output = cash_on_hand.coh_function()
    profitloss_output = profitloss_draft.profit_loss_function()
    
    return(overhead_output,coh_output,profitloss_output)

overhead_output,coh_output,profitloss_output = main()
# print(profitloss_output)
with open('summary_report.txt', 'w') as file:
    file.write(overhead_output + coh_output + profitloss_output)
    

