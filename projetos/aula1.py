#introdução a disciplina de python
#primeira parte
#o (#) n precisa estar no começo da linha mas sim no começo do comenário
"""
usar três aspas no início e no fina cria um docstring
q é basicamente um bloco de notas dentro do seu código
"""

#tipos de dados primitivos
#nulo
# print(None)

#int (inteiro)
# print(4, 7, -10, 2)

#(float) valores racionais
# print(4.2, 5.7, 8.9)

#(bool) boolleanos
# print(True, False)

#(str) string/texto
# print("hello world")
# print('hello world') #pode usar aspas simples para str também
print("olá", 22, "mundo", end=" ")
# print("olá", 22, "mundo", sep = "_")

#charactere de escape//escape char
#mostra pro python q o próximo cacractere não é literal
#\n da um enter (no texto)
#\t dá um tab (no texto)
# print("ola, \"mundo\"")
# print("ola, \nmundo")
# print("ola, \tmundo")
"""se usar três aspas dá pra escrever texto em mais de uma linha"""
# print("""texto com múltiplas linhas
    #   tipo isso aqui""")#também da pra usar aspas simples(é mais usado també,)

#lendo dados do usuário
# print(input("seu nome é:"))

#variáveis
#convensão de nomeação de variáveis: letras minusculas(snake case), começar com uma letra
#usando _ entre as palavras
nome = input("seu nome é? ")
print("olá", nome)

#python é uma linuagem de tipagem fraca e dinâmica
#python não possui constantes
#quando se quer criar uma "constante" se usa letra maiúscula

PI = 3.1415 #"constante"
