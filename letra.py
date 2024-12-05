A = input()
B = input()
count = 0
B = B.split()
for i in B:
    if A in i:
        count += 1

print(f"{(count / len(B)) * 100:.1f}")