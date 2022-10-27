router = 'Router-14'
seuip = "192.168.009.0"


# Validação em cima da RFC 1918
from verifica_rfc1918 import validaip_rfc1918

resultado = validaip_rfc1918(seuip, router)

if resultado[0] == False:
  print(resultado[1])
elif resultado[0] == True:
  print(resultado[1], resultado[2])
else:
  print('Retorno da função validaip não esperado.')



## validação simples
from nao_verifica_rfc1918 import validaip

resultado = validaip(seuip, router)

if resultado[0] == False:
  print(resultado[1])
elif resultado[0] == True:
  print(resultado[1], resultado[2])
else:
  print('Retorno da função validaip não esperado.')