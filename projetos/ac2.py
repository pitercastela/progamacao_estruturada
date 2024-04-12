#exercício 1

def bhaskara(a, b, c):
    delta = (b ** 2 - 4 * a * c) ** 0.5
    raiz1 = (-b + delta)/(a * 2)
    raiz2 = (-b - delta)/(a * 2)
    return raiz1, raiz2

print(bhaskara(1, -6, 8))

#só pra criar uma separação entre os exercícios
print("-" * 60)

#exercício 2

def ano_bissexto(ano = 2000):
    resultado = str((ano % 100 == 0) and (ano % 400 == 0) or (ano % 100 != 0) and (ano % 4 == 0))
    return resultado
print(ano_bissexto())
