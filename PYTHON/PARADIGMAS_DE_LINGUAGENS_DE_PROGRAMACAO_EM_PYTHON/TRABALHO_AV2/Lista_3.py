def converter(hora, minuto):
    return f"{hora if hora <= 12 else hora - 12:02}:{minuto:02} {'AM' if hora < 12 else 'PM'}"

while True:
    hora = int(input("Informe a hora ou digite negativo para sair: "))
    if hora < 0:
        break

    minuto = int(input("Informe os minutos: "))

    print(converter(hora, minuto))