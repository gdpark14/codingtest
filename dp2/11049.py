import sys
import collections

num=int(sys.stdin.readline())
matrix=collections.defaultdict(list)
for i in range(num):
    temp=list(map(int,sys.stdin.readline().split()))
    matrix[i]=temp

sheet=[[999999999]*(num) for _ in range(num)]

for start in range(num-1,-1,-1):
    for end in range(start,num):
        if start==end:
            sheet[start][end]=0
            continue
        for temp in range(start,end):
                sheet[start][end]=min(sheet[start][end],sheet[start][temp]+sheet[temp+1][end]+matrix[start][0]*matrix[temp][1]*matrix[end][1])

print(sheet[0][-1])