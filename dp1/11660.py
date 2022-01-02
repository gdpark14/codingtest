import sys
import collections

n,m=map(int,sys.stdin.readline().split())

table=[]
for i in range(n):
    temp=list(map(int,sys.stdin.readline().split()))
    table.append(temp)



for i in range(m):
    x1,y1,x2,y2=map(int,sys.stdin.readline().split())
