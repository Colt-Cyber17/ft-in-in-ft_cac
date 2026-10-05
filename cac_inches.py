print('choose your inches to feet calculator, or feet to inches')
print('Press [enter] for inches to feet')
print('Press [B] for feet to inches')

choice = input('Your choice: ').lower()
print()
if choice == 'b':
    print('Welcome to feet to inches calculator')
    cac_ft_in = int(input('Enter your number for feet: '))
    cac_in = cac_ft_in * 12
    print(f'inches = {cac_in} ')
    
elif choice == '':
    print('Welcome to inches to feet calculator')
    cac_in_ft = int(input('Enter your number for inches: '))
    cac_ft = cac_in_ft / 12
    print(f'Feet = {cac_ft:.2f}')
    
                    
    