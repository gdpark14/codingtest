import collections
import sys
sys.setrecursionlimit(99999)

N=int(input())
graph=collections.defaultdict(list)
for i in range(N-1):
    index,node,weight=map(int,sys.stdin.readline().split())
    graph[index].append([node,weight])

global ans
ans=0

def diameter(index):
    global ans
    
    if not graph[index]:
        return 0
    nodes=graph[index]

    temp=0
    temp_list=[]

    for i in range(len(nodes)):
        next=diameter(nodes[i][0])+nodes[i][1]

        temp_list.append(next)
        temp=max(temp,next)

    temp_list=sorted(temp_list)
    if len(temp_list)>=2:
        ans=max(ans,temp_list[-1]+temp_list[-2])
    if len(temp_list)==1:
        ans=max(ans,temp_list[-1])

    return temp


diameter(1)
print(ans)