# Função validaip que retorna uma lista (bool, informativo, lista com os quatro octetos)
# Parâmetros esperados: IP da rede e o nome do Roteador
#
# Validação do IP:
#
#  1. Verifica se o IP tem três pontos
#  2. Verifica se cada octeto tem mais de três caracteres
#  3. Verifica se cada octeto só tem digitos
#  4. Converte os octetos em inteiros
#  5. Valida se os octetos seguem o padrão de valores entre 0 e 255
#  6. Validação do número do Router se está no padrão IPv4
#  7. Troca do último octeto da rede pelo número do Router


def validaip(ip, roteador):

  # verifica se existem três pontos
  if ip.count('.') != 3:
    return [False, 'O formato do IP não possui três pontos.']

  # separa os decimais do octeto
  octeto = ip.split('.')

  for i in range(len(octeto)):
    if len(octeto[i]) > 3:
      return [False, f'O octeto da posição {i+1} tem mais de três digitos.']
    if not octeto[i].isdigit():
      return [False, f'O octeto da posição {i+1} não é um número inteiro.']
    else:
      # converte os octetos em inteiros
      octeto[i] = int(octeto[i])
    # Verifica o padão IPv4 dos Octetos
    if octeto[i] < 0 or octeto[i] > 255:
      return [False, f'O octeto da posição {i+1} não não está no padrão IPv4.']

  # Validando o IP final do router
  if roteador.count('-') != 1:
    return [False, 'No nome do roteador não tem traço.']
  roteador = roteador.split('-')
  host = roteador[1]
  if len(host) > 3 or not host.isdigit():
    return [False, "O número do roteador não está no padrão IPv4."]

  # Substituindo o último octeto da rede pelo número do Router
  octeto[3] = int(host)
  
  return [True, 'IP de rede Validado!', octeto] 
