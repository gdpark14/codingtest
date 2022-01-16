import sys
import collections
from collections import deque

N,M,V=map(int,sys.stdin.readline().split())
graph=collections.defaultdict(list)
for _ in range(M):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for key in graph.keys():
    graph[key].sort()

dfs_ans=[]
dfs_check=[False]*(N+1)
def dfs(index):
    dfs_ans.append(index)
    dfs_check[index]=True

    for next_index in graph[index]:
        if dfs_check[next_index]==False:
            dfs_check[next_index]=True
            dfs(next_index)

bfs_ans=[]
bfs_check=[False]*(N+1)
def bfs(index):
    queue=deque()
    queue.append(index)
    while queue:
        temp=queue.popleft()
        bfs_ans.append(temp)
        bfs_check[temp]=True

        for next_index in graph[temp]:
            if bfs_check[next_index]==False:
                bfs_check[next_index]=True
                queue.append(next_index)


dfs(V)
bfs(V)
print(*dfs_ans)
print(*bfs_ans)