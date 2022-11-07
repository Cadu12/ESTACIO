def trapezio(maior, menor, altura):
    return ((maior + menor) * altura) / 2

maior = float(input("Digite o valor da base maior: "))
menor = float(input("Digite o valor da base menor: "))
altura = float(input("Digite o valor da altura: "))

print(f"O valor da área do trapézio vale {trapezio(maior, menor, altura):.2f}")