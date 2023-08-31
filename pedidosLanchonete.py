#usei o zero pois o valor so vai ser atribuido a mais quando for escolhido cada pedido
print(' ')
print("Bem vindo a Lanchonete Hora do Lanche!")
print("*****************Cardápio*****************")
print('| Código | Descrição             | Valor |')
print('|  100   | Cachorro Quente       |  9,00 |')
print('|  101   | Cachorro Quente Duplo | 11,00 |')
print('|  102   | X-Egg                 | 12,00 |')
print('|  103   | X-Salada              | 12,00 |')
print('|  104   | X-Bacon               | 14,00 |')
print('|  105   | X-Tudo                | 17,00 |')
print('|  200   | Refrigerante Lata     |  5,00 |')
print('|  201   | Chá Gelado            |  4,00 |')
pedidos = 0
while True:
    cod = int(input('Insira o código do produto desejado: '))
    if cod == 100:
        pedidos += 9
        nome = 'Cachorro Quente'
        valor = 9.00
        print(f'Você escolheu um {nome} no valor de R$ {valor:.2f}')
        resp = int(input('Deseja fazer mais algum pedido?\n1 - Sim \n0 - Não\n'))
    if resp == 0:
        print (f'Valor total do pedido foi: R$ {pedidos:.2f}.')
        print('Obrigada e um bom dia!')
        break
    elif cod == 101:
        pedidos += 11
        nome = 'Cachorro Quente Duplo'
        valor = 11.00
        print(f'Você escolheu um {nome} no valor de R$ {valor:.2f}')
        resp = int(input('Deseja fazer mais algum pedido?\n1 - Sim \n0 - Não\n'))
    if resp == 0:
        print (f'Valor total do pedido foi: R$ {pedidos:.2f}.')
        print('Obrigada e um bom dia!')
        break
    elif cod == 102:
        pedidos += 12
        nome = 'X-Egg'
        valor = 12.00
        print(f'Você escolheu um {nome} no valor de R$ {valor:.2f}')
        resp = int(input('Deseja fazer mais algum pedido?\n1 - Sim \n0 - Não\n'))
    if resp == 0:
        print (f'Valor total do pedido foi: R$ {pedidos:.2f}.')
        print('Obrigada e um bom dia!')
        break

    elif cod == 103:
        pedidos += 12
        nome = 'X-Salada'
        valor = 12.00
        print(f'Você escolheu um {nome} no valor de R$ {valor:.2f}')
        resp = int(input('Deseja fazer mais algum pedido?\n1 - Sim \n0 - Não\n'))
        if resp == 0:
            print (f'Valor total do pedido foi: R$ {pedidos:.2f}.')
            print('Obrigada e um bom dia!')
            break
        elif cod == 104:
            pedidos += 14
            nome = 'X-Bacon'
            valor = 14.00
            print(f'Você escolheu um {nome} no valor de R$ {valor:.2f}')
            resp = int(input('Deseja fazer mais algum pedido?\n1 - Sim \n0 - Não\n'))
        if resp == 0:
            print (f'Valor total do pedido foi: R$ {pedidos:.2f}.')
            print('Obrigada e um bom dia!')
            break
        elif cod == 105 :
            pedidos += 17
            nome = 'X-Tudo'
            valor = 17.00
            print(f'Você escolheu um {nome} no valor de R$ {valor:.2f}')
            resp = int(input('Deseja fazer mais algum pedido?\n1 - Sim \n0 - Não\n'))
        if resp == 0:
            print (f'Valor total do pedido foi: R$ {pedidos:.2f}.')
            print('Obrigada e um bom dia!')
            break
        elif cod == 200:
            pedidos += 5
            nome = 'Refrigerante lata'
            valor = 5.00
            print(f'Você escolheu um {nome} no valor de R$ {valor:.2f}')
            resp = int(input('Deseja fazer mais algum pedido?\n1 - Sim \n0 - Não\n'))
        if resp == 0:
            print (f'Valor total do pedido foi: R$ {pedidos:.2f}.')
            print('Obrigada e um bom dia!')
            break
        elif cod == 201:
            pedidos += 4
            nome = 'Chá gelado'
            valor = 4.00
            print(f'Você escolheu um {nome} no valor de R$ {valor:.2f}')
            resp = int(input('Deseja fazer mais algum pedido?\n1 - Sim \n0 - Não\n'))
        if resp == 0:
            print (f'Valor total do pedido foi: R$ {pedidos:.2f}.')
            print('Obrigada e um bom dia!')
            break
        elif cod != 201 and cod != 200 and cod != 100 and cod != 101 and cod != 102 and cod != 103 and cod != 104 and cod != 105:
            print('Insira valores válidos!')
            resp = int(input('Deseja fazer mais algum pedido?\n1 - Sim \n0 - Não\n'))
        if resp == 1:
            continue
        if cod != 201 and cod != 200 and cod != 100 and cod != 101 and cod != 102 and cod !=103 and cod != 104 and cod != 105:
           print('Insira valores válidos!')
        elif resp == 0:
            print (f'Valor total do pedido foi: R$ {pedidos:.2f}.')
            print('Obrigada e um bom dia!')
            break
#usei as condicionais para cada opção do codigo
#atribui as variaveis em cada condicional de acordo com o necessário
#encerrei o programa com o break 