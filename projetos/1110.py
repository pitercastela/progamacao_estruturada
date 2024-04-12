n = 8
cartas = [num for num in range(n, 0, -1)]
print(cartas)
descartadas = []

while len(cartas) >= 2:
    descartadas.append(cartas.pop())
    cartas.insert(0, cartas.pop())
print(cartas)
print(descartadas)
