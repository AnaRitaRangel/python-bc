#Você está analisando um conjunto de dados de vendas e precisa garantir que todos os registros tenham valores positivos para quantidade e preço. Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos forem positivos ou "Dados inválidos" caso contrário.

quantity = int(input("Type quantity: "))

while quantity <= 0:
    print ('Invalid data input')
    quantity = int(input("Type quantity: "))

price = float(input("Type the unity price: "))

while price <= 0:
    print ('Invalid data input')
    price = float(input("Type the unity price: "))

print ('Valid data')

