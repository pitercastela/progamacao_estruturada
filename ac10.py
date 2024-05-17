#arvores
a = int(input())
if input() == "":
    for i in range(a):
        arvores = []
        qtd = []
        while True:
            b = input()
            if b == "":
                break
            arvores.append(b)
        arvores.sort()
        arvores_sem =list(dict.fromkeys(arvores))
        qtd_total = len(arvores)
        for i in arvores_sem:
            c = arvores.count(i)
            qtd.append(c)
        for i in range(len(arvores_sem)):
            print(f"{arvores_sem[i]} {(qtd[i]/qtd_total)*100:.4f}")
        print()