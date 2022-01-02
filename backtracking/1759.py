import sys
import collections

N,M=map(int,sys.stdin.readline().split())

lists=list(map(str,sys.stdin.readline().split()))
lists=sorted(lists)
result=[]
def dfs(start,comp):
    if len(start)==N:
        result.append(start)
        return
    for i in range(len(comp)):
        next_start=start.copy()
        next_comp=comp.copy()
        next_start.append(comp[i])
        next_comp=next_comp[i+1:]
        dfs(next_start,next_comp)

def check(comp):
    check_list=['a','e','i','o','u']
    count_m=0
    count_j=0
    for i in comp:
        if i in check_list:
            count_m+=1
        else:
            count_j+=1
    if count_m>=1 and count_j>=2:
        return 1
    else:
        return 0
dfs([],lists)
for temp in result:
    if check(temp)==1:
        print(''.join(temp))