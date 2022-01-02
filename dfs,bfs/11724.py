import sys
import collections

n,m=map(int,sys.stdin.readline().split())

graph=collections.defaultdict(list)
for i in range(m):
    u,v=map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

check=[]
def dfs(num):
    check.append(num)
    for next_num in graph[num]:
        if next_num not in check:
            dfs(next_num)

ans=0
for i in graph.keys():
    if i not in check:
        dfs(i)
        ans+=1

if len(check)!=n:
    last=n-len(check)
    ans+=last
print(ans)