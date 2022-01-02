import sys
import collections

num=int(sys.stdin.readline())
num_pair=int(sys.stdin.readline())
ans=[1]
network=collections.defaultdict(list)

for i in range(num_pair):
    start,end=map(int,sys.stdin.readline().split())
    network[start].append(end)
    network[end].append(start)

def dfs(start,dictionary):
    if start not in dictionary.keys():
        return
    for i in dictionary[start]:
        if i not in ans:
            ans.append(i)
            dfs(i,dictionary)

dfs(1,network)
print(len(ans)-1)