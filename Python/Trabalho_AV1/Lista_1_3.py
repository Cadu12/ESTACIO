valor = int(input("Quanto voce ganha por hora: "))
horas = int(input("Numero de horas trabalhadas no mes: "))
salario = valor * horas
print("Salario:", salario)
ir = salario * 0.11
print("Imposto de renda:", ir)
inss = salario * 0.08
print("INSS:", inss)
sind = salario * 0.05
print("Sindicato:", sind)
desc = ir + inss + sind
print("Desconto total:", desc)
print("Salario liquido:", salario - desc)