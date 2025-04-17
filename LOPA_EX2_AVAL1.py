
uso_cpu = [
[20, 25, 40, 50, 45, 60, 55, 35, 70, 65],
[30, 35, 50, 60, 40, 55, 60, 45, 50, 55],
[15, 20, 30, 25, 35, 40, 45, 50, 55, 60],
[10, 15, 25, 35, 45, 50, 55, 60, 65, 70],
]

def acima_da_media():
  
  for valor in uso_cpu:
    media = sum(valor) / len(valor)
    print(f'A média da região {valor} é: {media}')

print(acima_da_media())