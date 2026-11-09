pin = '0805'

for i in range(3):
    entered = input('Enter the PIN code: ')
    if entered == pin:
        print('Correct PIN')
        break
    else:
        print('Incorrect...')
        if i == 2:
            print('Sorry, your payment card has been blocked.')
