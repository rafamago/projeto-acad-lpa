listaPecas = []

def cadastrarPeca (codigo):
    print('Você selecionou a opção de Cadastrar peças')
    print(f'O código da peça será: {codigo}')
    peca = input("Informe a peça desejada:")
    fabricante = input('Fabricante desejado:')
    valorPeca = float(input('Digite o valor da peça:'))
    dicionarioPeca = {'codigo' : codigo, 'peca' : peca, 'fabricante': fabricante}
    listaPecas.append(dicionarioPeca.copy())
def consultarPeca():
 while True:
    try:
        print('Você selecionou a opção de Consulta de peças')
        print('Digite a opção desejada:\n 1- Consultar todas as peças\n 2- Consultar peças por código\n 3- Consultar peças por fabricante\n 4- Retornar')
        consulta = int(input())
        if consulta == 1:
            print('-' * 15)
            for pecas in listaPecas:
                for key, value in pecas.items():
                    print('{} : {}'.format(key,value))
                    print('-' * 15)
        if consulta == 2:
            print('Consulta de peças por código')
            escolha = int(input('Digite o código da peça desejada: '))
            print('-' * 15)
            for pecas in listaPecas:
                if(pecas['codigo'] == escolha):
                    for key, value in pecas.items():
                        print('{} : {}'.format(key,value))
                        print('-' * 15)
        if consulta == 3:
                print('Consulta pelo nome do fabricante')
                nomeF = input('Digite o nome do fabricante desejado: ')
                print('-' * 15)
                for pecas in listaPecas:
                    if(pecas['fabricante'] == nomeF):
                        for key, value in pecas.items():
                            print('{} : {}'.format(key,value))
                            print('-' * 15)
        if consulta == 4:
            break
        else:
            print('Por favor digite valores válidos')
            continue
    except:
            print('O programa só irá funcionar com valores válidos')
def removerPeca():
 print('Você selecionou a opção de Remoção de Peças')
 cod = int(input('Digite o código da peça a ser removida: '))
 for pecas in listaPecas:
    if(pecas['codigo'] == cod):
        listaPecas.remove(pecas)
    else: print('Você removeu o código.')
#chamei a função para remover o cadastro do codigo do armazenamento
#abaixo coloquei o programa principal para rodar
print("Bem vindo ao Controle de Estoque da Bicicletaria ")
armazenado = 0
import random
while True:
    try:
        print("Escolha a opção desejada:")
        print("1 - Cadastrar peças")
        print("2 - Consultar peças")
        print("3 - Remover peças")
        print("4 - Sair")
        opcao = int(input())
        if opcao == 1:
            armazenado = random.randint(0,9999)
            cadastrarPeca(armazenado)
        elif opcao == 2:
            consultarPeca()
        elif opcao == 3:
            removerPeca()
        elif opcao == 4:
            print('Programa encerrado, tenha um bom dia')
            break
        else:
            print('Digite valores válidos por gentileza')
    except:
        print('O programa só irá funcionar com valores válidos')
