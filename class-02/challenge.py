## Try to anticipate bugs. Develop a program that asks for the user name, mensal salary and the bónus value. The program should return a message calling the user by name and informing the salary ammount compared to the bonuses ##
# 1) Ask for the user name
while True:
    name = input("Type your name: ")
 # Check if the name is a digit
    if name.isdigit():
        print("NOTE: The user name can not be a number. Please try again")
        continue
# Check if the name is blank
    if len(name.strip()) == 0: # .strip() removes any whitespace
        print("NOTE: The user name can not be blank. Please try again")
        continue
    break

# 2) Ask for the user monthly salary
# Convert the data to a float
salary = float(input("Type your monthly salary: "))

# 3) Ask for the user bonus value
# Convert the data to a float
bonus_user = float(input("Type your bonus KPI: "))

# 4) Calculate the final bonus value
bonus_set = 1000
bonus_final = bonus_set + salary * bonus_user

# 5) Print the KPI calculus to the user 
print(f"Using the formula: {bonus_set} + {salary} * {bonus_user}")

# 6) Print a personalized message including the user name, salary and bonus 
print(f"The user {name} has a bonus of {bonus_final}")

