import decimal

num1 = decimal.Decimal (0.1)
num2 = decimal.Decimal(0.8)
num3 = num1 * num2 
print (round(num3 , 2))
print (f'{num3:.2f}')

#Ultiliza o decimal caso a conta seja muito alta ! + ''5 casas decimais''.