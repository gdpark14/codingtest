import sys
import collections

N,M=map(int,sys.stdin.readline().split())

lists=[]
for i in range(N):
    lists.append(i+1)

result=[]
def dfs(start,comp):
    if len(start)==M:
        result.append(start)
        return
    for i in range(len(comp)):
        next_start=start.copy()
        next_start.append(comp[i])
        next_comp=comp.copy()
        next_comp.remove(comp[i])
        dfs(next_start,next_comp)

dfs([],lists)
for i in result:
    for j in range(len(i)):
        if j==len(i)-1:
            print(i[j])
        else:
            print(i[j],end=' ')

