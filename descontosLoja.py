print("Bem vindo a Loja de Atacadão!")
valorp = int(input('Insira o valor do produto desejado: '))
qtd = int(input('Insira a quantidade de produtos que você deseja obter: '))
total = qtd * valorp

if qtd <=9:
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