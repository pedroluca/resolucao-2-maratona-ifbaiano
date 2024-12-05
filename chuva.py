valores = input().strip().split()
matriz = [int(valor) for valor in valores]
tabuleiro = []

for i in range (0, matriz[0]):
    tabuleiro.append(input())

tabuleiro = [[caractere for caractere in linha] for linha in tabuleiro]

for i in range (0, matriz[0]):
    for j in range (0, matriz[1]):
        if tabuleiro[i][j] == 'o' and i < matriz[0] - 1:
            if tabuleiro[i+1][j] == '.':
                tabuleiro[i+1][j] = 'o'
            else:
                if j > 0 and (tabuleiro[i][j-1] == '.'):
                    tabuleiro[i][j-1] = 'o'
                    if tabuleiro[i+1][j-1] == '.':
                        tabuleiro[i+1][j-1] = 'o'
                    else:
                        for k in range (j-1, 0, -1):
                            if tabuleiro[i][k-1] == '.' and tabuleiro[i+1][k] != 'o':
                                tabuleiro[i][k-1] = 'o'
                                if tabuleiro[i+1][k-1] == '.':
                                    tabuleiro[i+1][k-1] = 'o'
                    
                if j < matriz[1] - 1 and (tabuleiro[i][j+1] == '.' and tabuleiro[i+1][j] != 'o'):
                    tabuleiro[i][j+1] = 'o'
                    if tabuleiro[i+1][j+1] == '.':
                        tabuleiro[i+1][j+1] = 'o'
        else:
            pass

for i in range (0, matriz[0]):
    for j in range (0, matriz[1]):
        print(f"{tabuleiro[i][j]}", end="")
    print(end="\n")