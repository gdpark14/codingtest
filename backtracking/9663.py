import sys
import collections

N=int(sys.stdin.readline())
result=[]
def check(lists,cnt):
    length=len(lists)
    for i in range(len(lists)):
        if abs(cnt-lists[i])==length-i:
            return False
    return True

def dfs(start,comp):
    if len(start)==N:
        result.append(start)
        return
    for i in range(len(comp)):
        next_start=start.copy()
        next_comp=comp.copy()
        if check(next_start,comp[i])==True:
            next_start.append(comp[i])
            next_comp.remove(comp[i])
            dfs(next_start,next_comp)
        
lists=[]
for i in range(N):
    lists.append(i+1)
dfs([],lists)
print(len(result))