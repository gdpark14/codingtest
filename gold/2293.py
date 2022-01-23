import sys
import collections
import copy

n,k=map(int,sys.stdin.readline().split())
coins=[]
dp=[0]*(k+1)
dp[0]=1
for i in range(n):
    temp=int(input())
    coins.append(temp)

for coin in coins:
    for index in range(1,k+1):
        if 0<=index-coin<k:
            dp[index]+=dp[index-coin]
print(dp[k])