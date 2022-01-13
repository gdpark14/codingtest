import sys
import collections
from typing import Counter

people_num=int(input())
cal_a,cal_b=map(int,sys.stdin.readline().split())
parent_num=int(input())
family=collections.defaultdict(list)
for _ in range(parent_num):
    a,b=map(int,sys.stdin.readline().split())
    family[a].append(b)
    family[b].append(a)

global check
check=[False]*(people_num+1)
ans=-1
def dfs(index,stop,count):
    global ans
    if index==stop:
        ans=count
    check[index]=True
    
    count+=1
    for next_index in family[index]:
        if check[next_index]!=True:
            
            dfs(next_index,stop,count)
    
dfs(cal_a,cal_b,0)
print(ans)