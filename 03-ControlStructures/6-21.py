amount = int(input('Enter the amount in PLN: '))
n = amount

coins_5 = n // 5
n = n % 5

coins_2 = n // 2
n = n % 2

coins_1 = n

print(f'The amount of PLN {amount} in coins:')
print(f'5 PLN coins: {coins_5}')
print(f'2 PLN coins: {coins_2}')
print(f'1 PLN coins: {coins_1}')
