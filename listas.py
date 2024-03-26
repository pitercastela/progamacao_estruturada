#criação de uma lista
lista_compras = ["banana", "maçã", "laranja"]
"""listas são criadas a partir do zero, ou seja o termo 0 é banana, o 1 é maçã e assim por diante
   também é possível usar os termos de trás para frente, o termo -1 é laranja, o -2 é maçã, etc"""



#append: é uma função q adiciona um novo item ao final de uma lista
lista_compras.append("maracujá")

#o insert funciona de forma similar ao append, porém vc deve sinalizar a posição do novo item
lista_compras.insert(1, "chocolate")

#del serve para deletar um item de uma posição específica
del lista_compras[4]

#remove serve para vc deletar um item específico independente de sua posição
lista_compras.remove("chocolate")

#pop serve de forma semelhante ao del, porém ele é capaz de guardar p valo removido em uma variável
lista_compras.append("carro")
sonho = lista_compras.pop(-1)
lista_sonhos = [sonho]
print(lista_sonhos)

#sort, é uma função q coloca a lista em modo crescente por padrão
numeros = [7, 8, 6, 9, 3, 2, 4, 1, 5]
numeros.sort()
escritos = ["um", "dois", "tres", "quatro", "cinco", "seis"]
del numeros[-1]
del numeros[-1]
del numeros[-1]
print(numeros)

junção = []
for i in range(6):
    tupla = (numeros[i], escritos[i])
    junção.append(tupla)
    print(junção)
