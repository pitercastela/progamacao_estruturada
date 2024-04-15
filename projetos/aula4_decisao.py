'''
estruturas de decisão
-if/ eif/ else
-match/ case

'''
def saudacao(turno):
    if turno == "M":
        return("bom dia")
    elif turno == "T":
        return("bom tarde")
    if turno == "N":
        return("boa noite")
    return("dado inválido!")
#o return encerra a função imediatamente
print(saudacao("A"))
print(saudacao("M"))
print(saudacao("T"))
print(saudacao("N"))


def le_nome():
    nome = input("informe seu nome")
    if not nome: #se o nome for igual for igual a false, ou seja, for uma string vazia
        print("nome inválido!")

# ternários
#num ternário a sintaxe se inverte

def e_par(num):
    if num % 2:
        return "é impar"
    return "é par"
def e_par(num):
    return "é impar" if num % 2 else "é par"

print(e_par(2))

print("-"*100)
print("-"*100)
print("-"*100)

#match/case
def saudacao3(turno):
    match turno:
        case "M":
            print("bom dia")
        case "T":
            print("boa tarde")
        case "N":
            print("boa noite")
        case _: #equivalente a else
            print("dado inválido")

saudacao3("N")

def aprovacao(conceito):
    match conceito:
        case "Bom" | "Ótimo" | "Excelente":
            print("aprovado")
        case _:
            print("reprovado")


aprovacao("Bom")