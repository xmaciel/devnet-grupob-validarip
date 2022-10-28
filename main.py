from Cod_base_grupoB import validaip_rfc1918

router = '10'

# Solicitar o IP da rede
#seuip = input('Qual o IP da rede do Site: ')

i = 1
while i < 4:
  seuip = input('Qual o IP da rede do Site? \n')
  print('\n')
  lista_ip = validaip_rfc1918(seuip, router)  
  if lista_ip[0] == False:
    print(lista_ip[1],'\n')
  elif lista_ip[0] == True:
    print(lista_ip[1], lista_ip[2],'\n')
    break
  else:
    print('Retorno da função validaip não esperado.')
    break
  i += 1
 