nome = input("Digite seu nome: ")
peso = input("Digite seu peso: ")
altura = input(" Digite sua altura: ")

imc= peso / (altura *2)

print(f"{nome}, seu imc é {imc: 2f}")

if imc < 18.5:
    print(f"Classificação: abaixo do peso! ")
elif imc < 25:
    print("Classificação: peso normal. ")
elif imc < 30:
    print("Clssificação: Sobrepeso ")
else:
    print("Classificação: Obesidade. ")