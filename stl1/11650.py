import sys
import collections

ans=0

n=int(input())
plots=collections.defaultdict(list)
for i in range(n):
    index,color=map(int,sys.stdin.readline().split())
    plots[color].append(index)

for value in plots.values():
    value=sorted(value)
    if len(value)==1:
        continue
    else:
        for i in range(len(value)):
            if i==0:
                ans+=(value[1]-value[0])
            elif i==len(value)-1:
                ans+=(value[i]-value[i-1])
            else:
                temp=min((value[i]-value[i-1]),(value[i+1]-value[i]))
                ans+=temp
print(ans)





