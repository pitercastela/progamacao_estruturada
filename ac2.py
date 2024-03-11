#exercício 1

def bhaskara(a, b, c):
    delta = (b ** 2 - 4 * a * c) ** 0.5
    raiz1 = (-b + delta)/(a * 2)
    raiz2 = (-b - delta)/(a * 2)
    return raiz1, raiz2

def ano_bissexto(ano):
    resultado = str((ano % 100 == 0) and (ano % 400 == 0) or (ano % 100 != 0) and (ano % 4 == 0))
    return resultado

#exercício 2

def calcula_salario(valor_hora, num_horas, irpf = 0.275):
    salario_bruto = valor_hora * num_horas
    salario_liquido = salario_bruto - salario_bruto * irpf
    return salario_liquido

