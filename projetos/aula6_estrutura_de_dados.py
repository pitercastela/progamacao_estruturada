x = 2
y = x
print(x, y)#2, 2

x=3
print(x, y)#3, 2

x = [2]
y = x
print(x, y)#[2] [2]

#passagem por referência
x.append(3)
print(x, y)#[2, 3] [2, 3]
def func1(a):
    a.append(2)

func1(x)
print(x)

def func2(a):
    b = a.copy() #shallow copy
    b.append(2)
    return b

y = func2(x)
print(x, y)

def atualiza_lista(lista=[]):
    lista.append(2)
    return lista

x = atualiza_lista()
print(x)

x = atualiza_lista()
print(x)

def atualiza_lista2(lista=None):
    if lista is None:
        lista = []
    lista.append(2)
    return lista

x = atualiza_lista2()
print(x)

x = atualiza_lista2()
print(x)


def adiciona_elemento(dic, matricula, nota):
    dic[matricula] = nota

alunos = {}
adiciona_elemento(alunos, "1234", 7.5)
adiciona_elemento(alunos, "15634", 8.5)
print(alunos)


def op1():
    print("operação 1")
def op2():
    print("operação 2")
def op3():
    print("operação 3")

def erro():
    print("erro")

def main():
    while True:
        opcao = input("informe a opção desejada")
        match opcao:
            case "1":
                op1()
            case "2":
                op2
            case "3":
                op3

opcoes = {"1":op1, "2": op2, "3":op3}
def main():
    while True:
        opcao = input("informe a operação desejada: ")
        opcoes.get(opcao, erro)()

#main()

#compreensão de lista
numeros = [1,2,3,4,5,6,7]

#quadrados = []
#for numero in numeros:
#    quadrados.append(numero ** 2)
quadrados = [numero ** 2 for numero in numeros]

print(quadrados)

matriz = [
    [2,3,4]
    [4,5,6]
    [7,8,9]
]
linha_completa = []
for linha in matriz:
    for elemento in matriz:
        linha_completa.append(elemento)

linha_completa = [elem for linha in matriz for elem in linha]