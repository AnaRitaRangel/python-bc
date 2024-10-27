## Verify the number typed by the user. Change negatives to zero, print if it is zero or single, or greater
number = int(input("Type a number: "))
if number < 0:
        number = 0
        print("Negative number changed to zero")
elif number == 0:
        print("Number is Zero")
elif number == 1:
        print("Number is single")
else:
        print("Number is greater than one")
