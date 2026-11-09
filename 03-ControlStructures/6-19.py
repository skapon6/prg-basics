print('SURVEY')
q1 = input('Are you interested in computer science? (y/n): ') == 'y'
q2 = input('Do you like playing computer games? (y/n): ') == 'y'
q3 = input('Do you have an Instagram account? (y/n): ') == 'y'

print('SURVEY RESULTS')
if q1:
    print('Interested in computer science: Yes')
else:
    print('Interested in computer science: No')

if q2:
    print('Playing computer games: Yes')
else:
    print('Playing computer games: No')

if q3:
    print('Has an Instagram account: Yes')
else:
    print('Has an Instagram account: No')
