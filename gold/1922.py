import sys
import collections
import heapq

N=int(input())
M=int(input())
computers=[[] for _ in range(N+1)]
for _ in range(M):
    start,end,weight=map(int,sys.stdin.readline().split())
    computers[start].append([weight,end])
    computers[end].append([weight,start])

heap=[[0,1]]
visited=[0 for _ in range(N+1)]
heap_visited=[0 for _ in range(N+1)]
count=0
ans=0

while heap:
    temp=heapq.heappop(heap)
    check_index=temp[1]
    check_ans=temp[0]
    if visited[check_index]==0:
        visited[check_index]=1
        count+=1
        ans+=check_ans
    
    if count==N:
        break
    
    if heap_visited[check_index]==0:
        for next in computers[check_index]:
            heapq.heappush(heap,next)
        heap_visited[check_index]=1

print(ans)