import sys
import collections

num=int(sys.stdin.readline())
top=list(map(int,sys.stdin.readline().split()))

dict_top=collections.defaultdict(int)

for i in range(len(top)):
    dict_top[top[i]]=i+1

temp=[]
ans=[]
for i in range(len(top)):
    if not temp:
        temp.append(top[i])
        ans.append(0)
    else:
        while temp and temp[-1]<top[i]:
            temp.pop()
        if not temp:
            ans.append(0)
        else:
            ans.append(dict_top[temp[-1]])
        temp.append(top[i])

for i in range(len(ans)):
    print(ans[i],end=' ')