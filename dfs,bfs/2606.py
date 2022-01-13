import sys
import collections

com_num=int(input())
pair_num=int(input())
computers=collections.defaultdict(list)
for _  in range(pair_num):
    start,end=map(int,sys.stdin.readline().split())
    computers[start].append(end)
    computers[end].append(start)

check=[False]*(com_num+1)
count=0

def dfs(index):
    global check
    check[index]=True

    global count
    if index!=1:
        count+=1

    for next_index in computers[index]:
        if check[next_index]==False:
            dfs(next_index)
dfs(1)
print(count)