import os 
os.system("cls || clear")

lsita = [ 10 , 20 ,30 , 40]
del lsita [2]

lsita.append(50)
lsita.pop()
lsita.append(70)
lsita.append(60)
lsita.insert(0, "Joao que fez")
ultimo_valor = lsita.pop()
print (lsita ,'Removido ' , ultimo_valor)