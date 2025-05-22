opcao=-1
while opcao != 0:
    print("n--- Calculadora ---")
    print("1 - Somar ")
    print("2 - Subtrair")
    print("3 - Multiplicar ")
    print("4 - Dividir")
    print("0 - sair")
    
    opcao = int(input("Escolha uma opção:"))
    
    if opcao in [1,2,3,4]:
        num1 = float(input("Digite o primeiro número:"))
        num2 = float (input("Digite o segundo número:"))
        
    if opcao == 1:
        print(f"Resultado : {num1 + num2}")
    elif opcao == 2: 
        print(f"Resultado {num1 - num2}")
    elif opcao == 3:
        print(f"Resultado {num1 * num2}")
    elif opcao == 4:
        if num2 != 0:
            print(f"Resultado:{num1 / num2}")
        else:
            print("Erro: Divisão pro zero.")
    elif opcao == 0 :
        print("Encerrado...")
    else:
        print("Opção Inválida.")
                