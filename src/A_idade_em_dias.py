import sys 

n = int(sys.stdin.readline())
anos = n // 365
meses = (n % 365) // 30
dias = (n % 365) % 30
print(f"{anos} years")
print(f"{meses} months")
print(f"{dias} days")