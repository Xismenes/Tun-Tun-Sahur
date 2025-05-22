nome=input("Digite o nome do vendedor: ")
salario_fixo=float(input("Digite o salario fixo:"))
vendas= int(input("Digite o total de vendas efetuadas :"))
if vendas >= 20:
    bonus = salario_fixo * 0.15
    salario_total = salario_fixo + bonus
    print(f"Meta atingida! {nome} recebeu R$ {bonus:.2f}de comissão.")
    print(f"Salario final: R$ {salario_total:.2f}")
else:
    print("Meta nõa atingida.")
    