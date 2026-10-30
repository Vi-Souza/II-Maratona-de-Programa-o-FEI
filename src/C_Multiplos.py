import sys

n = sys.stdin.readline().split()

A = int(n[0])
B = int(n[1])

if A % B == 0 or B % A == 0:
    print("Multiples")
else:
    print("No Multiples")
