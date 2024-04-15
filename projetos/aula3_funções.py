'''
- encapsulamento
    - evitar a duplicidade de código
- organização do código
'''


'''
parâmetros posicionais devem vir antes de parâmetros chaves
esses são definidos deixando eles explicitos "traco = "." é um parâmetro chave
largura não
'''
def linha(largura, traco = "."):
    print(traco * largura)

def cabecalho(titulo):
    linha(50)
    print(titulo)
    linha(50, traco = "-")

cabecalho("bom dia")
cabecalho("boa noite")

#isso não é chamar a função e sim referencia-la
cabecalho
print(cabecalho)

def soma(a, b):
    return a + b
print(soma(4, 8) + soma(2, -5))

#múltiplos retornos
def subsequentes(x):
    return x + 1, x + 2 #tupla

print(subsequentes(10))

x = 0 #escopo global
#sempre q possível evite variáveis de escopo global a não ser q seja uma constante
def func1():
    x = 2 #escopo local
    print(x)

#alterando parâmetros globais dentro de uma função
def func2():
    global x #não é uma boa prática
    x = 3
    print(x)

#se não houverem variaveis locais com o nome ele usará a global
def func3():
    print(x)

print(x)
func1()
func3()
func2()
print(x)

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def main():
    x = 10
    y = 2
    print(soma(x, y))

main()

#receber dados significa trabalhar com parâmetros
#ler dados significa usar o input
#retornar parametros é usar o return
#escrever é usar o print