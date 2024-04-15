#1048
'''
salario = float(input())
if salario >= 0 and salario <= 400.00:
    reajuste = 0.15
elif salario >= 400.01 and salario <= 800:
    reajuste = 0.12
elif salario >= 800.01 and salario <= 1200:
    reajuste = 0.10
elif salario >= 1200.01 and salario <= 2000:
    reajuste = 0.07
elif salario > 2000:
    reajuste = 0.04
novo_salario = salario + salario*reajuste

print(f"Novo salario: {novo_salario:.2f}")
print(f"Reajuste ganho: {salario*reajuste:.2f}")
print("Em percentual:", int(reajuste*100),"%")
'''
#1065
'''
numeros = []
numerospares = 0
for i in range(5):
    numeros.append(int(input()))

for i in numeros:
    if i % 2 == 0:
        numerospares += 1
print(numerospares, "valores pares")
'''
#1132
numeros = []
for i in range(2):
    numeros.append(int(input()))
numeros = sorted(numeros)
resultado = 0
for i in range(numeros[0], numeros[1]+1):
    if i % 13 != 0:
        resultado += i
print(resultado)