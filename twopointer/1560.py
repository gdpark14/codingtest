import sys
import collections

N,M=map(int,sys.stdin.readline().split())

lists=[]
for i in range(N):
    lists.append(i+1)

ans=[]

def dfs(start,next):
    if len(start)==M:
        ans.append(start)
        return
    while next:
        new_start=start.copy()
        elem=next.pop(0)
        new_start.append(elem)
        new_next=next.copy()

        dfs(new_start,new_next)

dfs([],lists)
for list in ans:
    print(*list)