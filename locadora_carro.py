dias = int(input("Digite a quatidade de dias alugado: "))
kms = float(input("Digite a quatidade de KM percorridos: "))
valor_dias = dias * 90
valor_KM = kms *0.20
total = valor_dias + valor_KM
print(f"----Recibo----")
print(f"Dias alugados: {dias} x R$90 = R${valor_dias:.2f}")
print(f"KM percorridos:{kms} x R$o.20 = R$ {valor_KM:.2f}")
print(f" Total a pagar: R$ {total:.2f}")

 