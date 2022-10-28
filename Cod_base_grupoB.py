# Função validaip que retorna uma lista (bool, informativo, lista com os quatro octetos)
# Parâmetros esperados: IP da rede e o nome do Roteador
#
# Premissas:
#  - só pode ser um IP de classe A, B ou C privada
#
# Validação do IP:
#
#  1. Verifica se o IP tem três pontos
#  2. Verifica se cada octeto tem mais de três caracteres
#  3. Verifica se cada octeto só tem digitos
#  4. Converte os octetos em inteiros
#  5. Valida se o IP segue o padrão da RFC 1918 para IPs privados
#  5.1 Só aceita máscaras menores que 31
#  6. Validação do número do Router se está no padrão IPv4
#  7. Troca do último octeto da rede pelo número do Router


def validaip_rfc1918(ip, roteador):

  # verifica se existem três pontos
  if ip.count('.') != 3:
    return [False, 'O formato do IP não possui três pontos.']

  # separa os decimais do octeto
  octeto = ip.split('.')

  for i in range(len(octeto)):
    if len(octeto[i]) > 3:
      return [False, f'O octeto da posição {i+1} tem mais de três digitos.']
    if not octeto[i].isdigit():
      return [False, f'O octeto da posição {i+1} não é um número inteiro positivo.']
    else:
      # converte os octetos em inteiros
      octeto[i] = int(octeto[i])   

  # Módulo do último octeto para saber se é uma rede válida
  # pois o último octeto deve ser um número par
  parouimpar = octeto[3] % 2

  # Classe A Privada
  if octeto[0] == 10:
    # Segundo octeto
    if octeto[1] < 0 or octeto[1] > 255:
      return [False, 'O segundo octeto deve ser um inteiro entre 0 e 255']
    # Terceiro octeto
    if octeto[2] < 0 or octeto[2] > 255:
      return [False, 'O terceiro octeto deve ser um inteiro entre 0 e 255']
    # Quarto octeto
    if octeto[3] < 0 or octeto[3] > 252 or parouimpar != 0:
      return [False, 'O quarto octeto deve ser um inteiro par entre 0 e 252']

  # Classe B Privada
  elif octeto[0] == 172:
    # Segundo octeto
    if octeto[1] < 16 or octeto[1] > 31:
      return [False, 'O segundo octeto deve ser um inteiro entre 16 e 31']
    # Terceiro octeto
    if octeto[2] < 0 or octeto[2] > 255:
      return [False, 'O quarto octeto deve ser um inteiro entre 0 e 252']
    # Quarto octeto
    if octeto[3] < 0 or octeto[3] > 252 or parouimpar != 0:
      return [False, 'O quarto octeto deve ser um inteiro par entre 0 e 252']

  # Classe C Privada
  elif octeto[0] == 192:
    # Segundo octeto
    if octeto[1] != 168:
      return [False, 'O segundo octeto dever ser o inteiro 168']
    # Terceiro octeto
    if octeto[2] < 0 or octeto[2] > 255:
      return [False, 'O terceiro octeto deve ser um inteiro entre 0 e 255']
    # Quarto octeto
    if octeto[3] < 0 or octeto[3] > 252 or parouimpar != 0:
      return [False, 'O quarto octeto deve ser um inteiro par entre 0 e 252']
      
  else:
    return [False, 'Seu IP de rede deve ser do tipo privado de calsse A, B ou C, seguindo o padrão da RFC 1918. Fonte: https://www.rfc-editor.org/rfc/rfc1918.html']

  # Validando o IP final do router
  if len(roteador) > 3 or not roteador.isdigit() or int(roteador) >= 255 or int(roteador) <= 0:
    return [False, "O número do roteador não está no padrão IPv4."]

  # Substituindo o último octeto da rede pelo número do Router
  octeto[3] = int(roteador)
  
  return [True, 'IP de rede Validado!', octeto]
  