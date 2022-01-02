import sys
import collections

num, weight=map(int,sys.stdin.readline().split())

items=collections.defaultdict(list)
for i in range(num):
    temp=list(map(int,sys.stdin.readline().split()))
    items[i+1]=temp

sheet=[[0]*(weight+1) for _ in range(num+1)]

for i in range(1,num+1):
    for j in range(1,weight+1):
        if items[i][0]>j:
            sheet[i][j]=sheet[i-1][j]
        else:
            need_weight=items[i][0]
            add_value=items[i][1]
            sheet[i][j]=max(sheet[i-1][j],sheet[i-1][j-need_weight]+add_value)
print(sheet[-1][-1])