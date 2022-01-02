import sys
import collections

N,M=map(int,sys.stdin.readline().split())

lists=list(map(int,sys.stdin.readline().split()))


result=[]
def dfs(start,comp):
    if sum(start)==M and start:
        result.append(start)
    if not comp:
        return
    for i in range(len(comp)):
        next_start=start.copy()
        next_start.append(comp[i])
        next_comp=comp.copy()
        next_comp=next_comp[i+1:]
        dfs(next_start,next_comp)

dfs([],lists)
print(len(result))