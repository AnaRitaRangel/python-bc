##Teacher’s solution:
# 1) Ask for the user name
name = input("Type your name: ")
if
    name.isnumeric()
    print("You need to type your name, numbers are not allowed")

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
