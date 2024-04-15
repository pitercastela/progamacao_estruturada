import random

aventureiro = {
    "forca": random.randint(10, 18),
    "defesa": random.randint(10, 18),
    "vida": random.randint(100, 120),
    "posicao": [0, 0]
}
aventureiro["posicao"][0] += 1
aventureiro["posicao"][0] += 1
print(aventureiro["posicao"][0])