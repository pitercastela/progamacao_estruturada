
#método para criar uma matriz com um n de linhas, de colunas e o elemento de preenchimento
def cria_matriz(n_linhas, n_colunas, valor):
    ''' (int, int, valor) -> matriz (lista de listas)
    Cria e retorna uma matriz com n_linhas linha e n_colunas
    colunas em que cada elemento é igual ao valor dado.
    '''

    matriz = [] # lista vazia
    for i in range(n_linhas):
        # cria a linha i
        linha = [] # lista vazia
        for j in range(n_colunas):
            linha += [valor]

        # coloque linha na matriz
        matriz += [linha]
    return matriz

#-----------------------
A = cria_matriz(5,5,0)
A[0][0] = "@"
A[0][4] = "x"
#método para imprimir uma matriz(na forma de matriz)
for i in range(0, 5):
    print(A[i])