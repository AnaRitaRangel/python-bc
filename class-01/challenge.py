## Develop a program that asks for the user name, mensal salary and the bónus value. The program should return a message calling the user by name and informing the salary ammount compared to the bonuses ##
name = str(input("Type your name: "))
salary = int(input("Type your monthly salary: "))
kpi = int(1.5)
bonus = str(1000 + salary * kpi)
print(name + ", o valor do seu bônus é de " + (bonus))
