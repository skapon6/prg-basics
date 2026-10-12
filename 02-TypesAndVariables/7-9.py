from random import randint

random = randint(1,6)
print(f"Dice rolled: {random}")
special = random == 1 or random == 6
print(f"Special number (1 or 6): {special}")
