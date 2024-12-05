N = int(input())
D = int(input())
A = int(input())
count = 0

if (D < A):
    count = (N - A) + D
else:
    count = D - A

print(count)