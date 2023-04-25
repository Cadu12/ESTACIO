from tela import limparTela, pressionarEnter
from dados import isExiste


def adicionar():
  erro = None
  nome = None
  idade = None

  while True:
    limparTela()

    if erro is not None:
      print(erro)
      print()

    try:
      nome = str(input("NOME: ")).upper().strip()
      if len(nome) != 0:
        if all([nome.isalpha() or nome.isspace() for nome in nome]):
          if not isExiste(nome):
            erro = None
            break
          else:
            erro = "ERRO: REGISTRO EXISTE COM ESTE NOME."
        else:
          erro = "ERRO: NOME INVÁLIDO."
      else:
        erro = "ERRO: NOME VAZIO."
    except:
      pass

  while True:
    limparTela()
    print("NOME: " + nome)
    print()

    if erro is not None:
      print(erro)
      print()

    try:
      idade = int(input("IDADE: "))
      if idade >= 0:
        break
    except:
      erro = "ERRO: NÚMERO INVÁLIDO."

  with open("dados", "a") as arquivo:
    arquivo.write(nome + "\t" + str(idade) + "\n")

  limparTela()
  print("REGISTRADO COM SUCESSO.")
  print()

  pressionarEnter()
