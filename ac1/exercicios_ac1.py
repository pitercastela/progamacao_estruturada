#exercício 1

a = int(input("insira o termo a da equação:"))
b = int(input("insira o termo b da equação:"))
c = int(input("insira o termo c da equação:"))

delta = (b ** 2 - 4 * a * c) ** 0.5
raiz1 = (-b + delta)/(a * 2)
raiz2 = (-b - delta)/(a * 2)

print("a primeira raíz é: " + str(raiz1))
print("a segunda raíz é: " + str(raiz2))

print("--" * 30)

#exercício 2

ano = int(input("insira o ano: "))

resultado = str((ano % 100 == 0) and (ano % 400 == 0) or (ano % 100 != 0) and (ano % 4 == 0))
print(resultado)
