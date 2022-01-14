import sys
import collections
sys.setrecursionlimit(100000)
num=int(input())
graph=collections.defaultdict(list)
for i in range(num-1):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

leaf_node=[]
check=[False]*(num+1)
def dfs(index,count):
    if index!=1 and len(graph[index])==1:
        leaf_node.append(count)
        return
    check[index]=True

    count+=1
    for next_index in graph[index]:
        if check[next_index]==False:
            dfs(next_index,count)

dfs(1,0)

if sum(leaf_node)%2==0:
    print('No')
else:
    print('Yes')