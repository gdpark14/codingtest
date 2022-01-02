import sys
import collections
import heapq

V,E=map(int,sys.stdin.readline().split())
start=int(sys.stdin.readline())

nodes=[[] for _ in range(V+1)]
for i in range(E):
    a,b,c=map(int,sys.stdin.readline().split())
    nodes[a].append((c,b))

update=[5000000]*(V+1)

heap=[]

update[start]=0
heapq.heappush(heap,(0,start))
while heap:
    weight,cur=heapq.heappop(heap)

    for update_weight,next in nodes[cur]:
        temp=weight+update_weight
        if temp<update[next]:
            update[next]=temp
            heapq.heappush(heap,(update[next],next))

for i in range(V):
    if update[i+1]==5000000:
        print('INF')
    else:
        print(update[i+1])