X = int(input())
N = int(input())
M = []
count = 0

for i in range(0, N):
    M.append(int(input()))
    count = (X + count) - M[i]

print(count + X)