uso_cpu = [
[20, 25, 40, 50, 45, 60, 55, 35, 70, 65],
[30, 35, 50, 60, 40, 55, 60, 45, 50, 55],
[15, 20, 30, 25, 35, 40, 45, 50, 55, 60],
[10, 15, 25, 35, 45, 50, 55, 60, 65, 70],
]
#Organizando listas do menor uso para o maior uso.
def dados_decrescente():
  for indice, valor in enumerate(uso_cpu):
    print(f'A lista {indice + 1} em ordem crescente fica: {sorted(valor)}.')
    print(f'A lista {indice + 1} em ordem decrescente fica: {sorted(valor, reverse=True)}.\n')

print(dados_decrescente())