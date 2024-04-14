import random


tabuleiro = []
tamanho_tabuleiro = 5

for _ in range(tamanho_tabuleiro):
    tabuleiro.append(["~"] * tamanho_tabuleiro)

def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(linha))
  
def posicionar_navio(tabuleiro):
    linha_navio = random.randint(0, tamanho_tabuleiro - 1)
    coluna_navio = random.randint(0, tamanho_tabuleiro - 1)
    tabuleiro[linha_navio][coluna_navio] = "N"
    return linha_navio, coluna_navio

print("Bem-vindo ao Jogo de Batalha Naval!")
print("Escolha uma linha e uma coluna de 0 a 4 para atacar.")
linha_navio, coluna_navio = posicionar_navio(tabuleiro)

for turno in range(4):
    print(f"Turno {turno + 1}")
    palpite_linha = int(input("Adivinhe a linha: "))
    palpite_coluna = int(input("Adivinhe a coluna: "))

    if palpite_linha < 0 or palpite_linha >= tamanho_tabuleiro or palpite_coluna < 0 or palpite_coluna >= tamanho_tabuleiro:
        print("Palpite fora do tabuleiro! Tente novamente.")
    elif tabuleiro[palpite_linha][palpite_coluna] == "X":
        print("Você já tentou esta posição. Tente novamente.")
    elif tabuleiro[palpite_linha][palpite_coluna] == "N":
        print("Parabéns! Você afundou o navio!")
        tabuleiro[palpite_linha][palpite_coluna] = "X"
        exibir_tabuleiro(tabuleiro)
        break
    else:
        print("Você errou!")
        tabuleiro[palpite_linha][palpite_coluna] = "X"

    if turno == 3:
        print("Fim do jogo! O navio estava na linha", linha_navio, "e coluna", coluna_navio, end=".")
        print()
        tabuleiro[linha_navio][coluna_navio] = "N"
        exibir_tabuleiro(tabuleiro)


