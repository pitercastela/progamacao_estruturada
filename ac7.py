#1048
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

#1065

numeros = []
numerospares = 0
for i in range(5):
    numeros.append(int(input()))

for i in numeros:
    if i % 2 == 0:
        numerospares += 1
print(numerospares, "valores pares")

#1132
numerais = []
for i in range(2):
    numeros.append(int(input()))
numeraiss = sorted(numeros)
resultado = 0
for i in range(numerais[0], numerais[1]+1):
    if i % 13 != 0:
        resultado += i
print(resultado)

#1773
numero = int(input())
n = []
for i in range(10):
    n.append(numero)
    numero *= 2
    print(f"N[{i}] = {n[i]}")

#1180

qt_de_vezes = int(input())
lista_junta = input()
lista_strings = lista_junta.split()
lista_int = []
for i in range(qt_de_vezes):
    lista_int.append(int(lista_strings[i]))
lista_sorteada = sorted(lista_int)
menor_numero = lista_sorteada[0]
print(f"Menor valor: {menor_numero}")
for i in range(qt_de_vezes):
    if lista_int[i] == menor_numero:
        print(f"Posicao: {i}")

#1882
coluna = int(input())
operacao = input()
matriz = []
resultado = 0
for i in range(12):
    linha = []
    for i in range(12):
        linha.append(float(input()))
    matriz.append(linha)

if operacao == "s":
    for i in range(12):
        resultado += matriz[coluna][i]
elif operacao == "m":
    for i in range(12):
        resultado += matriz[coluna][i]
    resultado = resultado/12
print(resultado)

#1244
n = int(input())
for _ in range(n):
    entrada = input()
    palavras = entrada.split(" ")

    palavras.sort(key=len, reverse=True)
    print(" ".join(palavras))