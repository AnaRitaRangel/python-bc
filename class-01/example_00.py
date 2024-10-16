## Ask for user name and say hello to him/her ##
name = input ("Digite seu nome: ")
print("Hi, " + name + "!")

## Inform the user how many letters are there in his/her name ##
## Predictable bug: composed names, that have spaces. I need to remove them, otherwise the space will be counted as a letter ##
no_space_name = name.replace(" ", "")
print("Your name has " + str(len(no_space_name)) + " letters")

## Develop a program that adds two numbers chosen by the user ##
number1 = input("Enter a number: ")
number2 = input("Enter another number: ")
sum = int(number1) + int(number2)
print("The sum between " + str(number1) + " and " + str(number2) + " is: " + str(sum))