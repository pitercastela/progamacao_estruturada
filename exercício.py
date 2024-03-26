aluno = {}
aluno['nome'] = input("nome: ")
aluno['media'] = float(input(f"média de {aluno['nome']}: "))
if aluno['media'] < 7:
    aluno['situação'] = "reprovado"
else:
    aluno['situação'] = "aprovado"

for k,v in aluno.items():
    print(f"{k}: {v}")