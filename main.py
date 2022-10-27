from Cod_base_grupoB import validaip_rfc1918

router = '10'

# Solicitar o IP da rede
#seuip = input('Qual o IP da rede do Site: ')

i = 1
while i < 4:
  seuip = input('Qual o IP da rede do Site? \n')
  print('\n')
  resultado = validaip_rfc1918(seuip, router)  
  if resultado[0] == False:
    print(resultado[1],'\n')
  elif resultado[0] == True:
    print(resultado[1], resultado[2],'\n')
    break
  else:
    print('Retorno da função validaip não esperado.')
    break
  i += 1
 