import sys
import collections

N,L,I=map(int,sys.stdin.readline().split())

dp=[[0]*(L+1) for _ in range(N+1)]
for i in range(L+1):
    dp[0][i]=1
    dp[1][i]=2
for i in range(1,N+1):
    dp[i][0]=1

for i in range(1,N+1):
    for j in range(1,L+1):
        dp[i][j]=dp[i-1][j]+dp[i-1][j-1]

for n in range(N, 0, -1):
    if I <= dp[n-1][L]:
        print('0', end="")
    else:
        print('1', end="")
        I -= dp[n-1][L]
        L -= 1