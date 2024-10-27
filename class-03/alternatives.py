## Exercise 1: Verifying data quality
# You are analising a set of sales data and needs to assure that all the registers have a positive number for quantity and price. Develop a program that verifies these fields and print "Valid input for Quantity and Price" if all the conditions match
while True:
    quantity = int(input("Type quantity: "))
    if quantity < 1:
        print("The quantity must be one or above. Please try again")
        continue
    break
while True:
    price = float(input("Type the unity price: "))
    if price < 0:
        print("The price can not be negative. Please try again")
        continue
    elif price == 0:
        print("The price can not be zero. Please try again")
        continue
    else:
        print("Valid input for Quantity and Price")
    break
