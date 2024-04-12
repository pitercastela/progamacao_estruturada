def conta_pares(min, max):
    for i in range(min, max+1,):
        if i >= max - 1:
            if i % 2 == 0:
                print(i)
        elif i % 2 == 0:
            print(i, end=" - ")

#conta_pares(2, 8)

def calcula_fatorial(num):
    resultado = 1
    for i in range(2, num+1):
        resultado = resultado * i
    print(resultado)

calcula_fatorial(1000)

#recursão
#n! = n * (n-1)!
def fatorial2(num):
    if num == 1:
        return 1
    return num * fatorial2(num-1)

print(fatorial2(999))
