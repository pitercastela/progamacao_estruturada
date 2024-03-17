#exercício 1

def determina_tipo_triangulo(a, b, c):
    if a + b > c and b+c > a and c+a > b:
        if a == b == c:
            return "equilátero"
        if a == b or a == c or b == c:
            return "isósceles"
        else:
            return "escaleno"
    else:
        return "não é um triangulo"

def testa_triangulo():
    print(determina_tipo_triangulo(4, 4, 4)) # Equilátero
    print(determina_tipo_triangulo(2, 4, 4)) # Isósceles
    print(determina_tipo_triangulo(3, 4, 5)) # Escaleno
    print(determina_tipo_triangulo(1, 1, 4)) # Não é um triângulo

testa_triangulo()

#exercício 2

def dia_semana(dia):
    match dia:
        case 1:
            return "domingo"
        case 2:
            return "segunda feira"
        case 3:
            return "terça feira"
        case 4:
            return "quarta feira"
        case 5:
            return "quinta feira"
        case 6:
            return "sexta feira"
        case 7:
            return "sábado"
        case _:
            return ""

def testa_dia_semana():
    print(dia_semana(2)) # segunda-feira
    print(dia_semana(6)) # sexta-feira
    print(dia_semana(7)) # sábado
    print(dia_semana(9)) # string vazia

testa_dia_semana()

#exercício 3

def ler_numero():
    """retorna float's com os números escolhidos"""
    numero1 = input("informe um número: ")
    numero2 = input("informe outro número: ")
    return float(numero1), float(numero2)

def ler_operacao():
    """retorna o tipo de operação escolhida pelo usuário"""
    return input("informe a operação: ")

def seleciona_operacao(numero1, numero2, operacao):
    """seleciona uma operação das disponíveis"""
    if operacao:
        if operacao == "soma":
            resultado = soma(numero1, numero2)
        elif operacao == "subtração":
            resultado = subtracao(numero1, numero2)
        elif operacao == "multiplicação":
            resultado = multiplicacao(numero1, numero2)
        elif operacao == "divisão":
            resultado = divisao(numero1, numero2)
        return resultado
    else: print("operação inválida")


def soma(x, y):
    """soma os dois números selecionados"""
    return x + y

def subtracao(x, y):
    """subtrai os dois números selecionados"""
    return x - y

def multiplicacao(x, y):
    """multiplica os dois números selecionados"""
    return x * y

def divisao(x, y):
    """divide os dois números selecionados"""
    return x / y

def imprimeresultado(resultado):
    "mostra o resulado obtido na operação"
    print(resultado)

def main():
    """orquestra o passo a passo do prgrama"""
    numero1, numero2 = ler_numero()
    operacao = ler_operacao()
    resultado = seleciona_operacao(numero1, numero2, operacao)
    imprimeresultado(resultado)

main()


