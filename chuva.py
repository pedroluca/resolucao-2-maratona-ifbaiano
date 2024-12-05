valores = input().strip().split() # Recebe as medidas da matriz em string e separa os valores
matriz = [int(valor) for valor in valores] # Transforma os valores em int
tabuleiro = []

for i in range (0, matriz[0]):
    tabuleiro.append(input()) # Lê o tabuleiro por linha

tabuleiro = [[caractere for caractere in linha] for linha in tabuleiro] # Separa cada caracter do tabuleiro, lista de lista

for i in range (0, matriz[0]):
    for j in range (0, matriz[1]):
        if tabuleiro[i][j] == 'o' and i < matriz[0] - 1: # Busca pela casa com a gota
            if tabuleiro[i+1][j] == '.': # Se a casa abaixo da anterior for vazia, a gota desce
                tabuleiro[i+1][j] = 'o'
            else:
                if j > 0 and (tabuleiro[i][j-1] == '.'): # Checa se a casa anterior (esquerda) é vazia e escorre a gota
                    tabuleiro[i][j-1] = 'o'
                    if tabuleiro[i+1][j-1] == '.': # Checa se a casa abaixo da que escorreu é vazia, se for a gota desce
                        tabuleiro[i+1][j-1] = 'o'
                    else:
                        for k in range (j-1, 0, -1): # Se não for, vai checando para a esquerda até o início
                            if tabuleiro[i][k-1] == '.' and tabuleiro[i+1][k] != 'o': # Checa se a casa anterior é vazia e se a debaixo não tem gota descendo
                                tabuleiro[i][k-1] = 'o'
                                if tabuleiro[i+1][k-1] == '.': # Checa se a casa na diagonal baixa esquerda é vazia
                                    tabuleiro[i+1][k-1] = 'o'
                    
                if j < matriz[1] - 1 and (tabuleiro[i][j+1] == '.' and tabuleiro[i+1][j] != 'o'): # Checa se a próxima casa (direita) é vazia, se for a gota escorre
                    tabuleiro[i][j+1] = 'o'
                    if tabuleiro[i+1][j+1] == '.': # Checa se a casa na diagonal baixa direita é vazia, se for a gota desce
                        tabuleiro[i+1][j+1] = 'o'
        else:
            pass

for i in range (0, matriz[0]):
    for j in range (0, matriz[1]):
        print(f"{tabuleiro[i][j]}", end="") # Imprime o tabuleiro final
    print(end="\n")