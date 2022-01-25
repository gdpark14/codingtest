import sys
import collections
from collections import deque
import copy


R,C=map(int,sys.stdin.readline().split())
alphabet=[]
for i in range(R):
    temp=sys.stdin.readline().rstrip()
    temp=list(temp)
    alphabet.append(temp)

di=[0,-1,0,1]
dj=[-1,0,1,0]

max_ans=0

check=set()
check.add(alphabet[0][0])
def dfs(i,j,count):
    global max_ans
    max_ans=max(max_ans,count)
    for k in range(4):
        next_i=i+di[k]
        next_j=j+dj[k]
        if 0<=next_i<R and 0<=next_j<C and not alphabet[next_i][next_j] in check:
                check.add(alphabet[next_i][next_j])
                dfs(next_i,next_j,count+1)
                check.remove(alphabet[next_i][next_j])

dfs(0,0,1)
print(max_ans)