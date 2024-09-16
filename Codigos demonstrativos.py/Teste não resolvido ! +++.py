import os 
os.system("cls || clear ")

login  = 'joao'
senha = 123
QUANTIDADE_DE_TENTATIVAS = 3

for i in range (QUANTIDADE_DE_TENTATIVAS):
    while True:
        tentativa_de_login = input ("Digite o seu login : ")
        tentativa_de_senha = int (input ("Digite a sua senha : "))

        if tentativa_de_login == login and tentativa_de_senha == senha :
            print ("Bem vindo ! ")
            break
        else : 
            print ("Login ou senha inválidas ! ")


    