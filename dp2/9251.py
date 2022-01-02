import sys
import collections

a=sys.stdin.readline().strip().upper()
b=sys.stdin.readline().strip().upper()

matrix=[[0]*(len(b)+1) for _ in range(len(a)+1)]

matrix[0][0]=0
for i in range(0,len(a)):
    for j in range(0,len(b)):
        if a[i]==b[j]:
            matrix[i+1][j+1]=matrix[i][j]+1
        else:
            matrix[i+1][j+1]=max(matrix[i][j+1],matrix[i+1][j])

print(matrix[len(a)][len(b)])