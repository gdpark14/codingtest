import sys
import collections
from collections import deque

N=int(input())
buildings=[[] for _ in range(N+1)]
buildings_time=[0 for _ in range(N+1)]

inter_time=[0 for _ in range(N+1)]

degree=[0 for _ in range(N+1)]

for i in range(1,N+1):
    temp=list(map(int,sys.stdin.readline().split()))
    time=temp[0]
    buildings_time[i]=time

    for j in range(1,len(temp)):
        if temp[j]!=-1:
            buildings[temp[j]].append(i)
    degree[i]=len(temp)-2

queue=deque()

for i in range(1,N+1):
    if degree[i]==0:
        queue.append([i,buildings_time[i]])

ans=[0 for _ in range(N+1)]
while queue:
    temp=queue.popleft()
    cur=temp[0]
    cur_time=temp[1]

    for next in buildings[cur]:
        degree[next]-=1
        inter_time[next]=max(cur_time+buildings_time[next],inter_time[next])
        
        if degree[next]==0:
            queue.append([next,inter_time[next]])

    ans[cur]=cur_time

for i in range(1,N+1):
    print(ans[i])