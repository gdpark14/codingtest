import sys
import collections
from collections import deque

N,M=map(int,sys.stdin.readline().split())
graph=collections.defaultdict(list)
for _ in range(M):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

result=[]
def bfs(index,ans):
    check=[False]*(N+1)
    queue=deque()
    queue.append([index,0])
    check[index]=True

    while queue:
        temp=queue.popleft()
        next_index=temp[0]
        next_count=temp[1]
        ans+=next_count
    
        for i in graph[next_index]:
            if check[i]==False:
                queue.append([i,next_count+1])
                check[i]=True
    result.append([index,ans])
for i in range(1,N+1):
    bfs(i,0)
result=sorted(result,key=lambda x:x[1])
print(result[0][0])