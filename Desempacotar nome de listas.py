import os 
os.system("cls || clear")

# Abaixo , comando simples de desempacotamento de pacotes ! + Tuplas . E empacotamento !

#nome1 , nome2 ,nome3 = ["Joao" , "Victor" , "Joe"]
#print (nome2)


#--------------------------------------------------------------------------------------- 

nome1, *empacotamento = ["Joao" , "Victor" , "Joe"]
print (empacotamento)

#Acima terá o empacotamento , no caso os que não foram atribuidos fica empacotados. 

#======================================================================================

#Demosntração de Tuplas abaixo ! 

#nomes = "Maria" , "Joao" , "Linaldo"
#nomes = list (nomes)
#nomes = tuple(nomes)
#print (nomes [0])
#print (nomes)


#==================================================================================

nomes = ["Maria" , "Joao" , "Linaldo"]
nomes.append("Sherlock")

for item in enumerate (nomes):
    print (item)
