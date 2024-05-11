#ex 1
print(f"{int(input())*2} minutos")

#ex 2
b = int(input())
c = 1
for i in range(1, b+1):
    c *= i
print(c)

#ex 3
d = int(input())

for _ in range(d):
    e = int(input())

    precos = {}

    for _ in range(e):
        fruta, preco = input().strip().split(' ')

        precos[fruta] = float(preco)

    f = int(input())

    resposta = 0.0
    for _ in range(f):
        fruta, quantidade = input().strip().split(' ')

        resposta += int(quantidade) * precos[fruta]

    print(f'R$ {resposta:.2f}')

#ex 4
g = input()
nums = input().split(" ")
print(nums.count(g))

#ex 5
h = input().split(" ")
if int(h[0])*int(h[2]) <= int(h[1]):
    print("S")
else:
    print("N")

#ex 6
l = int(input())
m = 0
for i in range(l):
    n = input().split(" ")
    m += int(n[0]) * int(n[1])
print(m)

#ex7
print(int(input())*4)

#ex8
o = 1
p = []
q = int(input())
for i in range(q):
    p.append(int(input()))

for i in range(q):
    if p[i-1] == 1 or p[i-1] == 2:
        if p[i-1] != p[i]:
            o += 1

print(o)