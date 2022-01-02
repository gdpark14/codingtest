import sys
import collections

N,target=map(int,sys.stdin.readline().split())
cards=list(map(int,sys.stdin.readline().split()))

temp=0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            sum_temp=cards[i]+cards[j]+cards[k]
            if sum_temp <= target and sum_temp> temp:
                temp=sum_temp
print(temp)