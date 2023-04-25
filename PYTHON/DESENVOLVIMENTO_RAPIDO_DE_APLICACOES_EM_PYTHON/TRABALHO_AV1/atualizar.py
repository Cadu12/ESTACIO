from tela import limparTela, pressionarEnter
from listar import listar
from dados import isExiste


def atualizar():
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
          else:
            idade = None

            while True:
              limparTela()
              print("NOME: " + linha.split("\t")[0])
              print()

              if erro is not None:
                print(erro)
                print()

              try:
                idade = int(input("IDADE: "))
                if idade >= 0:
                  erro = None
                  break
              except:
                erro = "ERRO: NÚMERO INVÁLIDO."

            dados.append(linha.split("\t")[0] + "\t" + str(idade) + "\n")

      with open("dados", "w") as arquivo:
        for dado in dados:
          arquivo.write(dado)

      limparTela()
      print("ALTERADO COM SUCESSO.")
      print()

      pressionarEnter()
      return

    else:
      erro = "ERRO: REGISTRO NÃO EXISTE."
