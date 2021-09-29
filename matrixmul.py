#!/usr/bin/env python3
n = int(input('Enter the value of n:'))
print('Enter values for the Matrix A')
a = []
for i in range(n):
    a.append([int(x) for x in input().split()])
print('Enter values for the Matrix B')
b = []
for j in range(n):
    b.append([int(x) for x in input().split()])
c = []
for k in range(n):
    c.append([a[k][l]*b[k][l] for l in range(n)])
print('After matrix multiplication')
print('-'*7*n)
for x in c:
    for y in x:
        print(str(y).rjust(5),end=' ')
    print()
print('-'*7*n)
