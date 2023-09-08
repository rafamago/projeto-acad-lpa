#chamei as funções de acordo com cada exigência, cada condição de acordo com o desejado e coloquei tratamento de erro com o try e except 
def dimensoesObjeto():
    while True:
        try:
            comp = int(input('Digite o comprimento do objeto (em cm):'))
            largura = int(input('Digite a largura do objeto (em cm):'))
            altura = int(input('Digite a altura do objeto (em cm):'))
        except:
            print('Você digitou um valor não numérico, tente novamente com números por favor')
            continue
        volume = altura * largura * comp
        multiplicadorDimensao = volume
        print(f'O volume do objeto é (em cm³):{volume}')
        if volume == 0:
            print('Volume zero, favor digitar valores diferente de zero e tente novamente!')
            continue
        elif volume < 1000:
            multiplicadorDimensao = 10
            break
        elif 1000 <= volume and volume < 10000:
            multiplicadorDimensao = 20
            break
        elif 10000 <= volume and volume < 30000:
            multiplicadorDimensao = 30
            break
        elif 30000 <= volume and volume < 100000:
            multiplicadorDimensao = 50
            break
        else:
            print ('Volume não aceito')
            continue
    print(f'Valor referente ao volume = R${multiplicadorDimensao:.2f}')
    return multiplicadorDimensao
def pesoObjeto() :
 while True:
    try:
        peso = int(input('Digite o peso do objeto (em kg):'))
    except:
        print('Você digitou um valor não numérico')
        print('Por favor entre com o peso desejado novamente')
        continue
        print(f'O peso do objeto é (em kg):{peso}')
    if peso <= 0.1:
        multiplicadorPeso = 1 
        break
    elif 0.1 <= peso and peso < 1 :
        multiplicadorPeso = 1.5
        break
    elif 1 <= peso and peso < 10 :
        multiplicadorPeso = 2
        break
    elif 10 <= peso and peso < 30 :
        multiplicadorPeso = 3
        break
    elif peso >= 10000:
        print('Não aceitamos objetos tão pesados')
        continue
    else:
        print('Não é aceito')
        continue
 print(f'Valor referente ao peso = R${multiplicadorPeso:.2f}')
 return multiplicadorPeso
def rotaObjeto() :
 while True:
    print('Selecione a rota:')
    print('BR - De Brasília para Rio de Janeiro')
    print('BS - De Brasília para São Paulo')
    print('RB - De Rio de Janeiro para Brasília')
    print('RS - De Rio de Janeiro para São Paulo')
    print('SR - De São Paulo para Rio de Janeiro')
    print('SB - De São Paulo para Brasília')
    rota = str(input()).upper()

    multiplicadorRota = rota
    if rota == 'BR':
        multiplicadorRota = 1.5

    elif rota == 'BS':
        multiplicadorRota = 1.2

    elif rota == 'RB':
        multiplicadorRota = 1.5

    elif rota == 'RS':
        multiplicadorRota = 1

    elif rota == 'SR' :
        multiplicadorRota = 1

    elif rota == 'SB':
        multiplicadorRota = 1.2
    else:
        print('Você inseriu uma opção inválida, tente novamente')
        continue
    print(f'Valor referente a rota = R${multiplicadorRota:.2f}')
    return multiplicadorRota
    break
multiplicadorObjeto = dimensoesObjeto()
multiplicadorPeso = pesoObjeto ()
multiplicadorRota = rotaObjeto()
total = multiplicadorObjeto * multiplicadorPeso * multiplicadorRota
print(f'Preço total a ser pago: R$ {total:.2f} (dimensões: {multiplicadorObjeto} * peso:{multiplicadorPeso} * rota: {multiplicadorRota})')
print('Obrigada e um bom dia!')
exit()
#retornei os valores que foram atribuidos e fiz a multiplicação do total
