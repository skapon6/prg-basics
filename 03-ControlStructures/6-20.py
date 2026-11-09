decimal = int(input('Enter decimal number: '))
n = decimal
binary = ''

if n == 0:
    binary = '0'

while n > 0:
    remainder = n % 2
    binary = str(remainder) + binary
    n = n // 2

print(f'{decimal}(10) = {binary}(2)')
