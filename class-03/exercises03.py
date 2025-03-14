## Exercise 1: Verifying data quality
# You are analising a set of sales data and needs to assure that all the registers have a positive number for quantity and price. Develop a program that verifies these fields and print “Valid Data” if all data is valid, otherwise, print “Invalid Data”

quantity = int(input("Type quantity: "))

while quantity <= 0:
    print: ('Invalid data input')
    quantity = int(input("Type quantity: "))

price = float(input("Type the unity price: "))

while price <= 0:
    print: ('Invalid data input')
    price = float(input("Type the unity price: "))

print ('Valid data')

# Better solution: This way the code won't break if the user accidentally hits a key that is not a number
while True:
    try:
        quantity = int(input("Type quantity: "))
        if quantity <= 0:
            print('Invalid data input')
        else:
            break  # Exit the loop if the quantity is valid
    except ValueError:
        print("Invalid input. Please enter a valid integer for quantity.")

while True:
    try:
        price = float(input("Type the unity price: "))
        if price <= 0:
            print('Invalid data input')
        else:
            break  # Exit the loop if the price is valid
    except ValueError:
        print("Invalid input. Please enter a valid number for price.")

print('Valid data')



## Exercise 2: Classifying Sensor Data
# Imagine that you are working with IoT sensor data.
# The internet of things, or IoT, is a network of interrelated devices that connect and exchange data with other IoT devices and the cloud.
# The data include temperature measurements. You need to classify each reading as ‘Low’, ‘Normal’ or ‘High’. Considering that:  
# •	Temperature < 18°C is ‘Low’
# •	Temperature >= 18°C e <= 26°C is ‘Normal’
# •	Temperature > 26°C is ‘High’
temperature = float(input("Enter the temperature value in Celsius: "))
if temperature < 18:
    temperature = "The Temperature is Low"
elif temperature > 26:
    temperature = "The Temperature is High"
else:
    temperature = "The Temperature is Normal"
print(temperature)

