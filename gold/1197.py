import sys
import collections
import heapq

V,E=map(int,sys.stdin.readline().split())
nodes=[[] for _ in range(V+1)]

for _ in range(E):
    s,e,w=map(int,sys.stdin.readline().split())
    nodes[s].append([w,e])
    nodes[e].append([w,s])

heap=[[0,1]]
visited=[False]*(V+1)

count=0
ans=0
while heap:
    if count==V:
        break
    temp=heapq.heappop(heap)
    weight=temp[0]
    start=temp[1]
    if not visited[start]:
        visited[start]=True
        ans+=weight
        count+=1

        for next in nodes[start]:
            heapq.heappush(heap,next)
print(ans)