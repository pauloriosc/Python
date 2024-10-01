def contar_as(string):

  # Converte toda a string para minúsculas para facilitar a contagem
  string_minusc = string.lower()

  # Conta as ocorrências da letra 'a'
  contagem = string_minusc.count('a')

  # Verifica se a letra 'a' existe na string
  if contagem > 0:
    print(f"A letra 'a' aparece {contagem} vezes na string.")
  else:
    print("A letra 'a' não foi encontrada na string.")

# Exemplos de uso:
# 1. String definida no código:
minha_string = "Olá, mundo! Amo programar em Python."
contar_as(minha_string)

# 2. String fornecida pelo usuário:
string_usuario = input("Digite uma string: ")
contar_as(string_usuario)
