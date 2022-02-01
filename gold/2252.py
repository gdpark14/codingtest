import sys
import collections
from collections import deque

N,M=map(int,sys.stdin.readline().split())
graph=[[] for i in range(N+1)]
degree=[0 for i in range(N+1)]
queue=deque()

for _ in range(M):
    start,end=map(int,sys.stdin.readline().split())
    graph[start].append(end)
    degree[end]+=1

for i in range(1,N+1):
    if degree[i]==0:
        queue.append(i)

while queue:
    cur=queue.popleft()
    for next in graph[cur]:
        degree[next]-=1
        if degree[next]==0:
            queue.append(next)
    print(cur,end=' ')