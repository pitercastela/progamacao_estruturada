"""dicionários se comportam de forma semelhate as listas. porém possuem valores literais"""

dados = {'nome':"pedro",'idade':25}
print(dados['nome'])
print(dados['idade'])

#em dicionários não é necessário o uso de append
dados['sexo']='M'
print(dados['sexo'])

#o del funciona de forma semelhante
del dados['idade']
print(dados)

filmes = {'título':"star wars",
          'ano':1977,
          'diretor':"george lucas"}

#os values são o q atribuimos as classes
#as keys são as próprias classes
#os items são ambos
print(filmes.values())
print(filmes.keys())
print(filmes.items())

for k,v in filmes.items():
    print(f"o {k} é {v} ")

#é possível também inserir dicionários dentro de listas

filme1 = {'título':"star wars",
          'ano':1977,
          'diretor':"george lucas"}
filme2 = {'título':"vingadores",
          'ano':2012,
          'diretor':"joss whedon"}
filme3 = {'título':"matrix",
          'ano':1999,
          'diretor':"wachowski"}

locadora = [filme1, filme2, filme3]

print(locadora[0]['ano'])
print(locadora[2]['título'])

print(f'O filme {filme1["título"]} é do {filme1["diretor"]}')

#modificando um dicionário
pessoa = {'nome':"gustavo", 'idade':22, 'sexo':'masculino'}
pessoa['nome'] = "leandro"
pessoa['peso'] = 98
for k,v in pessoa.items():
    print(f'{k} = {v}')