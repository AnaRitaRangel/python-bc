## 11.	Develop a program that receives a string from the user and converts it to capital letters.
print("CONVERTING TO CAPITAL LETTERS")
phrase =str(input("Type any phrase: "))
upper_phrase = phrase.upper()
print(upper_phrase)

## 12.	Develop a program that receives the user name and converts it to lower case letters.
print("CONVERTING TO LOWER LETTERS")
phrase =str(input("Type any phrase: "))
lower_phrase = phrase.lower()
print(lower_phrase)

## 13.	Develop a program that asks the user for a phrase, then prints it with no blank spaces. 
print("NO BLANK SPACES")
phrase =str(input("Type any phrase: "))
blank_free_phrase = phrase.replace(" ", "")
print(blank_free_phrase)

## 14.	Develop a program that asks the user to enter a date on the formata mm/dd/yyyy and then prints month, day and year separetely.
print("SPLIT INFO")
date =str(input("Enter a date on the format mm/dd/yyyy: "))
edit_date = date.split("/")
print(f"You chose the month: {edit_date[0]}")
print(f"You chose the day: {edit_date[1]}")
print(f"You chose the year: {edit_date[2]}")

## 15.	Develop a program that concatenates two strings given by the user.
print("POPULAR SAYING")
saying1 = str(input("Enter the first part of the popular saying: "))
saying2 = str(input("Enter the first part of the popular saying: "))
full_saying = saying1 + " " + saying2
print(full_saying)

