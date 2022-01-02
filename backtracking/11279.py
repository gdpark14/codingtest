import sys
import collections
import heapq
n=int(sys.stdin.readline())
heap=[]

for i in range(n):
    k=int(sys.stdin.readline())
    if k==0:
        if not heap:
            print(0)
        else:
            temp=heapq.heappop(heap)
            print(temp[1])
    else:
        heapq.heappush(heap,(abs(k),k))

