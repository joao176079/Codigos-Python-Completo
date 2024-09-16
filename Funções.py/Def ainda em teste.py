import os 
os.system("cls || clear")



def big_mac():
    print ("Sanduiche Big mac.")


print ("Inicio")
big_mac()
print("Fim")

def fazer_big_mac(nome):
    print (f"{nome} pediu um sanduiche Big Mac.")

fazer_big_mac("João")
fazer_big_mac("Guilherme")
fazer_big_mac("Victor")

def fazer_batata(tamanho):
    print (f"O tamanho da batata é : {tamanho}")

def preparar_refrigerante(tipo , tamanho ):
    print (f"O seu tipo é : {tipo} . O seu tamanho é : {tamanho}")

fazer_big_mac("para João")
fazer_batata("Grande")
preparar_refrigerante("Coca" , "Média")

def fazer_combo_big_mac(nome ,tamanho_batata , tipo_refri , tamanho_refri):
   fazer_big_mac(nome)
   fazer_batata(tamanho_batata)
   preparar_refrigerante (tipo_refri , tamanho_refri)

fazer_combo_big_mac("João " , "Grande" , "Coca Cola" , "2L")