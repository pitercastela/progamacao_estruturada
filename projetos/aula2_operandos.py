'''operadores
- Aritméticos
- Atribuição
- Comparação ou relacionais
- Lógicos ou booleanos
'''

'''operadores aritméticos
quando os operandos são numércos'''
x = 8.4
y = 7.2

print(x + y)
print(x - y)
print(x * y) #multiplicação
print(x / y) #divisão
print(x ** y) #potêcia
print(x // y) # divisão onteira
'''divisão inteira numa divisão inteira negativa o resultado é arredondado pra baixo
-7//3 = -3      7/3 = 2'''
print(x % y) # resto de uma divisão


print(round(x + y, 2))
'''round é usado para arredondar valores,
 o 2 representa até q casa decimal ele deve mostrar'''

'''matrizes pode ser criadas através de umm processo de divião inteira e módulo de uma lista'''

# operandos str

print("olá," + "mundo") # Concatenação de strings
print("olá " * 30) # Multiplicação de string

'''strings só podem ser somadas com outras strings
e só podem ser multiplicadas por inteiros'''


#Operadores de atribuição
#atribui o valor da direita a variável da esquerda
#comuns de serem usados
x = 10
x += 2 # x = x + 2
x -= 1 # x = x - 1
x *= 2 # x = x * 2
#e assim por diante com todos os operadores aritméticos

print("- " * 30)

#Operadore de comparação ou relacionais
#retornam um booleano (true/false)
x=10
y=3

print(x > y)
print(x >= y)
print(x < y)
print(x <= y)
print(x == y)
print(x != y)

print("- " * 30)

x = "abc"
y = "Abc"
#a comparação ocorre caracter por caracter, se:
#a e A fosse igual ele iria comparar o próximo caracter,
# se não forem igual ele dá o resulado de imediato

print(x > y)
print(x >= y)
print(x < y)
print(x <= y)
print(x == y)
print(x != y)

print("- " * 30)
print("- " * 30)

# Operadores lógicos
print(True and False) #E
print(True or False) #OU
print(not False) #NÃO
'''
x||y||x E y|| OU || NÃO x|| NÃO y
V||V||V    ||V   ||F     ||F
F||V||F    ||V   ||V     ||F
V||F||F    ||V   ||F     ||V
F||F||F    ||F   ||V     ||V

x||y||
'''
print("- " * 30)
print("- " * 30)

print(int(6.0))
print(float("10.42"))
print(bool("10"))

print("a" and 16 ) #16
#o primeiro operando é verdadeiro, então ele retorna o segundo operando
print(0 and "abc") #"abc"
#se o primeiro operando é falso, ele o retorna

#com a operação or ocorre o contrário
print(0.0 or "") #""
print(1.5 and "texto") # "texto"

#regra básica, quando o termo se confirmar verdadeiro ele retornará o último valor visto

print("- " * 30)
print("- " * 30)

nome = input("informe o nome: ") or "Valor inválido"
print(nome)


'''
precedência de operadores
 ()
**
*
/
//
%
depois
<
<=
>
>=
not
and
or
'''

