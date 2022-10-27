from verifica_rfc1918 import validaip

#teste que o grupo A precisa fazer
router = 'Router-14'
seuip = "192.168.009.0"
resultado = validaip(seuip, router)

if resultado[0] == False:
  print(resultado[1])
elif resultado[0] == True:
  print(resultado[1], resultado[2])
else:
  print('Retorno da função validaip não esperado.')
