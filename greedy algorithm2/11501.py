import sys
import collections

T=int(input())
for i in range(T):
    day=int(input())
    price=list(map(int,sys.stdin.readline().split()))

    check=collections.defaultdict(int)
    temp=[]

    for j in range(day):
        while temp and temp[-1][1]<price[j]:
            temp.pop()
        temp.append([j,price[j]])
    
    result=0
    start=0
    for block in temp:
        k=block[1]*(block[0]-start)-sum(price[start:block[0]])
        result+=k

        start=block[0]+1
    print(result)