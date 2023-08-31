print("Bem vindo a Loja em Atacado!")
#coloquei para exibir o nome da loja no começo do programa
valorp = float(input('Insira o valor do produto desejado: '))
qtd = int(input('Insira a quantidade de produtos que você deseja obter: '))
#inseri as variáveis no input de acordo com os valores que cada uma vai obter
total = qtd * valorp
#inseri o calculo do valor total na variável total
#coloquei uma condição de 0 para exibir mensagem de erro pois o dado seria inválido
if valorp <= 0 or qtd == 0 :
 print("Números inválidos! Verifique e tente novamente com outros valores.")
#adicionei uma condição elif para cada um dos diferentes valores que seria apresentado
#de acordo com o desconto de cada um e da escolha de quantidade do cliente
elif qtd <=9:
 print('O total foi de: R$ {:.2f}'.format(total)) 
 print('Nenhum desconto aplicado!')
elif qtd >= 10 and qtd <= 99:
 valorfinal = total - total * 0.05
 print ('O total foi de: R$ {:.2f}'.format(total))
 print('O total com desconto é: R$ {:.2f} (Desconto de 5%!)'.format(valorfinal))
elif qtd >= 100 and qtd <= 999:
 valorfinal = total - total * 0.1
 print( 'O total foi de: R$ {:.2f}'.format(total))
 print('O total com desconto é: R$ {:.2f} (Desconto de 10%!)'.format(valorfinal))
elif qtd >= 1000:
 valorfinal = total - total * 0.15
 print('O total foi de: R$ {:.2f}'.format(total))
 print('O total com desconto é: R$ {:.2f} (Desconto de 15%!)1'.format(valorfinal))
#inseri o cálculo de cada condição dentro da variável valor final
