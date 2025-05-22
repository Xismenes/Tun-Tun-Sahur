print("Escolha a conversão")
print("1- Celcius para fahrenhient")
print("2-Celcius para kelvin")
opcao= int(input("Digite a sua opção"))
if  opcao== 1:
    temp = float(input("Digite a temperatura em Celcius"))
    fahrenheint = (temp *9 / 5) +32
    print(f"{temp}°C = {fahrenhenti:.2f}f")
elif opcao == 2:
    temp= float(input("Digite a temperatura em Celcius:"))
    kelvin = temp +273.15
    print(f"{temp}°C = {Kelvin:.2f}k")
else:
    print("opção invalida.")
    