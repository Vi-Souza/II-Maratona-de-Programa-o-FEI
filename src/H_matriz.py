import sys

n = int(sys.stdin.readline())

matriz = []

for _ in range(n):
    linha = sys.stdin.readline().split()
    matriz.append(list(map(int, linha)))

r1 = 0
r2 = 0

for i in range(n):
    for j in range(n):
        if i == j:
            r1 += matriz[i][j]
        elif i + j == n - 1:
            r2 += matriz[i][j]

rt = (r1 - r2) if r1 >= r2 else (r2 - r1)

print(rt) 