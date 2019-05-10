def cost_cal():
    print('Please enter the number of each item purchased. \n Rearz Safari Nighttume Briefs    $41.99 \n Safari Training Pants             $36.99 \n Safari Adult Baby Bottle         $24.99 \n Baby Wipes - 75                   $2.99')
    item1_q = float(input('Quantity for Rearz Safari Nighttume Briefs: '))
    item2_q = float(input('Quantity for Safari Training Pants: '))
    item3_q = float(input('Quantity for Safari Adult Baby Bottle: '))
    item4_q = float(input('Quantity for Baby Wipes - 75: '))
    
    total = item1_q * 41.99 + item2_q * 36.99 + item3_q * 24.99 + item4_q * 2.99 
    tax = round(total*0.13, 2)
    total_cost = total + tax
    print('Total ${} \nTax ${} \nYour Total Cost is {}'.format(total, tax, total_cost))

    