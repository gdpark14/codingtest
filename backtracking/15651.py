import sys
import collections

N,M=map(int,sys.stdin.readline().split())
nums=[]
for i in range(N):
    nums.append(i+1)

cur_list=[]
def dfs(cur_list,candidate):
    if len(cur_list)==M:
        print(*cur_list)
        return
    for i in range(len(candidate)):
        next_cur_list=cur_list.copy()
        next_candidate=candidate.copy()

        temp=next_candidate[i]
        next_candidate=next_candidate[i:]
        next_cur_list.append(temp)

        dfs(next_cur_list,next_candidate)
dfs(cur_list,nums)