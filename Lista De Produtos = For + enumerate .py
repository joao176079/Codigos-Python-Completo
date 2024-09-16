import os
os.system('cls|| clear')

lista_de_compras = int (input ("Digite a quantidade de produtos que você deseja : "))

produtos = []

for i in range (lista_de_compras):
    produto = input (f"Digite o seu produto {i+1}: ")
    produtos.append(produto)

for index , produto in enumerate (produtos):
    print (f"Produto {index + 1}ª : {produto}")
