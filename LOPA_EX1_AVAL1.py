
uso_cpu = [
[20, 25, 40, 50, 45, 60, 55, 35, 70, 65],
[30, 35, 50, 60, 40, 55, 60, 45, 50, 55],
[15, 20, 30, 25, 35, 40, 45, 50, 55, 60],
[10, 15, 25, 35, 45, 50, 55, 60, 65, 70],
]


def uso_maximo():

  for valor in uso_cpu:
    print(f'O maior valor da região {valor} foi: {max(valor)}.')

print(uso_maximo())