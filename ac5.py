import random

def main():
    #aventureiro
    hp_aventureiro = 100
    atk_aventureiro = random.randint(10, 20)
    defesa_aventureiro =random.randint(1, 5)

    #monstro
    hp_monstro = random.randint(60, 80)
    atk_monstro = random.randint(20, 30)

    rodada = 1

    print("aventureiro: vida", hp_aventureiro, "-", "att", atk_aventureiro, "-", "def", defesa_aventureiro)
    print("monstro: vida", hp_monstro, "-", "att", atk_monstro)

    while rodada:
        print("rodada", rodada)
        hp_monstro = hp_monstro - random.randint(1, atk_aventureiro)
        if hp_monstro <= 0:
            print("O monstro morreu!")
            break
        hp_aventureiro = hp_aventureiro - (random.randint(1, atk_monstro) - defesa_aventureiro)
        if hp_aventureiro<= 0:
            print("O aventureiro morreu!")
            break
        print("aventureiro: vida", hp_aventureiro, "-", "att", atk_aventureiro, "-", "def", defesa_aventureiro)
        print("monstro: vida", hp_monstro, "-", "att", atk_monstro)
        rodada += 1

main()