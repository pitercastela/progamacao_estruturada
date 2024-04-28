import math

#ex 1
vezes = int(input())
for i in range(vezes):
    numeros = input().split()
    num1 = int(numeros[0])
    num2 = int(numeros[1])
    if num1 > num2:
        for i in range(1,num1+1):
            if num1 % i == 0 and num2 % i == 0:
                mdc = i
    elif num2 > num1:
        for i in range(1,num2+1):
            if num1 % i == 0 and num2 % i == 0:
                mdc = i
    print(mdc)
#ex 2
while True:
    try:
        [x1, y1, x2, y2] = [int(x) for x in input().strip().split(' ')]
        if(x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0):
            break
        if(x1 == x2 and y1 == y2):
            print('0')
        elif(x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)):
            print('1')
        else:
            print('2')
    except EOFError:
        break

# ex 3

def fatorial(numeral):
    resultado = 1
    if numeral == 0:
        resultado = 1
    else:
        for i in range(1, numeral+1):
            resultado = resultado * i
    return resultado

while True:
    try:
        m, n = [int(x) for x in input().strip().split(' ')]
        print(fatorial(m) + fatorial(n))
    except EOFError:
        break

#ex 4

qntvezes = int(input())
for i in range(qntvezes):
    dias = 0
    comida = float(input())
    while True:
        if comida <= 1:
            print(f"{dias} dias")
            break
        dias += 1
        comida /= 2

#ex 5
z = int(input())
frequencias = [0 for _ in range(2001)]

for _ in range(z):
    num = int(input())
    frequencias[num] += 1
for i in range(1, 2001):
    if frequencias[i] > 0:
        print(f"{i} aparece {frequencias[i]} vez(es)")


#ex 6


def Crivo(n):
    C = [True for _ in range(n)]
    primos = []
    C[1] = False
    primos.append(2)
    for i in range(4, n, 2):
        C[i] = False
    for i in range(3, n, 2):
        if(C[i]):
            primos.append(i)
            for j in range(i * 3, n, 2 * i):
                C[j] = False
    return primos
def ehPrimo(primos, n):
    limite = math.ceil(math.sqrt(n))
    for primo in primos:
        if(primo > limite):
            return True
        elif(n % primo == 0):
            return (n == primo)

    return True
primos = Crivo(65536)
N = int(input())
for _ in range(N):
    X = int(input())

    print('Prime' if ehPrimo(primos, X) else 'Not Prime')

#ex 7

while True:
    mary = 0
    john = 0
    qvezes = int(input())
    if qvezes == False:
        break
    else:
        jogos = input().split()
        for i in range(qvezes):
            if int(jogos[i]) == 0:
                mary += 1
            elif int(jogos[i]) == 1:
                john += 1
        print(f"Mary won {mary} times and John won {john} times")
#ex 8

def func1(x,y):
    return ((3 * x)**2)+ (y**2)

def func2(x,y):
    return (2 * (x**2)) + ((5 *y) ** 2)

def func3(x,y):
    return (-100 * x) + (y **3)

numdevezes = int(input())
for _ in range(numdevezes):
    xey = input().split()
    Rafael = func1(int(xey[0]), int(xey[1]))
    Beto = func2(int(xey[0]), int(xey[1]))
    Carlos = func3(int(xey[0]), int(xey[1]))
    if Rafael > Carlos and Rafael > Beto:
        print("Rafael ganhou")
    elif Carlos > Rafael and Carlos > Beto:
        print("Carlos ganhou")
    elif Beto > Carlos and Beto > Rafael:
        print("Beto ganhou")
