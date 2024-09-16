while True:
    entrada = input("Digite um número (ou 0 para sair): ")
    if entrada == '0':
        print("Saindo do loop.")
        break  # Interrompe o loop
    print(f"Você digitou: {entrada}")