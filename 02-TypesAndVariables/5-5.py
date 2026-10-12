price = float(input("Enter price: "))
discount = float(input("Enter discount %: ")) / 100
price_with_discount = round(price * (1-discount),2)
print(f"Price with discount: {price_with_discount}")
print(f"Reduction: {round(price*discount,2)}")