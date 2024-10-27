temperature = float(input("Enter the temperature value in Celsius: "))
if temperature < 18:
    temperature = "The Temperature is Low"
elif temperature > 26:
    temperature = "The Temperature is High"
else:
    temperature = "The Temperature is Normal"
print(temperature)