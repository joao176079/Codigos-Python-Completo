
#Como exibir o índice de cada item da lista 

lista = [" Maria " , "Kaique " , "Joao"]
lista.append("Carlos")
indice = range (len (lista))

for indices in indice :
    print (indices , lista[indices] , type (lista[indices]))
