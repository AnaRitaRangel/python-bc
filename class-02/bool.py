# 16.	Develop a program that evaluates two expressions inserted by the user and return the AND result between them.
print("PYTHON BOOLEANS")
print("AND results will be true for just T & T")
value1 = input("Enter the first expression (e.g., 5 > 3): ")
value2 = input("Enter the second expression (e.g., 10 == 10): ")
and_result = eval(value1) and eval(value2)
print("Logic AND result: ", and_result)

# 17.	Develop a program that receives two bool values and returns the OR result
print("PYTHON BOOLEANS")
print("OR results will be FALSE for just F & F")
value1 = input("Enter the first expression (e.g., 100 >= 50): ")
value2 = input("Enter the second expression (e.g., 7 != 10): ")
or_result = eval(value1) or eval(value2)
print("Logic OR result: ", or_result)

# 18.	Develop a program that inverts the bool value inserted by the user
print("Inverting the results")
expression = input("Enter an expression (e.g., 9 == 9:) ")
result = eval(expression)
invert = not result
print("Logic invert result: ", invert)

# 19.	Develop a program that compares if two numbers given by the user are equal
print("Are these numbers the same?")
value1 = input("Enter the first number: ")
value2 = input("Enter the second number: ")
compare = value1 == value2
print("These numbers are the same: ", compare)

# 20.	Develop a program that verifies if two numbers given by the user are different
print("Are these numbers different?")
value1 = input("Enter the first number: ")
value2 = input("Enter the second number: ")
compare = value1 != value2
print("These numbers are different: ", compare)