#exercício 1
print("Hello World!")

#exercício 2
A = int(input())
B = int(input())

X = A + B
print("X =", X)

#exercício 3
produto1 = input().split(" ")
produto2 = input().split(" ")
preco1 = produto1[2]
preco2 = produto2[2]
quant1 = produto1[1]
quant2 = produto2[1]
total = (float(preco1) * int(quant1)) + (float(preco2) * int(quant2))
print(f"VALOR A PAGAR: R$ {total:.2f}")

#exercício 4
def maior(a, b):
    resultado = (a + b + abs(a - b))//2
    return resultado

nums = input().split(" ")
a = int(nums[0])
b = int(nums[1])
c = int(nums[2])

maior1 = maior(b, c)
resposta = maior(a, maior1)

print(f"{resposta} eh o maior")

#exercício 5
ponto1 = input().split(" ")
ponto2 = input().split(" ")
x1 = float(ponto1[0])
y1 = float(ponto1[1])
x2 = float(ponto2[0])
y2 = float(ponto2[1])

distancia = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
print(f"{distancia:.4f}")