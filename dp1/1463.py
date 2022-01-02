import sys
import collections

num=int(sys.stdin.readline())

table=collections.defaultdict(int)
table[1]=0

for i in range(2,num+1):
    table[i]=table[i-1]+1

    if i%3==0:
        table[i]=min(table[i],table[i/3]+1)
    if i%2==0:
        table[i]=min(table[i],table[i/2]+1)
print(table[num])
