import sys
import collections
import heapq

N,M=map(int,sys.stdin.readline().split())
houses=[[] for _ in range(N+1)]
for _ in range(M):
    start,end,weight=map(int,sys.stdin.readline().split())
    houses[start].append([weight,end])
    houses[end].append([weight,start])
heap=[[0,1]]
visited=[0 for _ in range(N+1)]
heap_visited=[0 for _ in range(N+1)]
count=0
ans=0
max_value=-1

while heap:
    temp=heapq.heappop(heap)
    check_index=temp[1]
    check_value=temp[0]

    if visited[check_index]==0:
        visited[check_index]=1
        count+=1
        ans+=check_value
        max_value=max(max_value,check_value)
    
    if count==N:
        break

    if heap_visited[check_index]==0:
        for next in houses[check_index]:
            if visited[next[1]]==0:
                heapq.heappush(heap,next)
        heap_visited[check_index]=1

print(ans-max_value)