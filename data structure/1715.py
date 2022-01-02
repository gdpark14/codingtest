import sys
import collections
import heapq

N=int(input())
cards=[]
for i in range(N):
    temp=int(input())
    heapq.heappush(cards,temp)

lists=[]
while len(cards)>1:
    a=heapq.heappop(cards)
    b=heapq.heappop(cards)
    heapq.heappush(cards,a+b)
    lists.append(a+b)
print(sum(lists))