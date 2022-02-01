import sys
import collections
from collections import deque
from queue import PriorityQueue

N,M=map(int,sys.stdin.readline().split())
graph=[[] for i in range(N+1)]
degree=[0 for i in range(N+1)]
queue=PriorityQueue()

for _ in range(M):
    start,end=map(int,sys.stdin.readline().split())
    graph[start].append(end)
    degree[end]+=1

for i in range(1,N+1):
    if degree[i]==0:
        queue.put(i)
count=0

while queue:
    cur=queue.get()
    for next in graph[cur]:
        degree[next]-=1
        if degree[next]==0:
            queue.put(next)
    print(cur,end=' ')
    count+=1

    if count==N:
        break