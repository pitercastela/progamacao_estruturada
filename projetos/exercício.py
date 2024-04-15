'''
def comparador_num(num1, num2):
    if num1 > num2: return num1
    else: return             num2

print(comparador_num(7, 10))

def conferidor_pos_neg(num):
    if num > 0:
        num = "positivo"
    else:
        num = "negativo"
    return num

print(conferidor_pos_neg(-7))

def consoante_ou_vogal(letra):
    match letra:
        case "a"|"e"|"i"|"o"|"u":
            return "vogal"
    return "consoante"

print(consoante_ou_vogal("a"))
'''
def nota_valida(nota):
    return 0 <= nota <= 10

def calcula_media(nota1, nota2, nota3):
    media = (int(nota1) + int(nota2) + int(nota3))/3
    if nota_valida(int(nota1)) and nota_valida(int(nota2)) and nota_valida(int(nota3)):
        if media < 0 or media > 10: return "nota inválida"
        elif media == 10: return "Aprovado com Distinção"
        elif media >= 7: return "aprovado"
        else: return "reprovado"
    else: return "nota inválida"

print(calcula_media(input("nota 1:"), input("nota 2:"), input("nota 3:")))

