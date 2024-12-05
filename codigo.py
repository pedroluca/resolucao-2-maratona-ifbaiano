N = int(input())
V = input()
V = V.strip().split()

valores = [int(valor) for valor in V]

count = 0

for i in range (0, N):
    if i >= 2:
        if valores[i-2] == 1 and valores[i-1] == 0 and valores[i] == 0:
            count += 1

print(int(count))