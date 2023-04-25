from tela import limparTela, pressionarEnter
from listar import listar
from dados import isExiste


def remover():
  erro = None

  while True:
    limparTela()
    listar()

    if erro is not None:
      print(erro)
      print()

    nome = str(input("NOME PARA REMOVER: ")).upper().strip()

    if isExiste(nome):
      dados = []

      with open("dados", "r") as arquivo:
        for linha in arquivo.readlines():
          if linha.split("\t")[0] != nome.upper().strip():
            dados.append(linha)

      with open("dados", "w") as arquivo:
        for dado in dados:
          arquivo.write(dado)

      limparTela()
      print("REMOVIDO COM SUCESSO.")
      print()

      pressionarEnter()
      return

    else:
      erro = "ERRO: REGISTRO NÃO EXISTE."
