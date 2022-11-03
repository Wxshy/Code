bad_varaibles = ['v', 'var', 'c1', 'atp', '123', 'var 1']
good_varaibles = ['account_name', 'password']

#------------------------------------------------------------

fav1 = input('Please enter your first favourite food: ')
fav2 = input('Please enter your second favourite food: ')

print('Here is the new food', fav1+fav2)

#-------------------------------------------------------------

total = float(input('Please enter the amount on the bill: $'))

print('15% Tip: $', str(round(total * 1.15)))
print('20% Tip: $', str(round(total * 1.20)))

#---------------------------------------------------------------

price = float(input('Please enter the base price of the car: $'))

dealer_prep = 100
destination_charge = 250
price += dealer_prep + destination_charge

print('Here is the final charge including all fees: $'+ str(price))