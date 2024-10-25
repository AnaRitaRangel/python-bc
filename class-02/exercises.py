## Ask for the user name ##
name = input("Type your name: ")

## print the user name in upper case ##
capital_name = name.upper()
print(capital_name)

## print the type of variable that information is ##
print(type(name))

## print user name lower case ##
print(name.lower())

## print name with just the first letter capital ##
print(name.capitalize())

## return the first part of an e-mail and the last one ##
e_mail = input("Write down your e-mail: ")
print(e_mail.split("@"))


