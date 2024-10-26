## Float
# 6. Develop a program that adds two float numbers. 
print("SUM of DECIMAL NUMBERS")
number1 = float(input("Type a decimal number: "))
number2 = float(input("Type another decimal number: "))
sum =  number1 + number2
print(f"The sum between {number1} and {number2} is {sum}")

# 7. Develop a program that calculates the average between two float numbers. 
print("AVERAGE BETWEEN DECIMAL NUMBERS")
number1 = float(input("Type a decimal number: "))
number2 = float(input("Type another decimal number: "))
average =  (number1 + number2) / 2
print(f"The average between {number1} and {number2} is {average}")

# 8.	Develop a program that calculates the base raised to the power of an exponent given by the user.  
print("POWER WITH DECIMAL NUMBERS")
base = float(input("Type a decimal number: "))
exponent = float(input("Type another decimal number: "))
power =  base ** exponent
print(f"The {base} raised to the power of {exponent} is {power}")

# 9.	Develop a program that converts the temperature in Celsius to Fahrenheit.
print("CONVERT CELSIUS TO FAHRENHEIT")
celsius = float(input("Type the temperature in degrees Celsius: "))
fahrenheit = celsius * 9/5 + 32
print(f"The equivalent of {celsius}° C is  {fahrenheit}° F")

# 10.	Develop a program that calculates the area of a circle based on the radius.
print("AREA OF THE CIRCLE")
import math
radius = float(input("Type the radius: "))
area = radius * math.pi ** 2
print(f"The area of a circle with {radius} radius is  {area:.2f}")